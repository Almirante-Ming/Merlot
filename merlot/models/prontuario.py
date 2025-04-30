#o SQLAlchemy, que é uma biblioteca que permite você criar tabelas como se fossem classes Python. Isso se chama ORM (Object-Relational Mapping)
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey# tipos do bancos que serão usados 
from merlot.database.database import Base # permite tranformar classe em tabela 

class Prontuario(Base):
    __tablename__ = "prontuario"
    id_prontuario = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao = Column(Date, nullable=False),
    id_paciente = Column(Integer, ForeignKey('id_paciente'), nullable=False)