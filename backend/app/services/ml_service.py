"""
Servicio de Machine Learning para predicción de razas de perros.
Carga el modelo entrenado y realiza inferencia.
"""

import torch
import torch.nn as nn
import torchvision.models as models
from torchvision.models import EfficientNet_V2_S_Weights
import cv2
import numpy as np
import joblib
import json
from pathlib import Path
from typing import List, Dict, Tuple
import albumentations as A
from albumentations.pytorch import ToTensorV2


class DogBreedPredictor:
    """
    Servicio de predicción de razas de perros usando modelo CNN entrenado.
    """
    
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.label_encoder = None
        self.breed_descriptions = None
        self.img_size = (224, 224)
        self.normalization = {
            'mean': [0.485, 0.456, 0.406],
            'std': [0.229, 0.224, 0.225]
        }
        self.transform = self._get_transform()
        
        # Rutas a los archivos del modelo
        self.models_dir = Path(__file__).parent.parent.parent / 'ML' / 'models'
        self.model_path = self.models_dir / 'dog_breed_model.pth'
        self.encoder_path = self.models_dir / 'label_encoder.pkl'
        
        # Ruta al archivo de descripciones
        self.data_dir = Path(__file__).parent.parent / 'data'
        self.descriptions_path = self.data_dir / 'breed_descriptions.json'
        
        # Cargar descripciones de razas
        self._load_breed_descriptions()
        
    def _get_transform(self):
        """
        Transformaciones para preprocesamiento de imágenes (sin augmentation).
        """
        return A.Compose([
            A.Resize(224, 224),
            A.Normalize(
                mean=self.normalization['mean'],
                std=self.normalization['std']
            ),
            ToTensorV2(),
        ])
    
    def _load_breed_descriptions(self):
        """
        Carga el archivo JSON con descripciones de razas.
        """
        try:
            if self.descriptions_path.exists():
                with open(self.descriptions_path, 'r', encoding='utf-8') as f:
                    self.breed_descriptions = json.load(f)
                print(f"✅ Descripciones de razas cargadas: {len(self.breed_descriptions)} razas")
            else:
                print(f"⚠️  Archivo de descripciones no encontrado: {self.descriptions_path}")
                self.breed_descriptions = {}
        except Exception as e:
            print(f"⚠️  Error al cargar descripciones: {e}")
            self.breed_descriptions = {}
    
    def _get_breed_info(self, breed_name: str) -> Dict:
        """
        Obtiene información descriptiva de una raza.
        
        Args:
            breed_name: Nombre de la raza
            
        Returns:
            Diccionario con información de la raza o dict vacío si no existe
        """
        if self.breed_descriptions and breed_name in self.breed_descriptions:
            return self.breed_descriptions[breed_name]
        return {}
    
    def _create_model(self, num_classes: int, model_name: str = 'efficientnet_v2_s'):
        """
        Recrea la arquitectura del modelo para cargar los pesos.
        """
        if model_name == 'efficientnet_v2_s':
            # Cargar arquitectura base
            weights = EfficientNet_V2_S_Weights.IMAGENET1K_V1
            model = models.efficientnet_v2_s(weights=None)  # Sin pesos, los cargaremos después
            
            # Adaptar clasificador (misma arquitectura que en entrenamiento)
            in_features = model.classifier[1].in_features
            model.classifier = nn.Sequential(
                nn.Dropout(p=0.3, inplace=True),
                nn.Linear(in_features, 512),
                nn.ReLU(inplace=True),
                nn.Dropout(p=0.3),
                nn.Linear(512, num_classes)
            )
        
        return model
    
    def load_model(self):
        """
        Carga el modelo entrenado y el label encoder.
        """
        try:
            # Cargar label encoder
            print(f"📥 Cargando label encoder desde: {self.encoder_path}")
            self.label_encoder = joblib.load(self.encoder_path)
            num_classes = len(self.label_encoder.classes_)
            print(f"✅ Label encoder cargado. Clases: {num_classes}")
            
            # Cargar modelo
            print(f"📥 Cargando modelo desde: {self.model_path}")
            checkpoint = torch.load(self.model_path, map_location=self.device)
            
            # Extraer información del checkpoint
            model_name = checkpoint.get('model_name', 'efficientnet_v2_s')
            
            # Crear modelo con arquitectura correcta
            self.model = self._create_model(num_classes, model_name)
            
            # Cargar pesos
            self.model.load_state_dict(checkpoint['model_state_dict'])
            self.model.to(self.device)
            self.model.eval()  # Modo evaluación
            
            print(f"✅ Modelo cargado exitosamente")
            print(f"   - Arquitectura: {model_name}")
            print(f"   - Val Accuracy: {checkpoint.get('val_acc', 0)*100:.2f}%")
            print(f"   - Device: {self.device}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar modelo: {e}")
            raise
    
    def preprocess_image(self, image_data: bytes) -> torch.Tensor:
        """
        Preprocesa imagen desde bytes para inferencia.
        
        Args:
            image_data: Bytes de la imagen
            
        Returns:
            Tensor preprocesado listo para el modelo
        """
        # Convertir bytes a numpy array
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            raise ValueError("No se pudo decodificar la imagen")
        
        # Convertir BGR a RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Aplicar transformaciones
        transformed = self.transform(image=image)['image']
        
        # Añadir dimensión de batch
        transformed = transformed.unsqueeze(0)
        
        return transformed
    
    def predict(self, image_data: bytes, top_k: int = 5) -> List[Dict]:
        """
        Realiza predicción de raza de perro en una imagen.
        
        Args:
            image_data: Bytes de la imagen
            top_k: Número de predicciones top a retornar (default: 5)
            
        Returns:
            Lista de diccionarios con raza y confianza, ordenados por confianza
        """
        if self.model is None:
            raise RuntimeError("Modelo no cargado. Ejecuta load_model() primero.")
        
        # Preprocesar imagen
        image_tensor = self.preprocess_image(image_data)
        image_tensor = image_tensor.to(self.device)
        
        # Inferencia
        with torch.no_grad():
            outputs = self.model(image_tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            
            # Obtener top-k predicciones
            top_probs, top_indices = torch.topk(probabilities, min(top_k, len(self.label_encoder.classes_)))
        
        # Convertir a formato de salida con descripciones
        predictions = []
        for prob, idx in zip(top_probs[0].cpu().numpy(), top_indices[0].cpu().numpy()):
            breed = self.label_encoder.inverse_transform([idx])[0]
            
            # Crear predicción base
            prediction = {
                'breed': breed,
                'confidence': float(prob),
                'confidence_percentage': f"{float(prob)*100:.2f}%"
            }
            
            # Agregar información descriptiva de la raza
            breed_info = self._get_breed_info(breed)
            if breed_info:
                prediction.update({
                    'name_es': breed_info.get('name_es'),
                    'origin': breed_info.get('origin'),
                    'size': breed_info.get('size'),
                    'temperament': breed_info.get('temperament'),
                    'description': breed_info.get('description'),
                    'life_expectancy': breed_info.get('life_expectancy')
                })
            
            predictions.append(prediction)
        
        return predictions
    
    def get_model_info(self) -> Dict:
        """
        Retorna información sobre el modelo cargado.
        """
        if self.model is None:
            return {'status': 'not_loaded'}
        
        return {
            'status': 'loaded',
            'device': str(self.device),
            'num_classes': len(self.label_encoder.classes_),
            'img_size': self.img_size,
            'all_breeds': self.label_encoder.classes_.tolist()
        }


# Singleton - Instancia global del predictor
_predictor_instance = None

def get_predictor() -> DogBreedPredictor:
    """
    Retorna instancia singleton del predictor.
    Carga el modelo en el primer acceso.
    """
    global _predictor_instance
    
    if _predictor_instance is None:
        _predictor_instance = DogBreedPredictor()
        _predictor_instance.load_model()
    
    return _predictor_instance 