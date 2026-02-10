"""
Schemas Pydantic para validación de requests/responses de predicción.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class BreedPrediction(BaseModel):
    """Predicción individual de raza con confianza."""
    breed: str = Field(..., description="Nombre de la raza")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confianza (0-1)")
    confidence_percentage: str = Field(..., description="Confianza en porcentaje")
    
    # Información descriptiva de la raza
    name_es: Optional[str] = Field(None, description="Nombre en español")
    origin: Optional[str] = Field(None, description="País/región de origen")
    size: Optional[str] = Field(None, description="Tamaño y peso")
    temperament: Optional[str] = Field(None, description="Temperamento típico")
    description: Optional[str] = Field(None, description="Descripción general de la raza")
    life_expectancy: Optional[str] = Field(None, description="Esperanza de vida")
    
    class Config:
        json_schema_extra = {
            "example": {
                "breed": "golden_retriever",
                "confidence": 0.8542,
                "confidence_percentage": "85.42%",
                "name_es": "Golden Retriever",
                "origin": "Escocia",
                "size": "Grande (25-34 kg)",
                "temperament": "Amigable, int eligente y devoto",
                "description": "Una de las razas más populares. Excepcional perro familiar, de asistencia y terapia.",
                "life_expectancy": "10-12 años"
            }
        }


class PredictionResponse(BaseModel):
    """Response de predicción con top-k razas."""
    success: bool = Field(..., description="Indica si la predicción fue exitosa")
    predictions: List[BreedPrediction] = Field(..., description="Lista de predicciones ordenadas por confianza")
    top_breed: str = Field(..., description="Raza con mayor confianza")
    top_confidence: float = Field(..., description="Confianza de la predicción principal")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp de la predicción")
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
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
        }


class ModelInfoResponse(BaseModel):
    """Información sobre el modelo cargado."""
    status: str = Field(..., description="Estado del modelo (loaded/not_loaded)")
    device: Optional[str] = Field(None, description="Dispositivo (cuda/cpu)")
    num_classes: Optional[int] = Field(None, description="Número de razas que puede clasificar")
    img_size: Optional[tuple] = Field(None, description="Tamaño de imagen esperado")
    all_breeds: Optional[List[str]] = Field(None, description="Lista de todas las razas")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "loaded",
                "device": "cuda",
                "num_classes": 120,
                "img_size": [224, 224],
                "all_breeds": ["affenpinscher", "afghan_hound", "..."]
            }
        }


class ErrorResponse(BaseModel):
    """Response para errores."""
    success: bool = Field(False, description="Siempre False en errores")
    error: str = Field(..., description="Mensaje de error")
    detail: Optional[str] = Field(None, description="Detalle adicional del error")
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": False,
                "error": "Invalid image format",
                "detail": "Could not decode image data"
            }
        }
