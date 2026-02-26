from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.orm import relationship

class Veiculo(Base):
    __tablename__ = "Veiculos"
    id = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    motor = Column(String, nullable=False)
    placa = Column(String, nullable=False)
    quilometragem = Column(String, nullable=False)
    agendamentos = relationship("Agendamento", back_populates="veiculo")