from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app.models.cliente import Cliente
from app.schemas.cliente_schema import ClienteCreate, ClienteOutput, ClienteUpdate
from app.services import cliente_service

router = APIRouter(
    prefix="/v1/clientes",
    tags=["cliente"]  
)

@router.post("/", response_model=list[ClienteOutput], status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.create_cliente(db, cliente)


@router.get("/{cliente_id}", response_model=ClienteOutput) #busca apenas um cliente
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = cliente_service.get_cliente_by_id(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="cliente nao encontrado")
    
    return cliente


@router.put("/{cliente_id}", response_model=ClienteOutput)
def update_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    return cliente_service.update_cliente(db, cliente_id, cliente)


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_service.delete_cliente(db, cliente_id)
    return 