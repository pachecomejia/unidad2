from typing import Union
from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel

class response(BaseModel):
    message: str

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str


app = FastAPI()

@app.get("/", response_model=response)
async def index():
    return {"message": "Fast API"}

        
@app.post("/clientes/", response_model=response)
async def cliente_add(nombre:str,email:str,numero:str):
    with sqlite3.connect("clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("insert into clientes(nombre,email,numero) values ('{nombre}', '{email}','{numero}')".format(nombre=nombre, email=email, numero=numero))
        response = cursor.fetchone()
        data = {"message":"usuario agregado"}
        return data

@app.put("/clientes/{id_usuario}", response_model=response)
async def cliente_put(id_cliente: int, nombre: str,email:str):
    with sqlite3.connect("clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("Update usuario set nombre = '{name}', email = '{email}' where id_cliente = {id}".format(name=nombre,email=email,id=id_cliente))
        response = cursor.fetchone()
        data = {"message":"usuario actualizado"}
        return data

@app.delete("/clientes/{id_cliente}", response_model=response)
async def cliente_delete(id_cliente: int):
    with sqlite3.connect("clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("Delete from clientes where id_cliente = {}".format(id_cliente))
        response = cursor.fetchone()
        data = {"message":"usuario borrado"}
        return data