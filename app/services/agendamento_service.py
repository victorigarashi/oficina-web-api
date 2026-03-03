from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.models.cliente import Cliente
from app.schemas.agendamento_schema import AgendamentoCreate,  AgendamentoUpdate
from datetime import datetime
from typing import Optional, List


def create_agendamento(db: Session, agendamento: AgendamentoCreate) -> Agendamento:
        
        db_agendamento = Agendamento(
                data_hora=agendamento.data_hora,
                servico=agendamento.servico,
                cliente_id=agendamento.cliente_id,
                veiculo_id=agendamento.veiculo_id,
            
        )
        db.add(db_agendamento)
        db.commit()
        db.refresh(db_agendamento)

        return db_agendamento

def get_agendamento(
                db: Session, 
                email: Optional[str] = None
) -> list[Agendamento] :
         query = db.query(Agendamento).join(Cliente)

         if email is not None:
                query = query.filter(Cliente.email == email)

         return query.all()

def update_agendamentos(
        db: Session,
         agendamento_update: AgendamentoUpdate,
         agendamento_id: int,
         servico: str,
         data_hora: datetime
):
        db_agendamento = db.query(Agendamento).filter(
        Agendamento.id == agendamento_id
    ).first()
        
        if not db_agendamento:
            return None
        
        db_agendamento.servico = servico
        db_agendamento.data_hora = data_hora
        
        db.commit()
        db.refresh(db_agendamento)
        
        return db_agendamento

def delete_agendamento(db: Session, email: str) -> bool:
        db_agendamento = db.query(Agendamento).join(Cliente).filter(
        Cliente.email == email
    ).all()
        if not db_agendamento:
                return False
        db.delete(db_agendamento)
        db.commit()
        return True
