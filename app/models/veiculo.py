from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.orm import relationship

class Veiculo(Base):
    __tablename__ = "veiculos"
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, nullable=False)
    motor = Column(String, nullable=False)
    placa = Column(String, nullable=False)
    quilometragem = Column(String, nullable=False)
    agendamento = relationship("Agendamento", back_populates="veiculo")