from main import app
from fastapi.testclient import TestClient
import requests
import json

clientes = TestClient(app)

def test_index():
    response = clientes.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Fast API"}
    




def test_add():
    parametrosAdd = {"nombre":"name","email":"ejemplo@email.com","numero":"7752225588"}
    response = clientes.post("/clientes/", params=parametrosAdd)
    data_add = {"message":"usuario agregado"}
    assert response.status_code == 200
    assert response.json() == data_add



def test_delete():
    response = clientes.delete("/clientes/6")
    dataCliente_delete = {"message":"usuario borrado"}
    assert response.status_code == 200
    assert response.json() == dataCliente_delete