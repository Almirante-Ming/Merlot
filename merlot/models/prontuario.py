from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from merlot.database.database import Base

class Prontuario(Base):
    __tablename__ = "prontuario"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao = Column(Date, nullable=False)
    id_paciente = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    
    paciente = relationship("Paciente", back_populates="prontuarios")
