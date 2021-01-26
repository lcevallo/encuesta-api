from flask import Flask
from flask_restful import Api
from resources.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)


api.add_resource(Usuario, '/usuario/<string:token>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)