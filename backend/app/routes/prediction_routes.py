"""
Rutas de FastAPI para predicción de razas de perros.
"""

from fastapi import APIRouter, UploadFile, File, Query, HTTPException
from ..controllers.prediction_controller import PredictionController
from ..schema.prediction_schema import PredictionResponse, ModelInfoResponse, ErrorResponse

# Crear router
router = APIRouter(
    prefix="/api/v1/predict",
    tags=["Prediction"],
    responses={
        500: {"model": ErrorResponse, "description": "Error interno del servidor"},
    }
)


@router.post(
    "/",
    response_model=PredictionResponse,
    summary="Predecir raza de perro",
    description="""
    Sube una imagen de un perro y obtén las predicciones de raza con confianza.
    
    **Parámetros:**
    - **file**: Imagen del perro (JPG, PNG, etc.)
    - **top_k**: Número de predicciones top a retornar (default: 5, max: 10)
    
    **Returns:**
    - Lista de predicciones ordenadas por confianza
    - Raza principal y su confianza
    - Timestamp de la predicción
    """,
    responses={
        200: {
            "description": "Predicción exitosa",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "predictions": [
                            {
                                "breed": "golden_retriever",
                                "confidence": 0.8542,
                                "confidence_percentage": "85.42%"
                            }
                        ],
                        "top_breed": "golden_retriever",
                        "top_confidence": 0.8542,
                        "timestamp": "2026-02-10T12:00:00"
                    }
                }
            }
        },
        400: {
            "model": ErrorResponse,
            "description": "Imagen inválida o error en datos de entrada"
        }
    }
)
async def predict_dog_breed(
    file: UploadFile = File(..., description="Imagen del perro"),
    top_k: int = Query(default=5, ge=1, le=10, description="Número de predicciones top")
):
    """
    Endpoint principal de predicción.
    """
    return await PredictionController.predict_breed(file, top_k)


@router.get(
    "/model-info",
    response_model=ModelInfoResponse,
    summary="Información del modelo",
    description="Obtiene información sobre el modelo de ML cargado, incluyendo lista de todas las razas."
)
def get_model_information():
    """
    Endpoint para obtener información del modelo.
    """
    return PredictionController.get_model_info()


@router.get(
    "/health",
    summary="Health check",
    description="Verifica el estado de salud del servicio de predicción.",
    response_model=dict
)
def health_check():
    """
    Endpoint de health check.
    """
    return PredictionController.health_check()


@router.get(
    "/breeds",
    response_model=dict,
    summary="Lista de razas",
    description="Obtiene la lista completa de razas que el modelo puede clasificar."
)
def list_all_breeds():
    """
    Endpoint para listar todas las razas disponibles.
    """
    info = PredictionController.get_model_info()
    
    if info.status != "loaded":
        raise HTTPException(status_code=503, detail="Modelo no cargado")
    
    return {
        "total_breeds": info.num_classes,
        "breeds": sorted(info.all_breeds) if info.all_breeds else []
    }
