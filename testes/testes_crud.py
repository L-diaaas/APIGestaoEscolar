import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/alunos"

def test_criar_aluno():
    aluno = {
        "nome": "João",
        "idade": 20,
        "turma_id": 1,
        "data_nascimento": "2003-01-01",
        "nota_primeiro_semestre": 7.0,
        "nota_segundo_semestre": 8.0,
        "media_final": 7.5
    }
    response = requests.post(BASE_URL, json=aluno)
    assert response.status_code == 201
    assert response.json()["message"] == "Aluno adicionado com sucesso"

def test_listar_alunos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)  

def test_listar_aluno_por_id():
    aluno = {
        "nome": "Carlos",
        "idade": 22,
        "turma_id": 4,
        "data_nascimento": "2001-05-10",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 9.0,
        "media_final": 8.5
    }
    response = requests.post(BASE_URL, json=aluno)
    assert response.status_code == 201 

    aluno_id = response.json()["aluno"]["id"]

    response = requests.get(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Carlos"

def test_atualizar_aluno():
    aluno = {
        "nome": "João",
        "idade": 20,
        "turma_id": 1,
        "data_nascimento": "2003-01-01",
        "nota_primeiro_semestre": 7.0,
        "nota_segundo_semestre": 8.0,
        "media_final": 7.5
    }
    response = requests.post(BASE_URL, json=aluno)
    assert response.status_code == 201  

    aluno_id = response.json()["aluno"]["id"]

    aluno_atualizado = {
        "nome": "João Atualizado",
        "idade": 21,
        "turma_id": 1,
        "data_nascimento": "2003-01-01",
        "nota_primeiro_semestre": 7.5,
        "nota_segundo_semestre": 8.5,
        "media_final": 8.0
    }
    response = requests.put(f"{BASE_URL}/{aluno_id}", json=aluno_atualizado)
    assert response.status_code == 200
    assert response.json()["message"] == "Aluno atualizado com sucesso!"

def test_deletar_aluno():
    aluno = {
        "nome": "Lucas",
        "idade": 19,
        "turma_id": 2,
        "data_nascimento": "2004-02-15",
        "nota_primeiro_semestre": 6.0,
        "nota_segundo_semestre": 7.0,
        "media_final": 6.5
    }
    response = requests.post(BASE_URL, json=aluno)
    assert response.status_code == 201  

    aluno_id = response.json()["aluno"]["id"]

    response = requests.delete(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 204 

    response = requests.get(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 404  
