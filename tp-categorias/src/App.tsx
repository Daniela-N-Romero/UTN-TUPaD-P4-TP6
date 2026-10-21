import { useState } from "react";
import type { Categoria } from "./types/categoria";
import { Navbar } from "./components/Navbar";
import { CategoriaList } from "./components/CategoriaList";
import { CategoriaModal } from "./components/CategoriaModal";
import { useCategorias } from "./hooks/useCategorias";

export function App() {
  const { categorias, saveCategoria, deleteCategoria } = useCategorias();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [categoriaSeleccionada, setCategoriaSeleccionada] = useState<Categoria | null>(null);

  const handleSave = async (datos: { nombre: string; descripcion: string }) => {
    await saveCategoria(datos, categoriaSeleccionada?.id);
  };

  const abrirModalCrear = () => {
    setCategoriaSeleccionada(null);
    setIsModalOpen(true);
  };

  const abrirModalEditar = (categoria: Categoria) => {
    setCategoriaSeleccionada(categoria);
    setIsModalOpen(true);
  };

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <Navbar />
      
      <main className="container mx-auto px-6 py-4">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold tracking-tight">Listado de Categorías</h2>
          <button
            onClick={abrirModalCrear}
            className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-4 py-2 rounded-md shadow transition-colors text-sm"
          >
            + Añadir Categoría
          </button>
        </div>

        <CategoriaList
          categorias={categorias}
          onEdit={abrirModalEditar}
          onDelete={deleteCategoria}
        />
      </main>

      <CategoriaModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleSave}
        categoriaActual={categoriaSeleccionada}
      />
    </div>
  );
}

export default App;