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
                                "Status": "Em Andamento"}

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
                "price": 110.0,
                "juros": 11.50,
                "tax": 1.0,
                "acao": "sum",
                "result": 0
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        {
            "name": "Mock",
            "description": "Testando endpoint",
            "price": 110.0,
            "juros": 11.50,
            "tax": 1.0,
            "acao": "sum",
            "result": 121.5
        },
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
                "price": 110.0,
                "juros": 11.50,
                "tax": 1.0,
                "acao": "div",
                "result": 0
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        {
            "name": "Mock",
            "description": "Testando endpoint",
            "price": 110.0,
            "juros": 11.50,
            "tax": 1.0,
            "acao": "div",
            "result": 9.565217391304348
        },
    }

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
                "price": 110.0,
                "juros": 11.50,
                "tax": 1.0,
                "acao": "mul",
                "result": 0
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        {
            "name": "Mock",
            "description": "Testando endpoint",
            "price": 110.0,
            "juros": 11.50,
            "tax": 1.0,
            "acao": "mul",
            "result": 1265.0
        },
    }
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
                "price": 110.0,
                "juros": 11.50,
                "tax": 1.0,
                "acao": "sub",
                "result": 0
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        {
            "name": "Mock",
            "description": "Testando endpoint",
            "price": 110.0,
            "juros": 11.50,
            "tax": 1.0,
            "acao": "sub",
            "result": 98.5
        },
    }

    """
Testando operacao de subtrair passando o objeto JSON
via POST e subtrair os valores das chaves price e juros
"""
def test_operacao_que_nao_exist():
    response = client.post(
        "/calcula/",
         json={
                "name": "Mock",
                "description": "Testando endpoint",
                "price": 110.0,
                "juros": 11.50,
                "tax": 1.0,
                "acao": "su2",
                "result": 0
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        {
            "name": "Mock",
            "description": "Testando endpoint",
            "price": 110.0,
            "juros": 11.50,
            "tax": 1.0,
            "acao": "sub",
            "result": "Operação não encontrada"
        },
    }