import { FileText, Upload, Brain, Target, Dog, Heart, Laptop } from 'lucide-react';

const ProjectDescription = () => {
  return (
    <section className="py-12 px-6">
      <div className="max-w-6xl mx-auto">
        {/* Section Title */}
        <div className="flex items-center justify-center gap-3 mb-8">
          <FileText className="w-8 h-8 text-blue-400" />
          <h2 className="text-3xl md:text-4xl font-bold gradient-text">
            Descripción del Proyecto
          </h2>
        </div>

        {/* Main Description */}
        <div className="card-glass max-w-4xl mx-auto mb-10">
          <p className="text-base text-gray-300 leading-relaxed text-center">
            Este proyecto es un <span className="gradient-text font-semibold">identificador de razas de perro</span> basado 
            en <span className="text-blue-400 font-semibold">redes neuronales convolucionales</span> (CNN). 
            Utiliza un modelo de deep learning entrenado con el dataset Stanford Dogs para clasificar 
            imágenes de perros en más de 120 razas diferentes. El sistema proporciona no solo la 
            predicción, sino también información detallada sobre el origen, temperamento y características 
            de cada raza identificada.
          </p>
        </div>

        {/* How to Use Section */}
        <div className="mb-10">
          <div className="flex items-center justify-center gap-3 mb-8">
            <span className="text-3xl">🎨</span>
            <h3 className="text-2xl md:text-3xl font-bold gradient-text">
              ¿Cómo Utilizar el Identificador?
            </h3>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {/* Step 1 */}
            <div className="card-glass text-center hover:scale-105 transition-transform">
              <div className="bg-linear-to-br from-blue-600 to-purple-600 w-16 h-16 rounded-2xl 
                            flex items-center justify-center mb-5 mx-auto">
                <Upload className="w-8 h-8 text-white" />
              </div>
              <h4 className="text-lg font-bold mb-3 gradient-text">
                📤 Sube una Foto
              </h4>
              <p className="text-gray-400 leading-relaxed text-sm">
                Selecciona una imagen clara de tu perro. Asegúrate de que el perro sea el 
                elemento principal de la foto para obtener mejores resultados. Formatos: JPG, PNG, WEBP.
              </p>
            </div>

            {/* Step 2 */}
            <div className="card-glass text-center hover:scale-105 transition-transform">
              <div className="bg-linear-to-br from-purple-600 to-pink-600 w-16 h-16 rounded-2xl 
                            flex items-center justify-center mb-5 mx-auto">
                <Brain className="w-8 h-8 text-white" />
              </div>
              <h4 className="text-lg font-bold mb-3 gradient-text">
                🧠 Procesamiento con IA
              </h4>
              <p className="text-gray-400 leading-relaxed text-sm">
                Nuestro modelo EfficientNetV2-S analiza la imagen mediante capas convolucionales, 
                extrayendo características visuales únicas para identificar la raza con precisión.
              </p>
            </div>

            {/* Step 3 */}
            <div className="card-glass text-center hover:scale-105 transition-transform">
              <div className="bg-linear-to-br from-pink-600 to-blue-600 w-16 h-16 rounded-2xl 
                            flex items-center justify-center mb-5 mx-auto">
                <Target className="w-8 h-8 text-white" />
              </div>
              <h4 className="text-lg font-bold mb-3 gradient-text">
                🎯 Obtén el Resultado
              </h4>
              <p className="text-gray-400 leading-relaxed text-sm">
                Recibe la predicción con el porcentaje de confianza, además de información completa: 
                origen, tamaño, temperamento, descripción y esperanza de vida de la raza.
              </p>
            </div>
          </div>
        </div>

        {/* Ideal For Section */}
        <div>
          <div className="flex items-center justify-center gap-3 mb-8">
            <span className="text-3xl">💡</span>
            <h3 className="text-2xl md:text-3xl font-bold gradient-text">
              Ideal Para:
            </h3>
          </div>

          <div className="grid md:grid-cols-3 gap-5 max-w-4xl mx-auto">
            {/* Audience 1 */}
            <div className="card-glass flex items-center gap-3 hover:scale-105 transition-transform">
              <div className="bg-linear-to-br from-blue-600 to-purple-600 w-12 h-12 rounded-xl 
                            flex items-center justify-center shrink-0">
                <Dog className="w-6 h-6 text-white" />
              </div>
              <p className="text-gray-300 text-sm leading-relaxed">
                <span className="font-semibold text-blue-300">🐶 Dueños curiosos</span> de perros mestizos o de raza
              </p>
            </div>

            {/* Audience 2 */}
            <div className="card-glass flex items-center gap-3 hover:scale-105 transition-transform">
              <div className="bg-linear-to-br from-purple-600 to-pink-600 w-12 h-12 rounded-xl 
                            flex items-center justify-center shrink-0">
                <Heart className="w-6 h-6 text-white" />
              </div>
              <p className="text-gray-300 text-sm leading-relaxed">
                <span className="font-semibold text-purple-300">❤️ Adoptantes</span> que quieran conocer el origen de su perro
              </p>
            </div>

            {/* Audience 3 */}
            <div className="card-glass flex items-center gap-3 hover:scale-105 transition-transform">
              <div className="bg-linear-to-br from-pink-600 to-blue-600 w-12 h-12 rounded-xl 
                            flex items-center justify-center shrink-0">
                <Laptop className="w-6 h-6 text-white" />
              </div>
              <p className="text-gray-300 text-sm leading-relaxed">
                <span className="font-semibold text-pink-300">💻 Amantes de los perros</span> y entusiastas de la tecnología
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProjectDescription;
