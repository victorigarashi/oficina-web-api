from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Agendamento(Base):
    __tablename__ = "Agendamento"
    id = Column(String, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    servico = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=False)
    status = Column(String, default="Pendente")
    cliente = relationship("Cliente", back_populates="agendamentos")
    veiculo = relationship("Veiculo", back_populates="agendamentos")
    