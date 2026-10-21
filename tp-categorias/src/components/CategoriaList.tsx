import type { Categoria } from "../types/categoria";
import { CategoriaCard } from "./CategoriaCard";

type Props = {
  categorias: Categoria[];
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
};

export function CategoriaList({ categorias, onEdit, onDelete }: Props) {
  if (categorias.length === 0) {
    return (
      <div className="text-center py-12 bg-white rounded-lg border border-dashed border-gray-300">
        <p className="text-gray-500">No hay categorías registradas todavía.</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {categorias.map((cat) => (
        <CategoriaCard key={cat.id} categoria={cat} onEdit={onEdit} onDelete={onDelete} />
      ))}
    </div>
  );
}