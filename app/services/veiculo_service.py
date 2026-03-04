from sqlalchemy.orm import Session
from app.models.veiculo import Veiculo
from app.models.agendamento import Agendamento
from app.schemas.veiculo_schema import VeiculoCreate,  VeiculoUpdate

def create_veiculo(db: Session, veiculo: VeiculoCreate) -> Veiculo:
    db_veiculo = Veiculo(
        modelo=veiculo.modelo,
        placa=veiculo.placa,
        ano=veiculo.ano,
        motor=veiculo.motor,
        quilometragem=veiculo.quilometragem,
        cliente_id=veiculo.cliente_id
    )
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def get_veiculo(db: Session, placa: str) -> Veiculo | None:
    db_veiculo = (
        db.query(Veiculo)
        .filter(Veiculo.placa == placa)
        .first()
    )
    if not db_veiculo:
        return False
    
    return db_veiculo

def update_veiculo_placa(db: Session, veiculo: VeiculoUpdate, nova_placa: str, placa_atual: str):
     db_veiculo = (
        db.query(Veiculo)
        .filter(Veiculo.placa == placa_atual)
        .first()
    )
     if not Veiculo:
         return False
     
     db_veiculo.placa = nova_placa
     db.commit()
     db.refresh(db_veiculo)
     return db_veiculo
 
def update_veiculo_quilometragem(db: Session, nova_quilometragem: int, placa: str):
     db_veiculo = (
        db.query(Veiculo)
        .filter(Veiculo.placa == placa)
        .first()
    )
     if not db_veiculo:
         return False
     db_veiculo.quilometragem = nova_quilometragem
     db.commit()
     db.refresh(db_veiculo)
     return db_veiculo
 
 
def delete_veiculo(db: Session, placa: str):
    db_veiculo = (
        db.query(Veiculo)
        .filter(Veiculo.placa == placa)
        .first()
    )
    if not db_veiculo:
         return False
     
    db.delete(db_veiculo)
    db.commit()
    return True