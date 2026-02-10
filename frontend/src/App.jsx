import Navbar from './components/Navbar';
import Hero from './components/Hero';
import ProjectDescription from './components/ProjectDescription';
import DogIdentifier from './components/DogIdentifier';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <div className="min-h-screen bg-dark-950">
      <Navbar />
      <Hero />
      <ProjectDescription />
      <DogIdentifier />
      <Footer />
    </div>
  );
}

export default App;
