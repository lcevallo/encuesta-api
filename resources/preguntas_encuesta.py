import json
from http import HTTPStatus

import myconnutils
from flask_restful import Resource, reqparse
from flask import request


class PreguntasEncuestasPregrado(Resource):
    def delete(self):

        # data = request.get_json()
        # ini_string = json.dumps(data)
        # data1 = json.loads(ini_string)
        # cedula = data1['cedula']
        preguntas_encuesta = self.obtener_preguntas()
        return {
            'respuesta': preguntas_encuesta
        }

    @classmethod
    def obtener_preguntas(cls):
        connectionMysql = myconnutils.getConnectionMysql()
        cursor = connectionMysql.cursor()

        sql_duplicados = """
                                SELECT
                                  lime_survey_896925.token, COUNT(lime_survey_896925.token)
                                FROM lime_survey_896925
                                  GROUP BY token
                                HAVING COUNT(token) > 1                                
                            """

        cursor.execute(sql_duplicados)
        rows1 = cursor.fetchall()

        data = []

        for row1 in rows1:
            cedula = row1['token']
            query_para_borrar = """
                                SELECT
                                id , token, startdate
                                FROM lime_survey_896925
                                WHERE lime_survey_896925.token = %s
                                AND startdate NOT IN (
                                SELECT MAX(startdate) FROM lime_survey_896925 WHERE token = %s)                                
                            """

            cursor.execute(query_para_borrar, (cedula, cedula))
            rows = cursor.fetchall()

            for row in rows:
                if row:
                    id = row['id']
                    query_borrar_accion = """
                            DELETE
                             FROM lime_survey_896925
                            WHERE token=%s AND 
                            id = %s
                    """
                    cursor.execute(query_borrar_accion, (cedula, id))
                    connectionMysql.commit()
                    data.append(f"cedula: {cedula}, id:{id}")

        connectionMysql.close()
        return data
