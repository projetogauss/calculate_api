from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


"""
Testando URI raiz com metedo GET
"""
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Teste Capgemini":"Tiago Samapaio",
                                "Status": "Finalizado"}

"""
Testando operacao de somar passando o objeto JSON
via POST e somando os valores das chaves price e juros
"""
def test_somar():
    response = client.post(
        "/calcula/",
         json={
                "name": "Mock",
                "description": "Testando endpoint",
                "price": 30.0,
                "juros": 3.0,
                "tax": 1.0,
                "acao": "sum"
            },
    )
    assert response.status_code == 200
    assert response.json() == {
                            "result": 33.0
                            }

"""
Testando operacao de dividir passando o objeto JSON
via POST e dividindo os valores das chaves price e juros
"""
def test_dividir():
    response = client.post(
        "/calcula/",
         json={
                "name": "Mock",
                "description": "Testando endpoint",
                "price": 30.0,
                "juros": 3.0,
                "tax": 1.0,
                "acao": "div"
            },
    )
    assert response.status_code == 200
    assert response.json() == {"result" : 10}

"""
Testando operacao de multiplicar passando o objeto JSON
via POST e multiplicando os valores das chaves price e juros
"""
def test_multiplicar():
    response = client.post(
        "/calcula/",
         json={
                "name": "Mock",
                "description": "Testando endpoint",
                "price": 30.0,
                "juros": 3.0,
                "tax": 1.0,
                "acao": "mul"
            },
    )
    assert response.status_code == 200
    assert response.json() == {"result" : 90}
"""
Testando operacao de subtrair passando o objeto JSON
via POST e subtrair os valores das chaves price e juros
"""
def test_subtrair():
    response = client.post(
        "/calcula/",
         json={
                "name": "Mock",
                "description": "Testando endpoint",
                "price": 30.0,
                "juros": 3.0,
                "tax": 1.0,
                "acao": "sub"
            },
    )
    assert response.status_code == 200
    assert response.json() == {"result" : 27}

