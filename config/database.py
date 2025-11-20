# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão (de acordo com o docker-compose)
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/db_gerenciador_contas"

# Cria o engine (gerencia a conexão)
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões (para interagir com o banco)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para as classes ORM (models)
Base = declarative_base()

# Dependência para FastAPI (injeção de sessão)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()