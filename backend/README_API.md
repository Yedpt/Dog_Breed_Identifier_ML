# 🚀 API Dog Breed Identifier - Guía de Ejecución

## 📋 Backend Implementado

### ✅ Archivos creados:

1. **`backend/app/services/ml_service.py`**
   - ✅ Clase `DogBreedPredictor` para cargar modelo y hacer predicciones
   - ✅ Singleton pattern para reutilizar instancia
   - ✅ Preprocesamiento de imágenes con Albumentations
   - ✅ Top-K predicciones con softmax

2. **`backend/app/schema/prediction_schema.py`**
   - ✅ `BreedPrediction` - Schema de predicción individual
   - ✅ `PredictionResponse` - Response con top-K
   - ✅ `ModelInfoResponse` - Info del modelo
   - ✅ `ErrorResponse` - Manejo de errores

3. **`backend/app/controllers/prediction_controller.py`**
   - ✅ Lógica de negocio para predicciones
   - ✅ Validación de archivos
   - ✅ Health check

4. **`backend/app/routes/prediction_routes.py`**
   - ✅ `POST /api/v1/predict/` - Subir imagen y predecir
   - ✅ `GET /api/v1/predict/model-info` - Info del modelo
   - ✅ `GET /api/v1/predict/health` - Health check
   - ✅ `GET /api/v1/predict/breeds` - Lista de razas

5. **`backend/app/main.py`**
   - ✅ App FastAPI configurada
   - ✅ CORS habilitado
   - ✅ Carga automática del modelo al iniciar

---

## 🏃 Cómo ejecutar la API

### Paso 1: Activar entorno virtual

```powershell
# Desde el directorio raíz del proyecto
.\.venv\Scripts\Activate.ps1
```

### Paso 2: Navegar a backend

```powershell
cd backend
```

### Paso 3: Ejecutar servidor FastAPI

```powershell
# Opción 1: Usando uvicorn directamente
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Opción 2: Ejecutando main.py directamente
python -m app.main
```

### Paso 4: Verificar que está corriendo

La API debería iniciar y verás:

```
======================================================================
🚀 Iniciando Dog Breed Identifier API...
======================================================================
📥 Cargando label encoder desde: ...\backend\ML\models\label_encoder.pkl
✅ Label encoder cargado. Clases: 120
📥 Cargando modelo desde: ...\backend\ML\models\dog_breed_model.pth
✅ Modelo cargado exitosamente
   - Arquitectura: efficientnet_v2_s
   - Val Accuracy: 89.50%
   - Device: cuda (o cpu)
✅ Modelo cargado exitosamente
======================================================================
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## 📡 Endpoints Disponibles

### 1. **Documentación Interactiva**

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 2. **Predicción de Raza**

```bash
POST /api/v1/predict/
Content-Type: multipart/form-data

# Parámetros:
- file: Imagen del perro (jpg, png, etc.)
- top_k: Número de predicciones (default: 5)
```

**Ejemplo con curl:**
```bash
curl -X POST "http://localhost:8000/api/v1/predict/?top_k=5" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@ruta/a/tu/imagen.jpg"
```

**Ejemplo con Python:**
```python
import requests

url = "http://localhost:8000/api/v1/predict/"
files = {"file": open("dog_image.jpg", "rb")}
params = {"top_k": 5}

response = requests.post(url, files=files, params=params)
print(response.json())
```

**Response esperado:**
```json
{
  "success": true,
  "predictions": [
    {
      "breed": "golden_retriever",
      "confidence": 0.8542,
      "confidence_percentage": "85.42%"
    },
    {
      "breed": "labrador_retriever",
      "confidence": 0.0821,
      "confidence_percentage": "8.21%"
    }
  ],
  "top_breed": "golden_retriever",
  "top_confidence": 0.8542,
  "timestamp": "2026-02-10T12:00:00"
}
```

### 3. **Información del Modelo**

```bash
GET /api/v1/predict/model-info
```

```json
{
  "status": "loaded",
  "device": "cuda",
  "num_classes": 120,
  "img_size": [224, 224],
  "all_breeds": ["affenpinscher", "afghan_hound", ...]
}
```

### 4. **Lista de Razas**

```bash
GET /api/v1/predict/breeds
```

```json
{
  "total_breeds": 120,
  "breeds": ["affenpinscher", "afghan_hound", ...]
}
```

### 5. **Health Check**

```bash
GET /api/v1/predict/health
GET /health
```

---

## 🧪 Probar la API

### Opción 1: Usando Swagger UI (Recomendado)

1. Abre http://localhost:8000/docs
2. Click en `POST /api/v1/predict/`
3. Click en "Try it out"
4. Sube una imagen de perro
5. Click en "Execute"

### Opción 2: Usando Python Script

Crear archivo `test_api.py`:

```python
import requests
from pathlib import Path

# URL de la API
BASE_URL = "http://localhost:8000"

def test_health():
    """Verificar que la API esté corriendo"""
    response = requests.get(f"{BASE_URL}/api/v1/predict/health")
    print("Health Check:", response.json())

def test_model_info():
    """Obtener información del modelo"""
    response = requests.get(f"{BASE_URL}/api/v1/predict/model-info")
    print("Model Info:", response.json())

def test_prediction(image_path: str):
    """Probar predicción con una imagen"""
    with open(image_path, "rb") as f:
        files = {"file": f}
        params = {"top_k": 5}
        response = requests.post(
            f"{BASE_URL}/api/v1/predict/",
            files=files,
            params=params
        )
    
    result = response.json()
    print(f"\nPredicción para: {image_path}")
    print(f"Raza principal: {result['top_breed']}")
    print(f"Confianza: {result['top_confidence']*100:.2f}%")
    print("\nTop 5 predicciones:")
    for pred in result['predictions']:
        print(f"  - {pred['breed']}: {pred['confidence_percentage']}")

if __name__ == "__main__":
    test_health()
    test_model_info()
    # test_prediction("ruta/a/imagen.jpg")  # Descomenta y pon ruta real
```

---

## 🔧 Troubleshooting

### Error: "Modelo no cargado"

Verifica que existan los archivos:
- `backend/ML/models/dog_breed_model.pth`
- `backend/ML/models/label_encoder.pkl`

### Error: "CUDA not available"

El modelo funcionará en CPU. Si quieres usar GPU:
```powershell
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Error: "Module not found"

```powershell
# Instalar dependencias faltantes
pip install fastapi uvicorn python-multipart
```

---

## 📊 Métricas del Modelo

- **Test Accuracy**: 90.22%
- **Val Accuracy**: 89.50%
- **Clases**: 120 razas de perros
- **Arquitectura**: EfficientNetV2-S
- **Overfitting**: -8.91% (generaliza mejor que training)

---

## 🎯 Próximos Pasos

1. ✅ **Backend completado** → API funcional
2. ⬜ **Frontend React** → Interfaz de usuario
3. ⬜ **Sistema de Feedback** → Mejora continua
4. ⬜ **A/B Testing** → Comparar modelos
5. ⬜ **Data Drift Monitoring** → Detectar degradación
6. ⬜ **Dockerización** → Deploy en contenedores
7. ⬜ **Cloud Deploy** → Producción en AWS/GCP/Azure
