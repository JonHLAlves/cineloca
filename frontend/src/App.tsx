import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Clientes from "./pages/Clientes";

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-background font-sans antialiased">
        {/* Aqui podemos colocar uma Navbar depois */}
        <Routes>
          <Route path="/" element={<Navigate to="/clientes" replace />} />
          <Route path="/clientes" element={<Clientes />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;