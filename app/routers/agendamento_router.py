from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app.models.agendamento import  Agendamento
from app.schemas.agendamento_schema import AgendamentoOutput, AgendamentoCreate, AgendamentoUpdate
from app.services import agendamento_service

router = APIRouter(
    prefix="/v1/agendamento",
    tags=["agendamento"]
)

@router.post("/", response_model=[AgendamentoOutput],status_code=status.HTTP_201_CREATED)
def create_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    return agendamento_service.create_agendamento(db, agendamento)


@router.get("/", response_model=list[AgendamentoOutput]) # lista todos os agendamentos
def list_agendamento(db: Session = Depends(get_db)):
    return agendamento_service.get_agendamento(db)


@router.get("/{agendamento_id}", response_model=AgendamentoOutput) # busca apenas um agendamento
def get_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    agendamento = agendamento_service.get_agendamento_by_id(db, agendamento_id)
    if not agendamento:
        raise HTTPException(status_code=404, detail="agendamento nao encontrado")
    
    return agendamento


@router.put("/{agendamento_id}", response_model=AgendamentoOutput)
def update_agendamento(agendamento_id: int, agendamento: AgendamentoUpdate, db: Session = Depends(get_db)):
    return agendamento_service.update_agendamentos(db, agendamento_id, agendamento)


@router.delete("/{agendamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    agendamento_service.delete_agendamento(db, agendamento_id)
    return