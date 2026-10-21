import type { Categoria } from "../types/categoria";

type Props = {
  categoria: Categoria;
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
};

export function CategoriaCard({ categoria, onEdit, onDelete }: Props) {
  return (
    <div className="bg-white p-5 rounded-lg shadow border border-gray-100 flex flex-col justify-between hover:shadow-md transition-shadow">
      <div>
        <div className="flex justify-between items-start mb-2">
          <h3 className="text-lg font-semibold text-gray-800">{categoria.nombre}</h3>
          <span className="text-xs font-mono bg-gray-100 text-gray-600 px-2 py-0.5 rounded">
            ID: {categoria.id}
          </span>
        </div>
        <p className="text-gray-600 text-sm mb-4">{categoria.descripcion}</p>
      </div>
      
      <div className="flex justify-end gap-2 border-t pt-3">
        <button
          onClick={() => onEdit(categoria)}
          className="px-3 py-1.5 text-xs font-medium bg-amber-50 text-amber-700 rounded hover:bg-amber-100 transition-colors"
        >
          Editar
        </button>
        <button
          onClick={() => onDelete(categoria.id)}
          className="px-3 py-1.5 text-xs font-medium bg-rose-50 text-rose-700 rounded hover:bg-rose-100 transition-colors"
        >
          Eliminar
        </button>
      </div>
    </div>
  );
}