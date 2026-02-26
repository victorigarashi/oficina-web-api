from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    cpf: Optional[str] = None
    
class ClienteCreate(ClienteBase):
    password: str

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None
    password: Optional[str] = None

class ClienteOutput(ClienteBase):
   id: int

   class config:
    from_attributes = True


    
    