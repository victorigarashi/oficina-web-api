from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.schemas.cliente_schema import ClienteOutput
from app.schemas.veiculo_schema import VeiculoOutput

class AgendamentoBase(BaseModel):
    cliente_id: int
    veiculo_id: int
    data_hora: datetime
    servico: str

class AgendamentoCreate(AgendamentoBase):
    confirmacao: str

class AgendamentoUpdate(BaseModel):
    data_hora: Optional[datetime] = None
    servico: Optional[str] = None

class AgendamentoOutput(AgendamentoBase):
    id: int
    cliente_id: int
    veiculo_id: int
    status: str
    criado_em: datetime

    class Config:
        from_attributes = True

class AgendamentoRead(AgendamentoOutput):
    cliente: ClienteOutput
    veiculo: VeiculoOutput