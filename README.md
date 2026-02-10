<div align="center">

# 🐕 DogBreed AI

### Identificador de Razas de Perros con Inteligencia Artificial

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.10.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.119.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19.2.0-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-90.22%25-success?style=for-the-badge" alt="Model Accuracy"/>
  <img src="https://img.shields.io/badge/Razas-119-blue?style=for-the-badge" alt="Dog Breeds"/>
  <img src="https://img.shields.io/badge/Inference-<3s-orange?style=for-the-badge" alt="Inference Time"/>
</p>

---

</div>

## 📋 Descripción

**DogBreed AI** es un sistema completo de identificación de razas de perros basado en **Deep Learning**. Utiliza una red neuronal convolucional (CNN) con arquitectura **EfficientNetV2-S** entrenada sobre el dataset Stanford Dogs para clasificar imágenes de perros en **119 razas diferentes** con una precisión del **90.22%**.

El proyecto incluye:
- 🧠 **Modelo CNN** entrenado con Transfer Learning
- ⚡ **Backend API** con FastAPI para inferencia en tiempo real
- 🎨 **Frontend moderno** con React + Tailwind CSS v4
- 📊 **Notebooks** de EDA, preprocessing y entrenamiento
- 📦 **Descripciones completas** de cada raza (origen, temperamento, características)

---

## ✨ Características Principales

### 🎯 Modelo de Deep Learning
- **Arquitectura**: EfficientNetV2-S (Transfer Learning)
- **Precisión**: 90.22% en test, 89.50% en validación
- **Dataset**: Stanford Dogs (20,580 imágenes)
- **Clases**: 119 razas de perros
- **Augmentación**: Albumentations para robustez

### 🚀 Backend API (FastAPI)
- **Predicción en tiempo real**: < 3 segundos
- **Top-K predictions**: Múltiples predicciones con confianza
- **Información detallada**: Origen, tamaño, temperamento, esperanza de vida
- **Documentación**: Swagger UI automática en `/docs`
- **CORS**: Habilitado para integración frontend

### 💎 Frontend Interactivo
- **Upload drag & drop**: Interface intuitiva para subir imágenes
- **Diseño moderno**: Dark theme con gradientes blue-purple
- **Responsive**: Adaptado a móviles, tablets y desktop
- **Animaciones**: Transiciones suaves y efectos visuales
- **Resultados detallados**: Visualización completa de predicciones

---

## 🛠️ Tecnologías Utilizadas

### Backend & ML
| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python | 3.11+ | Lenguaje principal |
| PyTorch | 2.10.0 | Framework de Deep Learning |
| FastAPI | 0.119.0 | API REST |
| Uvicorn | 0.38.0 | Servidor ASGI |
| scikit-learn | 1.8.0 | Métricas y preprocessing |
| OpenCV | 4.12.0.88 | Procesamiento de imágenes |
| Albumentations | 2.0.8 | Data augmentation |
| Pydantic | 2.12.3 | Validación de datos |

### Frontend
| Tecnología | Versión | Uso |
|------------|---------|-----|
| React | 19.2.0 | Framework UI |
| Vite | 8.0.0-beta.13 | Build tool |
| Tailwind CSS | v4 | Estilos y diseño |
| lucide-react | Latest | Iconos profesionales |

### Notebooks & Data Science
- **Jupyter Notebook** 7.3.1
- **Matplotlib** 3.9.4: Visualización
- **Seaborn** 0.13.2: Gráficos estadísticos
- **Pandas** 2.2.3: Manipulación de datos
- **NumPy** 2.2.6: Operaciones numéricas

---

## 📁 Estructura del Proyecto

```
Dog_Breed_Identifier_ML/
│
├── backend/                      # API Backend con FastAPI
│   ├── app/
│   │   ├── main.py              # Punto de entrada FastAPI
│   │   ├── controllers/         # Lógica de endpoints
│   │   ├── routes/              # Definición de rutas
│   │   ├── services/            # Servicios (ML, feedback)
│   │   │   └── ml_service.py    # Servicio de inferencia ML
│   │   ├── schema/              # Esquemas Pydantic
│   │   ├── model/               # Modelos de datos
│   │   ├── data/                # Datos estáticos
│   │   │   └── breed_descriptions.json  # Info de razas
│   │   └── utils/               # Utilidades
│   │
│   ├── ML/                      # Módulos de Machine Learning
│   │   ├── models/
│   │   │   └── training.py      # Pipeline de entrenamiento
│   │   ├── evaluation/          # Métricas y evaluación
│   │   ├── training/            # Trainers especializados
│   │   │   ├── cnn_trainer.py
│   │   │   ├── xgboost_trainer.py
│   │   │   └── data_preprocesor.py
│   │   └── monitoring/          # Data drift detection
│   │
│   ├── test/                    # Tests unitarios
│   ├── dog_breed_model.pth      # Modelo entrenado (191MB)
│   └── label_encoder.pkl        # Codificador de labels
│
├── frontend/                    # Frontend con React
│   ├── src/
│   │   ├── components/          # Componentes React
│   │   │   ├── Navbar.jsx       # Navegación
│   │   │   ├── Hero.jsx         # Sección principal
│   │   │   ├── ProjectDescription.jsx
│   │   │   ├── DogIdentifier.jsx # Upload y predicción
│   │   │   └── Footer.jsx
│   │   ├── App.jsx              # Componente principal
│   │   ├── main.jsx             # Entry point
│   │   └── index.css            # Estilos Tailwind
│   │
│   ├── public/                  # Assets estáticos
│   ├── package.json             # Dependencias npm
│   └── vite.config.js           # Configuración Vite
│
├── ml-pipeline/                 # Pipeline de Data Science
│   ├── notebooks/
│   │   ├── 01_eda.ipynb         # Análisis exploratorio
│   │   └── 02_preprocessing_images.ipynb
│   └── scripts/
│
└── requirements.txt             # Dependencias Python
```

---

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.11 o superior
- Node.js 18+ y npm
- Git

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/Dog_Breed_Identifier_ML.git
cd Dog_Breed_Identifier_ML
```

### 2️⃣ Configurar Backend

#### Instalar Dependencias
```bash
pip install -r requirements.txt
```

#### Iniciar Servidor FastAPI
```bash
cd backend
uvicorn app.main:app --reload
```

El backend estará disponible en: **http://127.0.0.1:8000**
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### 3️⃣ Configurar Frontend

#### Instalar Dependencias
```bash
cd frontend
npm install
```

#### Iniciar Servidor de Desarrollo
```bash
npm run dev
```

El frontend estará disponible en: **http://localhost:5173**

---

## 💡 Uso

### 1. Acceder a la Aplicación Web
Abre tu navegador en `http://localhost:5173`

### 2. Subir una Imagen
- Arrastra y suelta una foto de un perro
- O haz clic en "Seleccionar imagen"
- Formatos: JPG, PNG, WEBP (máx. 10MB)

### 3. Obtener Resultados
El sistema mostrará:
- ✅ **Raza identificada** con porcentaje de confianza
- 🌍 **Origen**: País o región
- 📏 **Tamaño**: Rango de peso
- 🎭 **Temperamento**: Características de personalidad
- 📖 **Descripción**: Información detallada
- ⏳ **Esperanza de vida**: Años promedio
- 🔝 **Top 5 predicciones**: Alternativas con confianza

---

## 📊 Rendimiento del Modelo

### Métricas
| Métrica | Valor |
|---------|-------|
| **Test Accuracy** | 90.22% |
| **Validation Accuracy** | 89.50% |
| **Train Loss** | 0.2847 |
| **Inference Time** | < 3 segundos |
| **Model Size** | 191 MB |

### Dataset
- **Fuente**: Stanford Dogs Dataset
- **Total imágenes**: 20,580
- **Train**: 12,000 imágenes
- **Validation**: 6,000 imágenes  
- **Test**: 2,580 imágenes
- **Clases**: 119 razas de perros

### Arquitectura del Modelo
```
EfficientNetV2-S (Transfer Learning)
├── Pretrained on ImageNet
├── Feature Extractor: Frozen layers
├── Custom Classifier Head:
│   ├── Adaptive Average Pooling
│   ├── Dropout (50%)
│   ├── Linear (features → 512)
│   ├── ReLU + Dropout (30%)
│   └── Linear (512 → 119 classes)
└── Optimizer: Adam (lr=0.0001)
```

---

## 🔌 API Endpoints

### `POST /api/v1/predict/`
Realiza la predicción de raza de perro.

**Request**:
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/predict/?top_k=5" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@dog_image.jpg"
```

**Response**:
```json
{
  "predictions": [
    {
      "breed": "Yorkshire_terrier",
      "confidence": 0.9148,
      "confidence_percentage": "91.48%",
      "name_es": "Yorkshire Terrier",
      "origin": "Inglaterra",
      "size": "Mini (2-3 kg)",
      "temperament": "Confiado, valiente e inteligente",
      "description": "Terrier toy con pelaje sedoso...",
      "life_expectancy": "11-15 años"
    }
  ],
  "processing_time": 2.14,
  "model_version": "EfficientNetV2_S_v1.0"
}
```

### `GET /api/v1/predict/model-info`
Información del modelo.

### `GET /api/v1/predict/health`
Health check del servicio.

### `GET /api/v1/predict/breeds`
Lista de todas las razas soportadas.

---

## 🎨 Capturas de Pantalla

### Hero Section
Sección principal con diseño moderno y llamado a la acción.

### Identificador de Razas
Interface de upload con drag & drop y preview de imagen.

### Resultados Detallados
Visualización completa de la predicción con información de la raza.

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest test/
```

Tests incluidos:
- ✅ `test_api.py`: Endpoints de API
- ✅ `test_models.py`: Modelos de datos
- ✅ `test_services.py`: Servicios ML

---

## 📈 Mejoras Futuras (Roadmap)

### Fase 3: MLOps & Monitoring
- [ ] A/B Testing de arquitecturas (ResNet50, MobileNetV3)
- [ ] Data drift detection con Evidently AI
- [ ] Feedback loop para reentrenamiento
- [ ] Dashboard de métricas con Prometheus + Grafana

### Fase 4: Dockerización
- [ ] Dockerfile para backend (FastAPI + PyTorch)
- [ ] Dockerfile para frontend (Nginx)
- [ ] docker-compose.yml con orquestación completa
- [ ] Multi-stage builds para imágenes optimizadas

### Fase 5: Cloud Deployment
- [ ] Deploy en AWS (ECS/Lambda) o GCP (Cloud Run)
- [ ] CI/CD con GitHub Actions
- [ ] Load balancer y auto-scaling
- [ ] CDN para assets estáticos

### Fase 6: Optimizaciones
- [ ] Model quantization (FP32 → INT8)
- [ ] ONNX Runtime para inference más rápida
- [ ] Redis cache para predicciones frecuentes
- [ ] WebP format optimization

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'feat: add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tuemail@ejemplo.com

---

## 🙏 Agradecimientos

- **Stanford Dogs Dataset**: Por proporcionar el dataset de imágenes
- **PyTorch Team**: Por el excelente framework de Deep Learning
- **FastAPI**: Por la increíble herramienta de desarrollo de APIs
- **React Community**: Por el ecosistema de componentes

---

<div align="center">

### ⭐ Si te gusta este proyecto, dale una estrella en GitHub ⭐

**Hecho con ❤️ para amantes de los perros y la tecnología**

</div>
