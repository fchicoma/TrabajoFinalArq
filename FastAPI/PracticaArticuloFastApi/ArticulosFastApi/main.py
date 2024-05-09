from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from datetime import date


app = FastAPI()

class Articulo(BaseModel):
    id: int
    titulo: str
    autor: str
    contenido: str
    creado: date
    categoria: str

articulos = []


@app.post("/articulo/")
async def crear_articulo(articulo: Articulo):
    articulos.append(articulo)
    return {"mensaje": "Artículo cambiado creado exitosamente"}

@app.delete("/articulo/{id}")
async def borrar_articulo(id: int):
    for articulo in articulos:
        if articulo.id == id:
            articulos.remove(articulo)
            return {"mensaje": "Artículo cambiado borrado exitosamente"}
    return {"mensaje": "Artículo no encontrado"}

@app.put("/articulo/{id}")
async def modificar_articulo(id: int, articulo: Articulo):
    for index, articulo_existente in enumerate(articulos):
        if articulo_existente.id == id:
            articulos[index] = articulo
            return {"mensaje": "Artículo  cambiado modificado exitosamente"}
    return {"mensaje": "Artículo no encontrado"}

@app.get("/articulo/{id}", response_model=Articulo)
async def leer_articulo(id: int):
    for articulo in articulos:
        if articulo.id == id:
            return articulo
    return {"mensaje": "Artículo no encontrado"}