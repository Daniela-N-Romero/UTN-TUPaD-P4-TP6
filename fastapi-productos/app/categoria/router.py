from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.core.database import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

router = APIRouter(prefix="/categorias", tags=["Categorias"])

# 1. LISTAR CATEGORÍAS (GET) ----------------------------------------------------------
@router.get("/", response_model=list[CategoriaRead])
def obtener_categorias(session: Session = Depends(get_session)):
    categorias = session.exec(select(Categoria)).all()
    return categorias

# 2. CREAR CATEGORÍA (POST)--------------------------------------------------------------
@router.post("/", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria_in: CategoriaCreate, session: Session = Depends(get_session)):
    # Convertimos el esquema de entrada al modelo de la base de datos con model_validate
    db_categoria = Categoria.model_validate(categoria_in)
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


# 3. TRAER UNA CATEGORIA POR ID (GET)-------------------------------------------------------
@router.get("/{categoria_id}", response_model=CategoriaRead)
def obtener_producto(categoria_id: int, session: Session = Depends(get_session)):
    db_categoria = session.get(Categoria, categoria_id)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    return db_categoria


# 3. ACTUALIZAR CATEGORÍA (PUT)----------------------------------------------------
@router.put("/{categoria_id}", response_model=CategoriaRead)
def actualizar_categoria(categoria_id: int, categoria_in: CategoriaUpdate, session: Session = Depends(get_session)):
    db_categoria = session.get(Categoria, categoria_id)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    # excluyendo los que vienen en None
    categoria_data = categoria_in.model_dump(exclude_unset=True)
    for key, value in categoria_data.items():
        setattr(db_categoria, key, value)
        
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria

# 4. ELIMINAR CATEGORÍA (DELETE)
@router.delete("/{categoria_id}", status_code=status.HTTP_200_OK)
def eliminar_categoria(categoria_id: int, session: Session = Depends(get_session)):
    db_categoria = session.get(Categoria, categoria_id)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    session.delete(db_categoria)
    session.commit()
    return {"message": "Categoría eliminada exitosamente", "id": categoria_id}