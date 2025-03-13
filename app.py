from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = [] #Lista para armazenar alunos
aluno_id_controle = 1 #Controle de unicidade


#Adiciona um aluno
@app.route("/alunos", methods=["POST"])
def creat_alunos():
    global aluno_id_controle
    data = request.get_json() #Pega os dados enviados pelo cliente
    novo_aluno = {
        # id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final
        "id" : aluno_id_controle,
        "nome" : data.get("nome"),
        "turma_id" : data.get("turma_id"),
        "data_nascimento" : data.get("data_nascimento"),
        "nota_primeiro_semestre" : data.get("nota_primeiro_semestre"),
        "nota_segundo_semestre" : data.get ("nota_segundo_semestre"),
        "media_final" : data.get ("media_final")
    }
    alunos.append(novo_aluno)
    aluno_id_controle += 1
    return jsonify({"message": "Aluno adicionado com sucesso", "aluno": novo_aluno}), 201

# Rota para listar todos os alunos
@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify({"alunos": alunos, "total": len(alunos)})  # Retorna os alunos e a quantidade de alunos

# Rota para listar alunos por ID
@app.route("/alunos/<int:aluno_id>", methods=["GET"])   
def get_alunosID(aluno_id):
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if not aluno:
        return jsonify({"message": "Aluno não encontrado."}), 404
    return jsonify(aluno)





if __name__ == "__main__":
    app.run(debug = True)
