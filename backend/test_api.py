"""
Script de prueba para la API de Dog Breed Identifier.
Ejecutar después de iniciar el servidor FastAPI.
"""

import requests
from pathlib import Path
import json

# Configuración
BASE_URL = "http://localhost:8000"
API_PREFIX = "/api/v1/predict"


def print_section(title: str):
    """Imprime separador de sección"""
    print("\n" + "="*70)
    print(f"🔍 {title}")
    print("="*70)


def test_root():
    """Prueba endpoint raíz"""
    print_section("Test 1: Root Endpoint")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200
        print("✅ PASSED")
    except Exception as e:
        print(f"❌ FAILED: {e}")


def test_health_check():
    """Prueba health check"""
    print_section("Test 2: Health Check")
    
    try:
        response = requests.get(f"{BASE_URL}{API_PREFIX}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        print("✅ PASSED")
    except Exception as e:
        print(f"❌ FAILED: {e}")


def test_model_info():
    """Prueba obtener información del modelo"""
    print_section("Test 3: Model Info")
    
    try:
        response = requests.get(f"{BASE_URL}{API_PREFIX}/model-info")
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Status: {data['status']}")
        print(f"Device: {data.get('device', 'N/A')}")
        print(f"Num Classes: {data.get('num_classes', 'N/A')}")
        print(f"Image Size: {data.get('img_size', 'N/A')}")
        assert response.status_code == 200
        assert data["status"] == "loaded"
        print("✅ PASSED")
        return data
    except Exception as e:
        print(f"❌ FAILED: {e}")
        return None


def test_breeds_list():
    """Prueba obtener lista de razas"""
    print_section("Test 4: Breeds List")
    
    try:
        response = requests.get(f"{BASE_URL}{API_PREFIX}/breeds")
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Total Breeds: {data['total_breeds']}")
        print(f"First 10 breeds: {data['breeds'][:10]}")
        assert response.status_code == 200
        assert len(data["breeds"]) > 0
        print("✅ PASSED")
    except Exception as e:
        print(f"❌ FAILED: {e}")


def test_prediction(image_path: str = None):
    """Prueba predicción con imagen"""
    print_section("Test 5: Prediction")
    
    if not image_path:
        print("⚠️ SKIPPED: No se proporcionó ruta de imagen")
        print("Para probar predicción, ejecuta:")
        print('   python test_api.py --image "ruta/a/imagen.jpg"')
        return
    
    image_path = Path(image_path)
    
    if not image_path.exists():
        print(f"❌ FAILED: Imagen no encontrada: {image_path}")
        return
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            params = {"top_k": 5}
            
            print(f"Enviando imagen: {image_path.name}")
            response = requests.post(
                f"{BASE_URL}{API_PREFIX}/",
                files=files,
                params=params
            )
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n🐕 Predicción exitosa!")
            print(f"Raza principal: {data['top_breed']}")
            print(f"Confianza: {data['top_confidence']*100:.2f}%")
            print(f"\nTop {len(data['predictions'])} predicciones:")
            for i, pred in enumerate(data['predictions'], 1):
                print(f"  {i}. {pred['breed']:30s} - {pred['confidence_percentage']}")
            print("✅ PASSED")
        else:
            print(f"Error: {response.text}")
            print("❌ FAILED")
            
    except Exception as e:
        print(f"❌ FAILED: {e}")


def test_invalid_file():
    """Prueba con archivo inválido"""
    print_section("Test 6: Invalid File (Negative Test)")
    
    try:
        # Crear archivo de texto temporal
        test_content = b"This is not an image"
        files = {"file": ("test.txt", test_content, "text/plain")}
        
        response = requests.post(
            f"{BASE_URL}{API_PREFIX}/",
            files=files
        )
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Debe retornar error 400
        assert response.status_code == 400
        print("✅ PASSED (error manejado correctamente)")
        
    except Exception as e:
        print(f"❌ FAILED: {e}")


def run_all_tests(image_path: str = None):
    """Ejecuta todas las pruebas"""
    print("\n" + "="*70)
    print("🧪 INICIANDO PRUEBAS DE LA API - DOG BREED IDENTIFIER")
    print("="*70)
    print(f"URL Base: {BASE_URL}")
    print(f"Prefijo API: {API_PREFIX}")
    
    # Verificar que el servidor esté corriendo
    try:
        requests.get(BASE_URL, timeout=2)
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: El servidor no está corriendo")
        print("Por favor, inicia el servidor primero:")
        print("   cd backend")
        print("   uvicorn app.main:app --reload")
        return
    
    # Ejecutar pruebas
    test_root()
    test_health_check()
    test_model_info()
    test_breeds_list()
    test_prediction(image_path)
    test_invalid_file()
    
    # Resumen
    print("\n" + "="*70)
    print("✅ PRUEBAS COMPLETADAS")
    print("="*70)
    print("\n💡 Siguiente paso: Probar con Swagger UI en http://localhost:8000/docs")


if __name__ == "__main__":
    import sys
    
    # Parsear argumentos simples
    image_path = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "--image" and len(sys.argv) > 2:
            image_path = sys.argv[2]
        else:
            image_path = sys.argv[1]
    
    run_all_tests(image_path)
