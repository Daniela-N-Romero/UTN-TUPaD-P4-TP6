from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.core.database import get_session
from app.producto.model import Producto, ProductoCategoria
from app.producto.schema import ProductoCreate, ProductoRead, ProductoUpdate

router = APIRouter(prefix="/productos", tags=["Productos"])

# 1. LISTAR PRODUCTOS (GET)
@router.get("/", response_model=List[ProductoRead])
def obtener_productos(session: Session = Depends(get_session)):
    productos = session.exec(select(Producto)).all()
    return productos

# 2. CREAR PRODUCTO (POST)
@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def crear_producto(producto_in: ProductoCreate, session: Session = Depends(get_session)):
    db_producto = Producto.model_validate(producto_in)
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto

# 3. OBTENER UN PRODUCTO POR ID (GET)
@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int, session: Session = Depends(get_session)):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# 4. ACTUALIZAR PRODUCTO (PUT)
@router.put("/{producto_id}", response_model=ProductoRead)
def actualizar_producto(
    producto_id: int, 
    producto_in: ProductoUpdate, 
    session: Session = Depends(get_session)
):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto_data = producto_in.model_dump(exclude_unset=True)
    for key, value in producto_data.items():
        setattr(db_producto, key, value)
        
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto

# 5. ELIMINAR PRODUCTO (DELETE)
@router.delete("/{producto_id}", status_code=status.HTTP_200_OK)
def eliminar_producto(producto_id: int, session: Session = Depends(get_session)):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    session.delete(db_producto)
    session.commit()
    return {"message": "Producto eliminado exitosamente", "id": producto_id}

# ==========================================
# ENDPOINTS PARA PRODUCTO_CATEGORIA
# ==========================================

# 6. ASOCIAR PRODUCTO A CATEGORÍA (POST)
@router.post("/{producto_id}/categorias/{categoria_id}", status_code=status.HTTP_201_CREATED)
def asociar_producto_categoria(
    producto_id: int, 
    categoria_id: int, 
    session: Session = Depends(get_session)
):
    # Verificamos que exista la relación previa
    existente = session.get(ProductoCategoria, (producto_id, categoria_id))
    if existente:
        raise HTTPException(status_code=400, detail="La relación ya existe")

    relacion = ProductoCategoria(producto_id=producto_id, categoria_id=categoria_id)
    session.add(relacion)
    session.commit()
    return {"message": "Producto asociado a categoría exitosamente", "producto_id": producto_id, "categoria_id": categoria_id}

# 7. DESASOCIAR PRODUCTO DE CATEGORÍA (DELETE)
@router.delete("/{producto_id}/categorias/{categoria_id}", status_code=status.HTTP_200_OK)
def desasociar_producto_categoria(
    producto_id: int, 
    categoria_id: int, 
    session: Session = Depends(get_session)
):
    relacion = session.get(ProductoCategoria, (producto_id, categoria_id))
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    
    session.delete(relacion)
    session.commit()
    return {"message": "Relación eliminada exitosamente"}