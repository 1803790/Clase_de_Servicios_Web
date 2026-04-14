from fastapi import FastAPI
from typing import List
from app.db import Base, engine, Session
from app.schemas.laboratorio import LaboratorioBase 
from app.models.laboratorios import Laboratorios

app = FastAPI(
    title="FastAPI Servicios web",
    version="0.1",
    description="API DESARROLLADA CON FASTAPI PARA SERVICIOS WEB UTILIZANDO FASTAPI",
)
@app.get("/")
async def root():
    return {"message": "Bienvenido a FastAPI Servicios web"}

@app.get("/laboratorios", response_model=List[LaboratorioBase])
def listar_laboratorios():
   db = Session()
   labs =  db.query(Laboratorios).all()
   db.close()
   return labs