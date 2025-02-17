from flask import Blueprint,request,jsonify
from database.models.database import Livros

livros_routes= Blueprint('livros', __name__)

@livros_routes.route('/livros', methods=['GET'])
def obter_livros():
	return jsonify(Livros)

@livros_routes.route('/livros/<int:id>', methods= ['GET'])
def obter_livros_id(id):
	pass
@livros_routes.route('/livros/<int:id>', methods= ['PUT'])
def editar_livro_por_id(id):
	pass
@livros_routes.route('/livros', methods=['POST'])		
def incluir_novo_livro():
	pass

@livros_routes.route('/livros/<int:id>', methods= ['DELETE'])
def excluir_livros(id):
	pass
