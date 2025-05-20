from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time, DateTime
from merlot.database.database import Base
from sqlalchemy.orm import relationship
from merlot.models.paciente import Paciente
from merlot.models.medico import Medico

class Consulta(Base):
    
    __tablename__ = 'consulta'
    
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    status = Column(String(20), nullable=False, default='ativa')
    observacoes = Column(Text)
    criado_em = Column(DateTime, default=datetime.now())
    atualizado_em = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    id_paciente = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    id_medico = Column(Integer, ForeignKey('medico.id'), nullable=False)

    paciente = relationship("Paciente", back_populates="consultas")
    medico = relationship("Medico", back_populates="consultas")