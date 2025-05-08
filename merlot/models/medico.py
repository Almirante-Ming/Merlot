from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from merlot.database.database import Base

class Medico(Base):
    __tablename__ = "medico"
    id_medico = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    crm = Column(String)
    especialidade = Column(String)
    telefone = Column(String)

    consultas = relationship("Consulta", back_populates="medico")  #aqui liga com Consulta
