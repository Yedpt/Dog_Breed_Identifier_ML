import { Github, Heart, Code, Mail } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="border-t border-dark-700 py-8 px-6 mt-12">
      <div className="max-w-6xl mx-auto">
        {/* Main Content */}
        <div className="grid md:grid-cols-3 gap-6 mb-6">
          {/* Brand */}
          <div>
            <h3 className="text-xl font-bold gradient-text mb-2 flex items-center gap-2">
              🐕 DogBreed AI
            </h3>
            <p className="text-gray-400 leading-relaxed text-sm">
              Identificación de razas de perros mediante redes neuronales convolucionales 
              y deep learning avanzado.
            </p>
          </div>

          {/* Tech Stack */}
          <div>
            <h4 className="text-base font-semibold text-gray-300 mb-2 flex items-center gap-2">
              <Code className="w-4 h-4 text-blue-400" />
              Tecnologías
            </h4>
            <ul className="space-y-1 text-gray-400 text-sm">
              <li>• EfficientNetV2-S (PyTorch)</li>
              <li>• FastAPI + React</li>
              <li>• Stanford Dogs Dataset</li>
              <li>• Tailwind CSS</li>
            </ul>
          </div>

          {/* Links */}
          <div>
            <h4 className="text-base font-semibold text-gray-300 mb-2 flex items-center gap-2">
              <Github className="w-4 h-4 text-purple-400" />
              Enlaces
            </h4>
            <ul className="space-y-1">
              <li>
                <a href="https://github.com" 
                   className="text-gray-400 hover:text-blue-400 transition-colors inline-flex items-center gap-2 text-sm">
                  <Github className="w-3 h-3" />
                  GitHub Repository
                </a>
              </li>
              <li>
                <a href="http://127.0.0.1:8000/docs" 
                   target="_blank"
                   rel="noopener noreferrer"
                   className="text-gray-400 hover:text-purple-400 transition-colors inline-flex items-center gap-2 text-sm">
                  <Code className="w-3 h-3" />
                  API Documentation
                </a>
              </li>
              <li>
                <a href="mailto:contact@dogbreed.ai" 
                   className="text-gray-400 hover:text-pink-400 transition-colors inline-flex items-center gap-2 text-sm">
                  <Mail className="w-3 h-3" />
                  Contacto
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-dark-700 pt-6">
          <div className="flex flex-col md:flex-row justify-between items-center gap-3">
            {/* Copyright */}
            <p className="text-gray-500 text-sm">
              © {currentYear} DogBreed AI. Todos los derechos reservados.
            </p>

            {/* Made with love */}
            <p className="text-gray-500 text-xs flex items-center gap-2">
              Desarrollado con 
              <Heart className="w-3 h-3 text-red-500 animate-pulse" />
              para amantes de los perros y la tecnología
            </p>
          </div>
        </div>

        {/* Credits */}
        <div className="text-center mt-4 pt-4 border-t border-dark-700">
          <p className="text-xs text-gray-600">
            Dataset: Stanford Dogs Dataset | Arquitectura: EfficientNetV2-S | 
            Framework: PyTorch 2.10.0 | API: FastAPI 0.119.0 | Frontend: React 19 + Tailwind CSS
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
