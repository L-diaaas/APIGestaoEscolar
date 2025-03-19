from flask import Flask, jsonify, request


dici = {"turmas": []}

app = Flask(__name__)


@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(dici['turmas'])


@app.route('/turmas/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    for turma in dici['turmas']:
        if turma['id'] == turma_id:
            return jsonify(turma)
    return jsonify({'mensagem': 'Turma não encontrada'})


@app.route('/turmas', methods=['POST'])
def create_turma():
    dados = request.json
    if not dados or 'id' not in dados:
        return jsonify({'erro': 'Dados inválidos'})
    dici['turmas'].append(dados)
    return jsonify(dados)



@app.route('/turmas/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in dici["turmas"]:
        if turma['id'] == turma_id:
            dados = request.json
            turma.update({
                "id": dados.get('id', turma['id']),
                "descricao": dados.get('descricao', turma.get('descricao')),
                "professor_id": dados.get('professor_id', turma.get('professor_id')),
                "activo": dados.get('activo', turma.get('activo'))
            })
            return jsonify(turma)
    return jsonify({"mensagem": "Turma não encontrada!"})



@app.route('/turmas', methods=['DELETE'])
def delete_turmas():
    dici['turmas'].clear()
    return jsonify({'mensagem': 'Todas as turmas foram removidas'})


@app.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    turmas = dici['turmas']
    for turma in turmas:
        if turma['id'] == turma_id:
            dici['turmas'].remove(turma)
            return jsonify({'mensagem': 'Turma removida'})
    return jsonify({'mensagem': 'Turma não encontrada'})

if __name__ == "__main__":
    app.run(debug=True)