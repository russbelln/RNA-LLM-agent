import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import AboutUs from './pages/AboutUs';
import HomeButton from './components/HomeButton'; // Botón reutilizable
import './App.css'; // Asegúrate de importar el CSS aquí

function App() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Router>
      <div className={`app-container ${collapsed ? 'sidebar-collapsed' : ''}`}>
        {/* Sidebar */}
        <Sidebar collapsed={collapsed} onToggle={() => setCollapsed(!collapsed)} />

        {/* Contenedor principal */}
        <div className="main-content">
          {/* Botón Home */}
          <div className="home-button-container">
            <HomeButton/>
          </div>

          {/* Rutas */}
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/aboutus" element={<AboutUs />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
