import { useState, useEffect } from "react";
import type { Categoria } from "../types/categoria";

const API_URL = `${import.meta.env.VITE_API_URL}/categorias`;

export function useCategorias() {
  const [categorias, setCategorias] = useState<Categoria[]>([]);

  // Cargar categorías (GET)
  const fetchCategorias = async () => {
    try {
      const response = await fetch(API_URL);
      if (response.ok) {
        const data = await response.json();
        setCategorias(data);
      }
    } catch (error) {
      console.error("Error al conectar con la API:", error);
    }
  };

  useEffect(() => {
    fetchCategorias();
  }, []);

  // Crear o Actualizar categoría (POST / PUT)
  const saveCategoria = async (datos: { nombre: string; descripcion: string }, idSeleccionado?: number) => {
    try {
      if (idSeleccionado) {
        const response = await fetch(`${API_URL}/${idSeleccionado}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(datos),
        });
        if (response.ok) fetchCategorias();
      } else {
        const response = await fetch(API_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(datos),
        });
        if (response.ok) fetchCategorias();
      }
    } catch (error) {
      console.error("Error al guardar la categoría:", error);
    }
  };

  // Eliminar categoría (DELETE)
  const deleteCategoria = async (id: number) => {
    if (!confirm("¿Estás seguro de que querés eliminar esta categoría?")) return;
    try {
      const response = await fetch(`${API_URL}/${id}`, {
        method: "DELETE",
      });
      if (response.ok) {
        setCategorias(categorias.filter((cat) => cat.id !== id));
      }
    } catch (error) {
      console.error("Error al eliminar:", error);
    }
  };

  return {
    categorias,
    saveCategoria,
    deleteCategoria,
  };
}