from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship #definie relacionamento entre as tabelas 
from merlot.database.database import Base

class Paciente(Base):
    __tablename__ = "paciente"
    id_paciente = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date)
    cpf = Column(String, unique=True)
    telefone = Column(String)
    email = Column(String)

    consultas = relationship("Consulta", back_populates="paciente")  # 👈 aqui liga com Consulta
