from typing import Union
from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel

class response(BaseModel): #define la clase 
    message: str

class Cliente(BaseModel):#define una clase 
    id_cliente: int
    nombre: str
    email: str


app = FastAPI()

@app.get("/", response_model=response)#url donde se puede buscar 
async def index():
    return {"message": "Fast API"}#mensaje de correcta ejecucion 

        
@app.post("/clientes/", response_model=response)#url donde se puede buscar con el post /docs 
async def cliente_add(nombre:str,email:str,numero:str): #definicion de campos que pueden añadir 
    with sqlite3.connect("code/sql/clientes.sqlite") as connection: #creacion  de donde se conectara y dopnde se ecuentra la base de datos creada 
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("insert into clientes(nombre,email,numero) values ('{nombre}', '{email}','{numero}')".format(nombre=nombre, email=email, numero=numero)) #campos que incluira la base de datos creada esto para poder relizar una comparacion con la que se ecnuentra en el archivo clientes.sql 
        response = cursor.fetchone()
        data = {"message":"usuario agregado"}#mensaje de la correcta ejecucion del post al añadir algun cambio 
        return data

@app.put("/clientes/{id_usuario}", response_model=response)#url donde se puede buscar con el put /docs 
async def cliente_put(id_cliente: int, nombre: str,email:str): #en esta parte define los campos que deberia lleavar para poder modificar 
    with sqlite3.connect("code/sql/clientes.sqlite") as connection:#creacion de la conectividad y la ruta donde se encunetra el archivo de ejecucion
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("Update usuario set nombre = '{name}', email = '{email}' where id_cliente = {id}".format(name=nombre,email=email,id=id_cliente))#campos que debe incluir el campo donde se de sea ejecutar
        response = cursor.fetchone()
        data = {"message":"usuario actualizado"}#mensaje de una correcta ejecucion 
        return data

@app.delete("/clientes/{id_cliente}", response_model=response)#crea una url donde se puede buscar dicho campo asi como los apartados que debe de llevar 
async def cliente_delete(id_cliente: int):#muestra el campo adicional 
    with sqlite3.connect("code/sql/clientes.sqlite") as connection:#conectividad con la carpeta en la que se debe alojar 
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("delete from clientes where id_cliente = {}".format(id_cliente))#campos que se pueden eliminar 
        response = cursor.fetchone()
        data = {"message":"usuario borrado"}#mensaje de que la ejhecucion del delete se ejecuto de manera correcta 
        return data