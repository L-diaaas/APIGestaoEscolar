import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/alunos"  # URL DA API

def test001_criar_aluno():
    novo_aluno = {
        "nome": "João Silva",
        "idade": 16,
        "turma_id": 1,
        "data_nascimento": "2008-03-10",
        "nota_primeiro_semestre": 8.5,
        "nota_segundo_semestre": 7.8,
        "media_final": 8.15
    }
    response = requests.post(BASE_URL, json=novo_aluno)
    assert response.status_code == 201
    assert response.json() == novo_aluno


def test002_obter_alunos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test003_obter_aluno_por_id():
    aluno_id = 1
    response = requests.get(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 200
    assert aluno_id in [aluno['id'] for aluno in response.json()]

def test004_atualizar_aluno():
    aluno_id = 1 
    dados_atualizados = {"nome": "João Pedro Silva", "idade": 17}
    response = requests.put(f"{BASE_URL}/{aluno_id}", json=dados_atualizados)
    assert response.status_code == 200
    assert response.json()['id'] == aluno_id

def test005_excluir_aluno():
    aluno_id = 1  
    response = requests.delete(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 204


def test006_criar_aluno_com_numero_no_nome():
    novo_aluno = {
        "nome": 12345, 
        "idade": 16,
        "turma_id": 1,
        "data_nascimento": "2008-03-10",
        "nota_primeiro_semestre": 8.5,
        "nota_segundo_semestre": 7.8,
        "media_final": 8.15
    }
    response = requests.post(BASE_URL, json=novo_aluno)
    assert response.status_code == 400 

def test007_obter_aluno_nao_existente():
    aluno_id = 9999  
    response = requests.get(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 404 

def test008_atualizar_aluno_nao_existente():
    aluno_id = 9999  
    dados_atualizados = {"nome": "Aluno Inexistente", "idade": 17}
    response = requests.put(f"{BASE_URL}/{aluno_id}", json=dados_atualizados)
    assert response.status_code == 404 

def test009_excluir_aluno_nao_existente():
    aluno_id = 9999 
    response = requests.delete(f"{BASE_URL}/{aluno_id}")
    assert response.status_code == 404 
