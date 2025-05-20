from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from merlot.database.database import Base

class Atendimento(Base):
    
    __tablename__ = "atendimento"
    
    id_atendimento = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    tipo = Column(String(50), nullable=False)
    observacoes = Column(Text)
    id_prontuario = Column(Integer, ForeignKey ('prontuario.id'), nullable=False)
    id_medico = Column(Integer, ForeignKey('medico.id'), nullable=False)