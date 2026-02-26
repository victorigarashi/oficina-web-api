from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.schemas.agendamento_schema import AgendamentoCreate,  AgendamentoUpdate


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

