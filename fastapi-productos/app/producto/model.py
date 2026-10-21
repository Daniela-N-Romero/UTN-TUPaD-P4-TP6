from typing import Optional

from sqlmodel import JSON, Column, Field, ForeignKey, Integer, Relationship, SQLModel

from app.categoria.model import Categoria


# 1. La Tabla de Enlace (Debe ir ANTES de la clase Producto)
class ProductoCategoria(SQLModel, table=True):
    __tablename__ = "producto_categoria"

    # Definimos las claves foráneas que vinculan las tablas
    # sa_column permite configurar la columna directamente con SQLAlchemy (bajo nivel), indicando restricciones nativas como llaves foráneas en cascada y claves compuestas.
    
    producto_id: int = Field(
        sa_column=Column(           
            Integer, 
            ForeignKey("producto.id", ondelete="CASCADE"),
            primary_key=True, 
            nullable=False) 

    )
    categoria_id: int | None = Field(
        sa_column=Column(
            Integer, 
            ForeignKey("categoria.id", ondelete="CASCADE"), 
            primary_key=True, 
            nullable=False
        )
    )
    
    producto: Optional["Producto"] = Relationship()
    categoria: Optional["Categoria"] = Relationship()
    
    
# Modelo de Base / Tabla
class Producto(SQLModel, table=True):
    __tablename__ = "producto"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str 
    descripcion: str
    precio_base: str
    imagen_url: list[str] = Field(default=[], sa_column=Column(JSON)) ## SOLUCIÓN PARA SQLITE: Guardamos la lista de Python como texto JSON en SQLite
    disponible: bool

