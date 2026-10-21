from typing import Optional
from sqlmodel import SQLModel

# Esquema base con campos comunes
class CategoriaBase(SQLModel):
    nombre: str
    descripcion: str

# Esquema para la creación (POST)
class CategoriaCreate(CategoriaBase):
    pass

# Esquema para la lectura/respuesta (GET) -> Incluye el ID asignado por la DB
class CategoriaRead(CategoriaBase):
    id: int

# Esquema para la actualización opcional (PUT / PATCH)
class CategoriaUpdate(SQLModel):
    nombre: str | None = None
    descripcion: str | None = None