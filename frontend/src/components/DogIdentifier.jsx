import { useState, useRef } from 'react';
import { Camera, Upload, CheckCircle, AlertCircle, Loader2, X, Info, Brain } from 'lucide-react';

const DogIdentifier = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [predictions, setPredictions] = useState(null);
  const [error, setError] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

  const handleFileSelect = (file) => {
    if (!file) return;

    // Validate file type
    const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/jpg'];
    if (!validTypes.includes(file.type)) {
      setError('Formato no válido. Use JPG, PNG o WEBP');
      return;
    }

    // Validate file size (10MB max)
    if (file.size > 10 * 1024 * 1024) {
      setError('La imagen debe ser menor a 10MB');
      return;
    }

    setSelectedImage(file);
    setError(null);
    setPredictions(null);

    // Create preview
    const reader = new FileReader();
    reader.onloadend = () => {
      setImagePreview(reader.result);
    };
    reader.readAsDataURL(file);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const file = e.dataTransfer.files[0];
    handleFileSelect(file);
  };

  const handleFileInput = (e) => {
    const file = e.target.files[0];
    handleFileSelect(file);
  };

  const handlePredict = async () => {
    if (!selectedImage) return;

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('file', selectedImage);

      const response = await fetch('http://127.0.0.1:8000/api/v1/predict/?top_k=5', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Error en la predicción. Verifica que el backend esté funcionando.');
      }

      const data = await response.json();
      setPredictions(data.predictions);
    } catch (err) {
      setError(err.message || 'Error al procesar la imagen');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedImage(null);
    setImagePreview(null);
    setPredictions(null);
    setError(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <section id="dog-identifier" className="py-12 px-6">
      <div className="max-w-5xl mx-auto">
        {/* Title */}
        <div className="text-center mb-8">
          <h2 className="text-3xl md:text-4xl font-bold gradient-text mb-3">
            🐕 Identificador de Razas
          </h2>
          <p className="text-base text-gray-400">
            Sube una foto de tu perro y descubre su raza al instante
          </p>
        </div>

        {/* Upload Area */}
        {!imagePreview && (
          <div className="card-glass max-w-2xl mx-auto mb-8">
            <div
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              className={`border-2 border-dashed rounded-2xl p-8 text-center transition-all ${
                isDragging 
                  ? 'border-blue-500 bg-blue-500/10' 
                  : 'border-dark-600 hover:border-dark-500'
              }`}
            >
              {/* Upload Icon */}
              <div className="relative mb-6 inline-block">
                <div className="bg-linear-to-br from-blue-600 to-purple-600 w-20 h-20 rounded-3xl 
                              flex items-center justify-center mx-auto animate-pulse-slow">
                  <Camera className="w-10 h-10 text-white" />
                </div>
                <div className="absolute -top-2 -right-2 bg-linear-to-r from-purple-600 to-pink-600 
                              w-8 h-8 rounded-full flex items-center justify-center animate-float">
                  <Upload className="w-4 h-4 text-white" />
                </div>
              </div>

              <h3 className="text-xl font-bold gradient-text mb-2">
                📷 Sube una foto de tu perro
              </h3>
              <p className="text-gray-400 mb-5 text-base">
                Arrastra y suelta o haz clic para seleccionar
              </p>
              
              <p className="text-xs text-gray-500 mb-5">
                <span className="font-semibold text-gray-400">Formatos aceptados:</span> JPG, PNG, WEBP (máx. 10MB)
              </p>

              <input
                ref={fileInputRef}
                type="file"
                accept="image/jpeg,image/png,image/webp,image/jpg"
                onChange={handleFileInput}
                className="hidden"
              />
              
              <button
                onClick={() => fileInputRef.current?.click()}
                className="bg-linear-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 
                         text-white font-semibold py-2.5 px-6 rounded-xl transition-all duration-300 
                         shadow-lg hover:shadow-xl hover:scale-105 inline-flex items-center gap-2"
              >
                <Upload className="w-5 h-5" />
                Seleccionar imagen
              </button>
            </div>

            {/* Error Message */}
            {error && (
              <div className="mt-6 bg-red-900/20 border border-red-500/50 rounded-xl p-4 flex items-center gap-3">
                <AlertCircle className="w-6 h-6 text-red-400 shrink-0" />
                <p className="text-red-300">{error}</p>
              </div>
            )}

            {/* Stats */}
            <div className="grid grid-cols-3 gap-4 mt-8">
              <div className="text-center">
                <div className="text-2xl font-bold gradient-text mb-1">98%</div>
                <div className="text-gray-400 text-sm">Precisión</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold gradient-text mb-1">120+</div>
                <div className="text-gray-400 text-sm">Razas</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold gradient-text mb-1">⚡</div>
                <div className="text-gray-400 text-sm">Instantáneo</div>
              </div>
            </div>
          </div>
        )}

        {/* Image Preview & Predict */}
        {imagePreview && !predictions && (
          <div className="card-glass max-w-2xl mx-auto">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-bold gradient-text">Imagen seleccionada</h3>
              <button
                onClick={handleReset}
                className="text-gray-400 hover:text-white transition-colors p-2 hover:bg-dark-700 rounded-lg"
              >
                <X className="w-6 h-6" />
              </button>
            </div>

            <div className="relative rounded-2xl overflow-hidden mb-5 bg-dark-900">
              <img
                src={imagePreview}
                alt="Preview"
                className="w-full max-h-80 object-contain"
              />
            </div>

            <button
              onClick={handlePredict}
              disabled={loading}
              className="btn-primary w-full text-base flex items-center justify-center gap-2"
            >
              {loading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Analizando imagen...
                </>
              ) : (
                <>
                  <Brain className="w-5 h-5" />
                  Identificar raza
                </>
              )}
            </button>

            {error && (
              <div className="mt-6 bg-red-900/20 border border-red-500/50 rounded-xl p-4 flex items-center gap-3">
                <AlertCircle className="w-6 h-6 text-red-400 shrink-0" />
                <p className="text-red-300">{error}</p>
              </div>
            )}
          </div>
        )}

        {/* Results */}
        {predictions && predictions.length > 0 && (
          <div className="max-w-4xl mx-auto space-y-6">
            {/* Top Prediction */}
            <div className="card-glass border-2 border-blue-500/30">
              <div className="flex items-start gap-3 mb-5">
                <div className="bg-linear-to-br from-blue-600 to-purple-600 w-14 h-14 rounded-2xl 
                              flex items-center justify-center shrink-0">
                  <CheckCircle className="w-7 h-7 text-white" />
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-2">
                    <h3 className="text-2xl font-bold gradient-text">
                      {predictions[0].name_es || predictions[0].breed}
                    </h3>
                    <span className="bg-green-500/20 text-green-300 px-3 py-1 rounded-full text-xs font-semibold">
                      {predictions[0].confidence_percentage}% confianza
                    </span>
                  </div>
                  {predictions[0].description && (
                    <p className="text-gray-300 text-base leading-relaxed mb-3">
                      {predictions[0].description}
                    </p>
                  )}
                </div>
              </div>

              {/* Breed Details */}
              {predictions[0].origin && (
                <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-3 pt-5 border-t border-dark-600">
                  {predictions[0].origin && (
                    <div className="bg-dark-900/50 rounded-xl p-3">
                      <div className="text-blue-400 text-xs font-semibold mb-1">🌍 Origen</div>
                      <div className="text-gray-200 text-sm">{predictions[0].origin}</div>
                    </div>
                  )}
                  {predictions[0].size && (
                    <div className="bg-dark-900/50 rounded-xl p-3">
                      <div className="text-purple-400 text-xs font-semibold mb-1">📏 Tamaño</div>
                      <div className="text-gray-200 text-sm">{predictions[0].size}</div>
                    </div>
                  )}
                  {predictions[0].temperament && (
                    <div className="bg-dark-900/50 rounded-xl p-3">
                      <div className="text-pink-400 text-xs font-semibold mb-1">🎭 Temperamento</div>
                      <div className="text-gray-200 text-sm">{predictions[0].temperament}</div>
                    </div>
                  )}
                  {predictions[0].life_expectancy && (
                    <div className="bg-dark-900/50 rounded-xl p-3">
                      <div className="text-green-400 text-xs font-semibold mb-1">⏳ Esperanza de vida</div>
                      <div className="text-gray-200 text-sm">{predictions[0].life_expectancy}</div>
                    </div>
                  )}
                </div>
              )}

              {/* Image Preview in Results */}
              <div className="mt-5 rounded-xl overflow-hidden bg-dark-900">
                <img
                  src={imagePreview}
                  alt="Analyzed dog"
                  className="w-full max-h-52 object-contain"
                />
              </div>
            </div>

            {/* Other Predictions */}
            {predictions.length > 1 && (
              <div>
                <div className="flex items-center gap-2 mb-5">
                  <Info className="w-5 h-5 text-blue-400" />
                  <h4 className="text-lg font-bold text-gray-300">
                    Otras posibles razas:
                  </h4>
                </div>
                <div className="grid md:grid-cols-2 gap-3">
                  {predictions.slice(1).map((pred, idx) => (
                    <div key={idx} className="card-glass flex items-center justify-between">
                      <div>
                        <div className="font-bold text-base text-gray-200 mb-1">
                          {pred.name_es || pred.breed}
                        </div>
                        {pred.origin && (
                          <div className="text-xs text-gray-400">🌍 {pred.origin}</div>
                        )}
                      </div>
                      <div className="text-xl font-bold gradient-text">
                        {pred.confidence_percentage}%
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Reset Button */}
            <div className="text-center">
              <button
                onClick={handleReset}
                className="bg-linear-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 
                         text-white font-semibold py-2.5 px-6 rounded-xl transition-all duration-300 
                         shadow-lg hover:shadow-xl hover:scale-105 inline-flex items-center gap-2"
              >
                <Upload className="w-4 h-4" />
                Analizar otra imagen
              </button>
            </div>
          </div>
        )}
      </div>
    </section>
  );
};

export default DogIdentifier;
