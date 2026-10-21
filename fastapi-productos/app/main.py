from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import create_db_and_tables
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=['http://localhost:5173'],
allow_methods=['*'],
allow_headers=['*'],
)

# Evento que se ejecuta al iniciar la app para crear las tablas en SQLite
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Incluimos las rutas de categorías
app.include_router(categoria_router)
app.include_router(producto_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Backend del Trabajo Práctico - FastAPI & React"}