"""
FastAPI Backend - Dog Breed Identifier ML
API para clasificación de razas de perros usando Deep Learning.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import prediction_routes
import uvicorn

# Crear aplicación FastAPI
app = FastAPI(
    title="Dog Breed Identifier API",
    description="""
    API de Machine Learning para identificación de razas de perros.
    
    **Características:**
    - 🐕 Clasificación de 120 razas de perros
    - 🎯 90.22% de accuracy en test set
    - 🧠 Modelo: EfficientNetV2-S con Transfer Learning
    - ⚡ GPU/CPU support
    
    **Endpoints principales:**
    - `POST /api/v1/predict/` - Predecir raza de perro
    - `GET /api/v1/predict/model-info` - Información del modelo
    - `GET /api/v1/predict/breeds` - Lista de razas
    """,
    version="1.0.0",
    contact={
        "name": "Dog Breed Identifier Team",
    },
    license_info={
        "name": "MIT",
    }
)

# Configurar CORS para permitir requests desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(prediction_routes.router)


@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raíz con información de la API.
    """
    return {
        "message": "🐕 Dog Breed Identifier API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "health": "/api/v1/predict/health"
    }


@app.get("/health", tags=["Root"])
def health():
    """
    Health check general de la API.
    """
    return {
        "status": "healthy",
        "service": "Dog Breed Identifier API"
    }


# Evento al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    """
    Carga el modelo ML al iniciar la aplicación.
    """
    print("=" * 70)
    print("🚀 Iniciando Dog Breed Identifier API...")
    print("=" * 70)
    
    try:
        from .services.ml_service import get_predictor
        predictor = get_predictor()
        print("✅ Modelo cargado exitosamente")
        print("=" * 70)
    except Exception as e:
        print(f"❌ Error al cargar modelo: {e}")
        print("=" * 70)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Limpieza al cerrar la aplicación.
    """
    print("🛑 Cerrando Dog Breed Identifier API...")


# Para ejecutar directamente con Python
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Hot reload en desarrollo
    ) 