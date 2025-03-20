import unittest
import requests
from flask import Flask

class TestStudentMethods(unittest.TestCase):
  
    BASE_URL = 'http://127.0.0.1:5000/alunos'

    def test_000_criar_aluno_sucesso(self):
        aluno = {
            "nome": "Maria Silva",
            "turma_id": 101,
            "idade": 20,
            "data_nascimento": "2004-03-19",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 9.0,
            "media_final": 8.75
        }
        response = requests.post(self.BASE_URL, json=aluno)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['aluno']['nome'], aluno['nome'])

    def test_001_criar_aluno_erro_sem_nome(self):
        aluno = {
            "nome": None,
            "turma_id": 102,
            "idade": 22,
            "data_nascimento": "2002-03-19",
            "nota_primeiro_semestre": 7.0,
            "nota_segundo_semestre": 7.5,
            "media_final": 7.25
        }
        response = requests.post(self.BASE_URL, json=aluno)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], "O campo 'nome' é obrigatório e deve estar preenchido.")

    def test_002_listar_alunos(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_003_buscar_aluno_id_sucesso(self):
        # Primeiro, criamos o aluno para garantir que ele exista
        aluno = {
            "nome": "Lucas Rocha",
            "turma_id": 103,
            "idade": 21,
            "data_nascimento": "2003-03-19",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.0,
            "media_final": 7.75
        }
        response_post = requests.post(self.BASE_URL, json=aluno)
        aluno_id = response_post.json()['aluno']['id']
        
        # Agora, verificamos se conseguimos recuperar esse aluno com o ID correto
        response_get = requests.get(f"{self.BASE_URL}/{aluno_id}")
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_get.json()['nome'], aluno['nome'])

    def test_004_buscar_aluno_id_erro(self):
        aluno_id = 9999  # Um ID que não existe
        response = requests.get(f"{self.BASE_URL}/{aluno_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], "Aluno não encontrado.")

    def test_005_atualizar_aluno_sucesso(self):
        aluno = {
            "nome": "Ana Souza",
            "turma_id": 104,
            "idade": 23,
            "data_nascimento": "2001-03-19",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 8.5,
            "media_final": 8.25
        }
        response_post = requests.post(self.BASE_URL, json=aluno)
        aluno_id = response_post.json()['aluno']['id']
        
        # Atualizando o aluno
        aluno_atualizado = {
            "nome": "Ana Souza Silva",
            "turma_id": 105,
            "idade": 24,
            "data_nascimento": "2000-03-19",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 9.0,
            "media_final": 9.0
        }
        response_put = requests.put(f"{self.BASE_URL}/{aluno_id}", json=aluno_atualizado)
        self.assertEqual(response_put.status_code, 200)
        self.assertEqual(response_put.json()['aluno']['nome'], aluno_atualizado['nome'])

    def test_006_atualizar_aluno_erro(self):
        aluno_id = 9999  # Um ID que não existe
        aluno_atualizado = {
            "nome": "Pedro Alves",
            "turma_id": 106,
            "idade": 25,
            "data_nascimento": "1999-03-19",
            "nota_primeiro_semestre": 6.0,
            "nota_segundo_semestre": 6.5,
            "media_final": 6.25
        }
        response = requests.put(f"{self.BASE_URL}/{aluno_id}", json=aluno_atualizado)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], "Aluno não encontrado.")

    def test_007_deletar_aluno_sucesso(self):
        aluno = {
            "nome": "Carlos Oliveira",
            "turma_id": 107,
            "idade": 22,
            "data_nascimento": "2002-03-19",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.5,
            "media_final": 8.0
        }
        response_post = requests.post(self.BASE_URL, json=aluno)
        aluno_id = response_post.json()['aluno']['id']
        
        # Agora, tentamos excluir o aluno
        response_delete = requests.delete(f"{self.BASE_URL}/{aluno_id}")
        self.assertEqual(response_delete.status_code, 200)
        self.assertEqual(response_delete.json()['message'], "Aluno deletado com sucesso!")

    def test_008_deletar_aluno_erro(self):
        aluno_id = 9999  # Um ID que não existe
        response = requests.delete(f"{self.BASE_URL}/{aluno_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Aluno não encontrado.")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStudentMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
