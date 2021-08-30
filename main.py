from flask import Flask, request, json
from flask_restful import Resource, Api
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0,
     'nome': 'Jacob',
     'habilidades': ['Python','Flask']
     },

    {'id': 1,
     'nome': 'Franco',
     'habilidades': ['Python','Django']}
]


# Criando GET, PUT, DELETE---->
"""Criando a rota pelo app,route e o método DEV, para testar três ops
GET (Recuperar dev pelo id) - PUT (Alterar configs de devs pelo id) - 
DELETE ('Excluir devs pelo id')"""

class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]

            # Levantando a excessão de erros quando o id não está na lista de devs
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}

            # Levantando a excessão de erros  quaisquer
        except Exception:
            mensagem = 'Erro desconhecido. procure o adm da API'
            response = {'staus': 'erro', 'mensagem': mensagem}

            # Se não houver erros, retornará o dev
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados


    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso', 'mensagem': 'Registro excluído com sucesso'}


# Criando POST e GET ---->
"""Criando a rota pelo app,route e o método lista_devs para testar a op
POST (Listar todos os devs e registrar mais devs)"""

class Lista_Desenvolvedores(Resource):

    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)

        return desenvolvedores

# Registrando as apis
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run()