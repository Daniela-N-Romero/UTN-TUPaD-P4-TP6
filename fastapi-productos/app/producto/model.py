from typing import Optional, List
from sqlmodel import SQLModel, Field, Column, JSON

# Modelo de Base / Tabla
class Producto(SQLModel, table=True):
    __tablename__ = "producto"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: List[str] = Field(default=[], sa_column=Column(JSON)) ## SOLUCIÓN PARA SQLITE: Guardamos la lista de Python como texto JSON en SQLite
    disponible: bool

class ProductoCategoria(SQLModel, table=True):
    __tablename__ = "producto_categoria"

    # Definimos las claves foráneas que vinculan ambas tablas
    producto_id: Optional[int] = Field(
        default=None, foreign_key="producto.id", primary_key=True
    )
    categoria_id: Optional[int] = Field(
        default=None, foreign_key="categoria.id", primary_key=True
    )
