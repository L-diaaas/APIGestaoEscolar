from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = [] #Lista para armazenar alunos
aluno_id_controle = 1 

@app.route("/alunos", methods=["POST"])
def create_alunos():
    global aluno_id_controle
    data = request.get_json() 
    novo_aluno = {
        "id" : aluno_id_controle,
        "nome" : data.get("nome"),
        "turma_id" : data.get("turma_id"),
        "idade" : int(data.get("idade")),
        "data_nascimento" : data.get("data_nascimento"),
        "nota_primeiro_semestre" : float(data.get("nota_primeiro_semestre")),
        "nota_segundo_semestre" : float(data.get ("nota_segundo_semestre")),
        "media_final" : float(data.get ("media_final"))
    }
    alunos.append(novo_aluno)
    aluno_id_controle += 1
    return jsonify({"message": "Aluno adicionado com sucesso", "aluno": novo_aluno}), 201


@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(alunos) 


@app.route("/alunos/<int:aluno_id>", methods=["GET"])   
def get_alunosID(aluno_id):
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if not aluno:
        return jsonify({"message": "Aluno não encontrado."}), 404
    return jsonify(aluno)


@app.route("/alunos/<int:aluno_id>", methods=["PUT"])
def update_aluno(aluno_id):
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if not aluno:
        return jsonify({"message": "Aluno não encontrado."}), 404
    
    data = request.get_json()
    aluno["nome"] = data.get("nome", aluno["nome"])
    aluno["turma_id"] = data.get("turma_id", aluno["turma_id"])
    aluno["idade"] = int(data.get("idade", aluno["idade"]))
    aluno["data_nascimento"] = data.get("data_nascimento", aluno["data_nascimento"])
    aluno["nota_primeiro_semestre"] = float( data.get("nota_primeiro_semestre", aluno["nota_primeiro_semestre"]))
    aluno["nota_segundo_semestre"] = float(data.get("nota_segundo_semestre", aluno["nota_segundo_semestre"]))
    aluno["media_final"] = float(data.get("media_final", aluno["media_final"]))
    return jsonify({"message": "Aluno atualizado com sucesso!", "aluno": aluno})

@app.route("/alunos/<int:aluno_id>", methods=["DELETE"])
def delete_aluno(aluno_id):
    global alunos
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)
    if not aluno:
        return jsonify ({"message": "Aluno não encontrado"}), 404
    alunos.remove(aluno)
    return jsonify ({"message": "Aluno deletado com sucesso!"}), 204



if __name__ == "__main__":
    app.run(debug = True)
