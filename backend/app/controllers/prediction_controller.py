"""
Controlador para manejar lógica de predicción de razas de perros.
"""

from fastapi import UploadFile, HTTPException
from ..services.ml_service import get_predictor
from ..schema.prediction_schema import PredictionResponse, ModelInfoResponse, ErrorResponse, BreedPrediction
from typing import List
from datetime import datetime


class PredictionController:
    """
    Controlador para operaciones de predicción.
    """
    
    @staticmethod
    async def predict_breed(file: UploadFile, top_k: int = 5) -> PredictionResponse:
        """
        Predice la raza de perro en una imagen.
        
        Args:
            file: Archivo de imagen subido
            top_k: Número de predicciones top a retornar
            
        Returns:
            PredictionResponse con las predicciones
            
        Raises:
            HTTPException: Si hay error en procesamiento
        """
        try:
            # Validar tipo de archivo
            if not file.content_type.startswith('image/'):
                raise HTTPException(
                    status_code=400,
                    detail=f"Tipo de archivo inválido: {file.content_type}. Se esperaba una imagen."
                )
            
            # Leer imagen
            image_data = await file.read()
            
            if len(image_data) == 0:
                raise HTTPException(
                    status_code=400,
                    detail="Archivo de imagen vacío"
                )
            
            # Obtener predictor y realizar predicción
            predictor = get_predictor()
            predictions = predictor.predict(image_data, top_k=top_k)
            
            # Formatear response
            breed_predictions = [BreedPrediction(**pred) for pred in predictions]
            
            return PredictionResponse(
                success=True,
                predictions=breed_predictions,
                top_breed=predictions[0]['breed'],
                top_confidence=predictions[0]['confidence'],
                timestamp=datetime.now()
            )
            
        except HTTPException:
            raise
        except ValueError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Error al procesar imagen: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error interno del servidor: {str(e)}"
            )
    
    @staticmethod
    def get_model_info() -> ModelInfoResponse:
        """
        Obtiene información sobre el modelo cargado.
        
        Returns:
            ModelInfoResponse con información del modelo
        """
        try:
            predictor = get_predictor()
            info = predictor.get_model_info()
            
            return ModelInfoResponse(**info)
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error al obtener información del modelo: {str(e)}"
            )
    
    @staticmethod
    def health_check() -> dict:
        """
        Verifica el estado de salud del servicio.
        
        Returns:
            Diccionario con estado del servicio
        """
        try:
            predictor = get_predictor()
            model_loaded = predictor.model is not None
            
            return {
                "status": "healthy" if model_loaded else "unhealthy",
                "model_loaded": model_loaded,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "model_loaded": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
