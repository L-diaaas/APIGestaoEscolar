import unittest
import requests

class TestTurmasMethods(unittest.TestCase):
    
    BASE_URL = "http://localhost:5000/turmas"

    def test_get_turmas(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_turma_sucesso(self):
        turma = {
            "id": 1,
            "descricao": "Turma de Matemática",
            "professor_id": 101,
            "activo": True
        }
        requests.post(self.BASE_URL, json=turma)
        response = requests.get(f"{self.BASE_URL}/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_get_turma_erro(self):
        response = requests.get(f"{self.BASE_URL}/9999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['mensagem'], 'Turma não encontrada')

    def test_create_turma_sucesso(self):
        turma = {
            "id": 2,
            "descricao": "Turma de História",
            "professor_id": 102,
            "activo": True
        }
        response = requests.post(self.BASE_URL, json=turma)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['descricao'], turma['descricao'])

    def test_create_turma_erro(self):
        turma = {
            "descricao": "Turma de Geografia"
        }
        response = requests.post(self.BASE_URL, json=turma)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json()['erro'], 'Dados inválidos')

    def test_update_turma_sucesso(self):
        turma = {
            "id": 3,
            "descricao": "Turma de Física",
            "professor_id": 103,
            "activo": True
        }
        requests.post(self.BASE_URL, json=turma)
        updated_turma = {
            "descricao": "Turma de Física Avançada",
            "professor_id": 104,
            "activo": False
        }
        response = requests.put(f"{self.BASE_URL}/3", json=updated_turma)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['descricao'], updated_turma['descricao'])

    def test_update_turma_erro(self):
        updated_turma = {
            "descricao": "Turma de Química",
            "professor_id": 105,
            "activo": True
        }
        response = requests.put(f"{self.BASE_URL}/9999", json=updated_turma)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['mensagem'], "Turma não encontrada!")

    def test_delete_turmas(self):
        turma = {
            "id": 4,
            "descricao": "Turma de Biologia",
            "professor_id": 106,
            "activo": True
        }
        requests.post(self.BASE_URL, json=turma)
        response = requests.delete(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['mensagem'], 'Todas as turmas foram removidas')

    def test_delete_turma_sucesso(self):
        turma = {
            "id": 5,
            "descricao": "Turma de Artes",
            "professor_id": 107,
            "activo": True
        }
        requests.post(self.BASE_URL, json=turma)
        response = requests.delete(f"{self.BASE_URL}/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['mensagem'], 'Turma removida')

    def test_delete_turma_erro(self):
        response = requests.delete(f"{self.BASE_URL}/9999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['mensagem'], 'Turma não encontrada')

if __name__ == '__main__':
    unittest.main()
