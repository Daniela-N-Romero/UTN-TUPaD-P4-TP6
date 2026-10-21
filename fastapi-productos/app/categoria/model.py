from sqlmodel import SQLModel, Field
from typing import Optional

# Modelo de Base / Tabla
class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str