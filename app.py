from flask import Flask
from flask_restful import Api
from resources.usuarioPostGrado import UsuarioPostGrado
from resources.estudiantesEkudemic import Estudiante
from resources.estudiantePregrado import EstudiantePreGrado

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

api.add_resource(UsuarioPostGrado, '/usuario/<string:token>')
api.add_resource(Estudiante, '/estudiante/<string:cedula>')
api.add_resource(EstudiantePreGrado,'/estudiante-pregrado/<string:cedula>' )

if __name__ == '__main__':
    app.run(port=5000, debug=True)
