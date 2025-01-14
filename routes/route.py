from flask import Blueprint,request,jsonify
from database.database import livros

livros_routes= Blueprint('livros', __name__)

@livros_routes.route('/livros', methods=['GET'])
def obter_livros():
	return jsonify(livros)

@livros_routes.route('/livros/<int:id>', methods= ['GET'])
def obter_livros_id(id):
	for livro in livros:
		if livro.get('id')== id:
			return jsonify(livro)
@livros_routes.route('/livros/<int:id>', methods= ['PUT'])
def editar_livro_por_id(id):
	livro_alterado=request.get_json
	for indice, livro in enumerate(livros):
		if livro.get('id')==id:
			livros[indice].update(livro_alterado)
			return jsonify(livros[indice])
		
@livros_routes.route('/livros', methods=['POST'])		
def incluir_novo_livro():
	novo= request.get_json
	livros.append(novo)
	return jsonify(livros)

@livros_routes.route('/livros/<int:id>', methods= ['DELETE'])
def excluir_livros(id):
	for indice, livro in enumerate(livros):
		if livro.get('id')== id:
			del livros[indice]
	return jsonify(livros)		

