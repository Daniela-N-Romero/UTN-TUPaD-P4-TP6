from typing import Optional
from sqlmodel import SQLModel

# Esquema base con campos comunes
class ProductoBase(SQLModel):
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list = []
    disponible: bool

# Esquema para la creación (POST)
class ProductoCreate(ProductoBase):
    pass

# Esquema para la lectura/respuesta (GET) -> Incluye el ID asignado por la DB
class ProductoRead(ProductoBase):
    id: int

# Esquema para la actualización opcional (PUT / PATCH)
class ProductoUpdate(SQLModel):
    nombre: str | None = None
    descripcion: str | None = None
    precio_base: str | None = None
    imagen_url: list | None = None
    disponible: bool | None = None