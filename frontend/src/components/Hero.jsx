import { Brain, Zap, Target, ArrowRight } from 'lucide-react';

const Hero = () => {
  const scrollToIdentifier = () => {
    document.getElementById('dog-identifier')?.scrollIntoView({ 
      behavior: 'smooth' 
    });
  };

  return (
    <section className="min-h-screen flex items-center justify-center px-6 py-16 pt-24">
      <div className="max-w-6xl w-full">
        {/* Badge */}
        <div className="flex justify-center mb-6 animate-float">
          <div className="inline-flex items-center gap-2 bg-linear-to-r from-blue-600/20 to-purple-600/20 
                          border border-blue-500/30 px-5 py-2 rounded-full backdrop-blur-sm">
            <span className="text-xl">🎓</span>
            <span className="text-blue-300 font-semibold text-sm">Inteligencia Artificial Avanzada</span>
          </div>
        </div>

        {/* Main Title */}
        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-center mb-6 leading-tight">
          <span className="gradient-text">
            Identifica la Raza de tu Perro con IA
          </span>
        </h1>

        {/* Subtitle */}
        <p className="text-base md:text-lg text-gray-400 text-center max-w-3xl mx-auto mb-8 leading-relaxed">
          Descubre la raza de tu mejor amigo en segundos gracias a nuestro modelo de 
          redes neuronales entrenado con miles de imágenes y una precisión del 98%
        </p>

        {/* CTA Button */}
        <div className="flex justify-center mb-12">
          <button 
            onClick={scrollToIdentifier}
            className="btn-primary inline-flex items-center gap-2 text-base group"
          >
            Probar ahora
            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </button>
        </div>

        {/* Feature Cards */}
        <div className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
          {/* Card 1: Precisión */}
          <div className="card-glass animate-float">
            <div className="bg-linear-to-br from-blue-600 to-purple-600 w-14 h-14 rounded-2xl 
                          flex items-center justify-center mb-5 mx-auto">
              <Brain className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-xl font-bold text-center mb-3 gradient-text">
              98% Precisión
            </h3>
            <p className="text-gray-400 text-center leading-relaxed text-sm">
              Modelo entrenado con deep learning para resultados exactos basado en 
              arquitectura EfficientNetV2-S
            </p>
          </div>

          {/* Card 2: Velocidad */}
          <div className="card-glass animate-float animation-delay-200">
            <div className="bg-linear-to-br from-purple-600 to-pink-600 w-14 h-14 rounded-2xl 
                          flex items-center justify-center mb-5 mx-auto">
              <Zap className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-xl font-bold text-center mb-3 gradient-text">
              ⚡ Instantáneo
            </h3>
            <p className="text-gray-400 text-center leading-relaxed text-sm">
              Resultados en menos de 3 segundos con procesamiento en tiempo real 
              gracias a optimizaciones avanzadas
            </p>
          </div>

          {/* Card 3: Cobertura */}
          <div className="card-glass animate-float animation-delay-400">
            <div className="bg-linear-to-br from-pink-600 to-blue-600 w-14 h-14 rounded-2xl 
                          flex items-center justify-center mb-5 mx-auto">
              <Target className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-xl font-bold text-center mb-3 gradient-text">
              120+ Razas 🐕
            </h3>
            <p className="text-gray-400 text-center leading-relaxed text-sm">
              Base de datos completa con las razas más populares del mundo 
              desde el Stanford Dogs Dataset
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
