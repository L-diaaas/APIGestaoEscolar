import requests
import unittest

BASE_URL = ""  #URL DA API

class TestAlunosAPI(unittest.TestCase):
    def test001_criar_aluno(self):
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["nome"], "João Silva")

    def test002_obter_alunos(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test003_obter_aluno_por_id(self):
        aluno_id = 1  # Substitua por um ID existente
        response = requests.get(f"{BASE_URL}/{aluno_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("nome", response.json())

    def test004_atualizar_aluno(self):
        aluno_id = 1  # Substitua por um ID existente
        dados_atualizados = {"nome": "João Pedro Silva", "idade": 17}
        response = requests.put(f"{BASE_URL}/{aluno_id}", json=dados_atualizados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nome"], "João Pedro Silva")

    def test005_excluir_aluno(self):
        aluno_id = 1  # Substitua por um ID existente
        response = requests.delete(f"{BASE_URL}/{aluno_id}")
        self.assertEqual(response.status_code, 204)

    def test006_criar_aluno_com_numero_no_nome(self):
        novo_aluno = {
            "nome": 12345,  # Número no lugar de string
            "idade": 16,
            "turma_id": 1,
            "data_nascimento": "2008-03-10",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.8,
            "media_final": 8.15
        }
        response = requests.post(BASE_URL, json=novo_aluno)
        self.assertEqual(response.status_code, 400)  # requisição inválida

    def test007_obter_aluno_nao_existente(self):
        aluno_id = 9999  # ID que não existe
        response = requests.get(f"{BASE_URL}/{aluno_id}")
        self.assertEqual(response.status_code, 404)  #  "não encontrado"

    def test008_atualizar_aluno_nao_existente(self):
        aluno_id = 9999  # ID que não existe
        dados_atualizados = {"nome": "Aluno Inexistente", "idade": 17}
        response = requests.put(f"{BASE_URL}/{aluno_id}", json=dados_atualizados)
        self.assertEqual(response.status_code, 404)  #  "não encontrado"

    def test009_excluir_aluno_nao_existente(self):
        aluno_id = 9999  # ID que não existe
        response = requests.delete(f"{BASE_URL}/{aluno_id}")
        self.assertEqual(response.status_code, 404)  #  "não encontrado"

if __name__ == "__main__":
    unittest.main()