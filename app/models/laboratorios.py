from sqlalchemy import column, Integer, String
from db import Base

class Laboratorios(Base):
    __table_args__ = {"Schema": "laboratorios"}
    __table__="laboratorios"

    idlaboratorio = column(Integer, primary_key=True, index=True)
    nombre = column(String(50), nullable=True)
    tipo = column(String(30), nullable=True)
    ubicacion = column(String(50), nullable=True)

