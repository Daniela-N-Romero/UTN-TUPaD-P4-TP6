from sqlmodel import Session, select
from app.core.database import engine, create_db_and_tables
from app.categoria.model import Categoria
from app.producto.model import Producto, ProductoCategoria

def ejecutar_seed():
    # Verificamos si ya hay categorías cargadas
    with Session(engine) as session:
        categorias_existentes = session.exec(select(Categoria)).first()
        
        # Si está vacía, insertamos los datos iniciales
        if not categorias_existentes:
            print("Base de datos vacía detectada. Insertando datos iniciales...")
            
            cat1 = Categoria(nombre="Pizzas", descripcion="Pizzas artesanales con masa fresca")
            cat2 = Categoria(nombre="Bebidas", descripcion="Bebidas frías y gaseosas")
            session.add(cat1)
            session.add(cat2)
            session.commit()
            session.refresh(cat1)
            session.refresh(cat2)

            prod1 = Producto(
                nombre="Pizza Mozzarella",
                descripcion="Salsa de tomate, mozzarella y orégano",
                precio_base="8500",
                imagen_url=["https://ejemplo.com/pizza.jpg"],
                disponible=True
            )
            prod2 = Producto(
                nombre="Coca Cola 1.5L",
                descripcion="Bebida gaseosa retornable",
                precio_base="2500",
                imagen_url=["https://ejemplo.com/coca.jpg"],
                disponible=True
            )
            session.add(prod1)
            session.add(prod2)
            session.commit()
            session.refresh(prod1)
            session.refresh(prod2)

            rel1 = ProductoCategoria(producto_id=prod1.id, categoria_id=cat1.id)
            rel2 = ProductoCategoria(producto_id=prod2.id, categoria_id=cat2.id)
            session.add(rel1)
            session.add(rel2)
            session.commit()
            print("Datos iniciales cargados con éxito a la BD.")