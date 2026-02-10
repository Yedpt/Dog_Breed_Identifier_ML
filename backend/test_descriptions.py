"""
Script de prueba para verificar que las descripciones de razas funcionan.
Simula una predicción y muestra el formato de respuesta con descripciones.
"""

import json
from pathlib import Path

# Cargar descripciones
descriptions_path = Path(__file__).parent / 'app' / 'data' / 'breed_descriptions.json'

with open(descriptions_path, 'r', encoding='utf-8') as f:
    descriptions = json.load(f)

# Simular respuesta de predicción para Yorkshire Terrier
print("=" * 80)
print("🐕 EJEMPLO DE RESPUESTA CON DESCRIPCIONES")
print("=" * 80)
print()

# Simulación de top-3 predicciones
example_predictions = [
    {
        "breed": "Yorkshire_terrier",
        "confidence": 0.8148,
        "confidence_percentage": "81.48%"
    },
    {
        "breed": "silky_terrier", 
        "confidence": 0.1076,
        "confidence_percentage": "10.76%"
    },
    {
        "breed": "Australian_terrier",
        "confidence": 0.0451,
        "confidence_percentage": "4.51%"
    }
]

# Enriquecer con descripciones
enriched_predictions = []
for pred in example_predictions:
    breed = pred['breed']
    breed_info = descriptions.get(breed, {})
    
    enriched = {
        **pred,
        'name_es': breed_info.get('name_es'),
        'origin': breed_info.get('origin'),
        'size': breed_info.get('size'),
        'temperament': breed_info.get('temperament'),
        'description': breed_info.get('description'),
        'life_expectancy': breed_info.get('life_expectancy')
    }
    enriched_predictions.append(enriched)

# Respuesta completa
response = {
    "success": True,
    "predictions": enriched_predictions,
    "top_breed": "Yorkshire_terrier",
    "top_confidence": 0.8148,
    "timestamp": "2026-02-10T15:30:00"
}

# Mostrar JSON formateado
print(json.dumps(response, indent=2, ensure_ascii=False))

print()
print("=" * 80)
print("✅ DATOS INCLUIDOS EN CADA PREDICCIÓN:")
print("=" * 80)
print()

# Mostrar primer predicción detallada
top_pred = enriched_predictions[0]
print(f"🏆 Raza detectada: {top_pred['breed']}")
print(f"📊 Confianza: {top_pred['confidence_percentage']}")
print()
print(f"📝 Nombre en español: {top_pred['name_es']}")
print(f"🌍 Origen: {top_pred['origin']}")
print(f"📏 Tamaño: {top_pred['size']}")
print(f"🧠 Temperamento: {top_pred['temperament']}")
print(f"📖 Descripción: {top_pred['description']}")
print(f"⏳ Esperanza de vida: {top_pred['life_expectancy']}")
print()

print("=" * 80)
print(f"📊 Total de razas con descripciones: {len(descriptions)}")
print("=" * 80)
