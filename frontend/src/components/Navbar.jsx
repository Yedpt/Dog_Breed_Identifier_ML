import { Dog, Sparkles } from 'lucide-react';

const Navbar = () => {
  const scrollToIdentifier = () => {
    document.getElementById('dog-identifier')?.scrollIntoView({ 
      behavior: 'smooth' 
    });
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-dark-950/80 backdrop-blur-xl border-b border-dark-800">
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <div className="flex items-center gap-3 group cursor-pointer">
            <div className="bg-linear-to-br from-blue-600 to-purple-600 w-10 h-10 rounded-xl 
                          flex items-center justify-center group-hover:scale-110 transition-transform">
              <Dog className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold gradient-text">DogBreed AI</h1>
              <p className="text-xs text-gray-500">Powered by Neural Networks</p>
            </div>
          </div>

          {/* CTA Button */}
          <button
            onClick={scrollToIdentifier}
            className="bg-linear-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 
                     text-white font-semibold px-6 py-2.5 rounded-xl transition-all duration-300 
                     shadow-lg hover:shadow-xl hover:scale-105 flex items-center gap-2 text-sm"
          >
            <Sparkles className="w-4 h-4" />
            Pruébalo ahora
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
