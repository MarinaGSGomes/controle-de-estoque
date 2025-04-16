# db_connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.produto import Base  # Importa a base declarativa para criar as tabelas

DATABASE_URL = "sqlite:///estoque.db"  # Substitua pela URL do seu banco de dados

# Criação do engine
engine = create_engine(DATABASE_URL)

# Configuração da sessão
Session = sessionmaker(bind=engine)

def get_session():
    """Cria e retorna uma nova sessão."""
    return Session()

def close_session(session):
    """Fecha a sessão fornecida."""
    session.close()

def criar_tabelas():
    """Cria as tabelas no banco de dados, se não existirem."""
    Base.metadata.create_all(engine)
    # Cria todas as tabelas definidas na base declarativa
    # Caso queira criar apenas uma tabela específica, use:
    # Base.metadata.create_all(engine, tables=[Produto.__table__])
    # Exemplo: Base.metadata.create_all(engine, tables=[Produto.__table__])
    # Caso queira criar apenas uma tabela específica, use:
    # Base.metadata.create_all(engine, tables=[Produto.__table__])
    # Exemplo: Base.metadata.create_all(engine, tables=[Produto.__table__])