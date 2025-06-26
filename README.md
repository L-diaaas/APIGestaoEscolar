
# 🏫 API Gestão Escolar
Projeto desenvolvido como parte da disciplina de Desenvolvimento de API e Microsserviçoes do curso de Sistemas de Informação.

Esta é uma API RESTful para gerenciamento de informações escolares, implementada em Python com o framework Flask, utilizando SQLAlchemy para persistência de dados, documentação com Swagger, e testes automatizados com unittest.

## 👩‍💻 Desenvolvedoras

[Geovanna Toso](https://github.com/geovannatoso)

[Laura Dias](https://github.com/laura-dsouza)

[Talita Yuki](https://github.com/taltsolyu)

## 📁 Estrutura do Projeto
```
APIGestaoEscolar/
├── alunos/
│   ├── alunos_model.py
│   └── alunos_rotas.py
├── professores/
│   ├── professores_model.py
│   └── professores_routes.py
├── turmas/
│   ├── turmas_model.py
│   └── turmas_routes.py
├── instance/
│   └── app.db  # Banco de dados SQLite
├── swagger/    
│   ├── namespace/
│       ├── alunos_namespace.py
│       ├── professores_namespace.py
│       └──  turmas_namespace.py
│   ├── __init__.py
│   └── swagger_config.py
├── testes/
│   ├── testes_alunos.py
│   ├── testes_professores.py
│   ├── testes_turmas.py
│   └── testes_alunos_turmas_professores.py
├── README.md
├── app.py      # Arquivo principal
├── config.py   # Configurações da aplicação
├── dockerfile  # Dockerfile para containerização
└── requirements.txt    # Dependências do projeto
```

## 🚀 Como executar
- Python 3.10+

- (Opcional) Docker

- Pipenv ou virtualenv (opcional, mas recomendado)

### Passos para rodar localmente

- Clone o repositório

        git clone https://github.com/laura-dsouza/APIGestaoEscolar.git

        cd APIGestaoEscolar

- Crie o ambiente virtual (usando virtualenv ou pipenv)

        python -m venv venv

        source venv/bin/activate    #Linux/Mac

        venv\Scripts\activate       #Windows

- Instale as dependências

        pip install -r requirements.txt

- Execute a aplicação

        python app.py

### ⌨️ Endpoints principais
- A aplicação estará disponível em:

        http://localhost:5000

- Alunos: [http://localhost:5000/alunos](http://localhost:5000/alunos)

    - `GET /alunos` – Listar todos
    - `POST /alunos` – Criar novo
    - `GET /alunos/<id>` – Buscar por ID
    - `PUT /alunos/<id>` – Atualizar
    - `DELETE /alunos/<id>` – Remover

- Professores: [http://localhost:5000/professores](http://localhost:5000/professores)

    - `GET /professores` – Listar todos
    - `POST /professores` – Criar novo
    - `GET /professores/<id>` – Buscar por ID
    - `PUT /professores/<id>` – Atualizar
    - `DELETE /professores/<id>` – Remover

- Turmas: [http://localhost:5000/turmas](http://localhost:5000/turmas)

    - `GET /turmas` – Listar todas
    - `POST /turmas` – Criar nova
    - `GET /turmas/<id>` – Buscar por ID
    - `PUT /turmas/<id>` – Atualizar
    - `DELETE /turmas/<id>` – Remover

#### ⚠️ Atenção: Ordem de Cadastro Importa
Devido aos relacionamentos entre as entidades, a API exige uma ordem específica ao cadastrar:

- **Professores** devem ser cadastrados primeiro, pois uma **turma só pode ser criada se for vinculada a um professor existente**.
- Em seguida, cadastre a **turma**, associando-a a um professor.
- Por último, cadastre os **alunos**, vinculando-os a uma turma já registrada.

⛔ Tentar cadastrar uma turma sem um professor, ou um aluno sem uma turma, resultará em erro.

### 🧪 Executando os testes
Confira se está na pasta "APIGestaoEscolar" e execute os testes com os comandos:

        cd testes

        python -m unittest <nome do arquivo de teste que deseja executar sem o .py>

## 📚 Funcionalidades

- ✅ Cadastro, listagem, atualização e remoção de alunos

- ✅ Cadastro, listagem, atualização e remoção de professores

- ✅ Cadastro, listagem, atualização e remoção de turmas

- ✅ Integração via Swagger UI

- ✅ Testes automatizados

## 🧭 Documentação Swagger

A documentação interativa da API pode ser acessada em:

        http://localhost:5000/api/docs

## 🐳 Docker (opcional)
Para rodar com Docker:

- Build da imagem

        docker build -t apigestao .

- Executar container

        docker run -p 5000:5000 apigestao

## 📌 Observações
- Projeto desenvolvido para fins acadêmicos na disciplina de Desenvolvimento de API e Microsserviços.

- O banco de dados utilizado é o SQLite (instance/app.db).

- A estrutura segue o padrão MVC com rotas separadas por entidade.

## 📄 Licença
Este projeto é de uso acadêmico e não possui licença comercial.





