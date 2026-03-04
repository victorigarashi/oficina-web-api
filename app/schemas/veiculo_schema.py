from typing import Optional
from pydantic import BaseModel

class VeiculoBase(BaseModel):
    modelo: str
    ano: int
    motor: Optional[str]
    placa: str
    quilometragem: int

class VeiculoCreate(VeiculoBase):
    cliente_id: int

class VeiculoUpdate(BaseModel):
    modelo: Optional[str] = None
    ano: Optional[int] = None
    motor: Optional[str] = None
    placa: Optional[str] = None
    quilometragem: Optional[int] = None

class VeiculoOutput(VeiculoBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True