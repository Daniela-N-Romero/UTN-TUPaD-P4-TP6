from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

# Verificamos si estamos usando SQLite para aplicar 'check_same_thread'
connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Creamos el motor utilizando la URL configurada centralizadamente
engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session