from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.core.database import get_session
from app.producto.model import Producto, ProductoCategoria
from app.producto.schema import ProductoCreate, ProductoRead, ProductoUpdate

router = APIRouter(prefix="/productos", tags=["Productos"])

# 1. LISTAR TODOS LOS PRODUCTOS (GET)--------------------------------------------------------
@router.get("/", response_model=list[ProductoRead])
def obtener_productos(session: Session = Depends(get_session)):
    productos = session.exec(select(Producto)).all()
    return productos



# 2. CREAR PRODUCTO (POST)----------------------------------------------------------------
@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def crear_producto(producto_input: ProductoCreate, session: Session = Depends(get_session)):
        # Convertimos el esquema de entrada al modelo de la base de datos con model_validate
    db_producto = Producto.model_validate(producto_input)
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto



# 3. TRAER UN PRODUCTO POR ID (GET)-------------------------------------------------------
@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int, session: Session = Depends(get_session)):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto



# 4. ACTUALIZAR PRODUCTO (PUT)-------------------------------------------------------------
@router.put("/{producto_id}", response_model=ProductoRead)
def actualizar_producto(
    producto_id: int, 
    producto_in: ProductoUpdate, 
    session: Session = Depends(get_session)
):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # excluyendo los que vienen en None
    producto_data = producto_in.model_dump(exclude_unset=True)
    for key, value in producto_data.items():
        setattr(db_producto, key, value)
        
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto



# 5. ELIMINAR PRODUCTO (DELETE)---------------------------------------------------------
@router.delete("/{producto_id}", status_code=status.HTTP_200_OK)
def eliminar_producto(producto_id: int, session: Session = Depends(get_session)):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    session.delete(db_producto)
    session.commit()
    return {"message": "Producto eliminado exitosamente", "id": producto_id}






# ==========================================
# ENDPOINTS PARA PRODUCTO_CATEGORIA (TABLA INTERMEDIA)
# ==========================================



# ASOCIAR PRODUCTO A CATEGORÍA (POST)
@router.post("/{producto_id}/categorias/{categoria_id}", status_code=status.HTTP_201_CREATED)
def asociar_producto_categoria(
    producto_id: int, 
    categoria_id: int, 
    session: Session = Depends(get_session)
):
    # Verificamos si existe la relación antes
    existente = session.get(ProductoCategoria, (producto_id, categoria_id))
    if existente:
        raise HTTPException(status_code=400, detail="La relación ya existe")

    relacion = ProductoCategoria(producto_id=producto_id, categoria_id=categoria_id)
    session.add(relacion)
    session.commit()
    return {"message": "Producto asociado a categoría exitosamente", "producto_id": producto_id, "categoria_id": categoria_id}

# DESASOCIAR PRODUCTO DE CATEGORÍA (DELETE)
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

# TRAER UNA RELACION
@router.get("/{producto_id}/categorias/{categoria_id}", status_code=status.HTTP_200_OK)
def obtener_relacion_clasica(
    producto_id: int, 
    categoria_id: int, 
    session: Session = Depends(get_session)
):
    relacion = session.get(ProductoCategoria, (producto_id, categoria_id))
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return relacion

# TRAER TODOS LOS DATOS DE UNA RELACION
@router.get("/{producto_id}/categorias/{categoria_id}/full", status_code=status.HTTP_200_OK)
def obtener_relacion_full(
    producto_id: int, 
    categoria_id: int, 
    session: Session = Depends(get_session)
):
   statement = (
        select(ProductoCategoria)
        .where(
            ProductoCategoria.producto_id == producto_id,
            ProductoCategoria.categoria_id == categoria_id
        )
        .options(
            selectinload(ProductoCategoria.producto),
            selectinload(ProductoCategoria.categoria)
        )
    )
   relacion = session.exec(statement).first()
    
   if not relacion:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    
   #armamos un objeto que traiga todos los datos 
   return {
        "producto_id": relacion.producto_id,
        "categoria_id": relacion.categoria_id,
        "producto": relacion.producto,     # datos del producto
        "categoria": relacion.categoria   #datos de la categoría
    }