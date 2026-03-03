from sqlalchemy.orm import Session
from app.models.cliente import Cliente
import hashlib
from app.schemas.cliente_schema import ClienteCreate, ClienteUpdate


def hash_password(password: str) -> str:
    return hashlib.sha3_256(password.encode("utf-8")).hexdigest()
    


def create_cliente(db: Session, cliente: ClienteCreate) -> Cliente:
    db_cliente = Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        cpf=cliente.cpf,
        email=cliente.email,
        password=hash_password(cliente.password)
    )
    
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def get_cliente(db: Session, email: str, password: str):
    senha_hash = hash_password(password)
    db_cliente = (
        db.query(Cliente)
        .filter(
            Cliente.email == email,
            Cliente.password == senha_hash
        )
        .first()
    )
    return db_cliente

def update_password_cliente(db: Session, email: str, nova_senha: str):
    db_cliente = (
        db.query(Cliente)
        .filter(Cliente.email == email)
        .first()
    )

    if not db_cliente:
        return None

    db_cliente.password = hash_password(nova_senha)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, email: str) -> bool:
    db_cliente = (
        db.query(Cliente)
        .filter(
            Cliente.email == email,
        )
        .first()
    )
    if not db_cliente:
        return False
    db.delete(db_cliente)
    db.commit()
    return True