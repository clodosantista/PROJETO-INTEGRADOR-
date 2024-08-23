#API É UM LOCAL PARA DISPONIBILIZAR RECURSOS E/OU FUNCIONALIDADES É UMA PONTE
#1. OBJETIVO: Criar uma API que disponibiliza a consulta, criação, edição e exclusão
#2. URL base - localhost
#3. Endpoints-
    # localhost/carros (GET)
    # localhost/carros (PUT)
    # localhost/carros (DELETE)
    # localhost/carros id (GET)

from flask import Flask, jsonify, request, make_response
#Importa o banco de dados
from bd import Carros


#Instanciar o modulo Flask na nossa variavel app
app= Flask('carros')

#PRIMEIRO MÉDTODO - VISUALIZAR DADOS (GET)
#app.route -> definir que essa função é uma rota para que o flask é um metodo que deve ser executado
@app.route('/carros', methods= ['GET'])
def get_carros():
    return Carros



#PRIMEIRO MÉTODO PARTE 2 - VISUALIZAR DADOS POR ID (GET / ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)

#SEGUNDO MÉTODO - CRIAR NOVOS DADOS (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro= request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso',
                carro=carro
                )
    )

#TERCEIRO MÉTODO - EDITAR DADOS (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])



#QUARTO MÉTODO -  DELETAR DADOS (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem:": "carro exluido com sucesso"})



app.run(port=5000, host='localhost')