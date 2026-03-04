from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app.models.veiculo import  Veiculo
from app.schemas.veiculo_schema import VeiculoOutput, VeiculoCreate, VeiculoUpdate
from app.services import veiculo_service

router = APIRouter(
    prefix="/v1/veiculo",
    tags=["veiculo"]
)

@router.post("/", response_model=VeiculoOutput, status_code=status.HTTP_201_CREATED)
def create_veiculo(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    return veiculo_service.create_veiculo(db, veiculo)


@router.get("/{veiculo_id}", response_model=VeiculoOutput)
def get_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = veiculo_service.get_veiculo_by_id(db, veiculo_id)
    if not veiculo:
        raise HTTPException(status_code=404, detail="veiculo nao encontrado")
    
    return veiculo


@router.put("/{veiculo_id}", response_model=VeiculoOutput)
def update_veiculo(veiculo_id, veiculo: VeiculoUpdate, db: Session = Depends(get_db)):
    return veiculo_service.update_veiculo(db, veiculo_id, veiculo)


@router.delete("/{veiculo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo_service.delete_veiculo(db, veiculo_id)
    return