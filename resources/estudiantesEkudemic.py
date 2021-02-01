import myconnutils
from flask_restful import Resource, reqparse
from flask import request

from models.EstudianteEncuesta import EstudianteEncuesta


class Estudiante(Resource):

    def get(self, cedula):
        if len(cedula) < 10:
            cedula = "0" + cedula

        estudiante_row = self.find_by_cedula(cedula)
        print(estudiante_row)
        estudiante_encuesta = EstudianteEncuesta()

        if estudiante_row:
            return estudiante_encuesta.obtener_json(estudiante_row)
        return {'message': 'Estudiante no encontrado en ekudemic'}, 404

    @classmethod
    def find_by_cedula(cls, cedula):
        connection = myconnutils.getConnectionEkudemic()
        cursor = connection.cursor()

        query = "SELECT null as tid, null as participant_id, (((usu.primer_nombre) ::text || ' ' ::text) || (usu.segundo_nombre) ::text) AS firstname, (((usu.primer_apellido) ::text || ' ' ::text) || (usu.segundo_apellido) ::text) AS lastname, usu.email, 'OK' AS emailstatus, usu.identificacion AS token, 'es-MX' AS language, null AS blacklisted, 'N' AS sent, 'N' AS remindersent, 0 AS remindercount , 'N' AS completed, 10 AS usesleft, null AS validfrom, null AS validuntil, null AS mpid, public.carrera.id  as attribute_1, usu.fecha_nacimiento as attribute_2, (Select  pais.nombre  from pais where id=  usu.pais_id ) as attribute_3, usu.direccion_domicilio as attribute_4, usu.telefono_domicilio as attribute_5, usu.celular as attribute_6, (Select sexo.sexo from sexo where id= usu.sexo_id) as attribute_7, usu.primer_nombre as attribute_8, usu.segundo_nombre as attribute_9, usu.primer_apellido as attribute_10, usu.segundo_apellido as attribute_11, usu.lugar_nacimiento as attribute_12, usu.email_universidad as attribute_13, (Select provincia.nombre from provincia where id = usu.provincia_id) as attribute_14, ( SELECT ciudad.nombre FROM ciudad WHERE (ciudad.id = usu.ciudad_id) ) AS attribute_15,  carrera.nombre AS attribute_16  FROM public.malla INNER JOIN public.carrera ON (public.malla.carrera_id = public.carrera.id) INNER JOIN public.alumno_malla ON (public.malla.id = public.alumno_malla.malla_id) INNER JOIN usuario usu ON (public.alumno_malla.alumno_id = usu.id) WHERE identificacion= %s"
        cursor.execute(query, (cedula,))
        row = cursor.fetchone()

        connection.close()

        if row:
            return row
