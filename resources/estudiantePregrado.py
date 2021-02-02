import json
from http import HTTPStatus

import myconnutils
from flask_restful import Resource, reqparse
from flask import request

from models.EstudianteEncuesta import EstudianteEncuesta
from resources.estudiantesEkudemic import Estudiante


class EstudiantePreGrado(Resource):

    def get(self, cedula):
        # item = next((item for item in items if item['name'] == name), None)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        estudiante_encuesta = self.obtener_x_cedula(cedula)
        if estudiante_encuesta:
            return {'estudiante': estudiante_encuesta}, HTTPStatus.OK
        else:
            return {'message': 'Usuario no encontrado'}, 404

    def post(self, cedula):
        if len(cedula) < 10:
            cedula = "0" + cedula

        estudiante_eku = self.find_by_cedula_ekudemic(cedula)
        if estudiante_eku:

            self.guardar_usuario(estudiante_eku)
            estudiante_encuesta = self.obtener_x_cedula(cedula)
            if estudiante_encuesta:
                return {estudiante_encuesta}, 201

        else:
            return {'info': 'Ya existe en el sistema de encuestas'}

    @classmethod
    def find_by_cedula_ekudemic(cls, cedula):
        estudianteEkudemic = Estudiante.find_by_cedula(cedula)
        if estudianteEkudemic:
            connectionMysql = myconnutils.getConnectionMysql()
            cursor = connectionMysql.cursor()

            queryEncuestas = "SELECT  `token` FROM   `lime_tokens_896925` where token = %s"

            cursor.execute(queryEncuestas, (estudianteEkudemic[6],))
            row = cursor.fetchone()

            connectionMysql.close()

            if row is None:
                return estudianteEkudemic
            else:
                return None
        else:
            return None

    @classmethod
    def obtener_x_cedula(cls, cedula):
        connectionMysql = myconnutils.getConnectionMysql()
        cursor = connectionMysql.cursor()

        queryEncuestas = "SELECT  * FROM `lime_tokens_896925` where token = %s"

        cursor.execute(queryEncuestas, (cedula,))

        columns = cursor.description
        result = ""
        data = []
        row = cursor.fetchone()
        if row:
            estudianteEnc = EstudianteEncuesta(
                row['tid'],
                row['participant_id'],
                row['firstname'],
                row['lastname'],
                row['email'],
                row['emailstatus'],
                row['token'],
                row['language'],
                row['blacklisted'],
                row['sent'],
                row['remindersent'],
                row['remindercount'],
                row['completed'],
                row['usesleft'],
                row['validfrom'],
                row['validuntil'],
                row['mpid'],
                row['attribute_1'],
                row['attribute_2'],
                row['attribute_3'],
                row['attribute_4'],
                row['attribute_5'],
                row['attribute_6'],
                row['attribute_7'],
                row['attribute_8'],
                row['attribute_9'],
                row['attribute_10'],
                row['attribute_11'],
                row['attribute_12'],
                row['attribute_13'],
                row['attribute_14'],
                row['attribute_15'],
                row['attribute_16']
            )
            data.append(estudianteEnc.data)

            # result = "{"
            # for i in range(len(columns)):
            #     if i == len(columns) - 1:
            #         registro_json = '"' + str(columns[i][0]) + '":' + str(row[columns[i][0]])
            #     else:
            #         registro_json = '"' + str(columns[i][0]) + '":' + str(row[columns[i][0]]) + ","
            #
            #     result = result + registro_json
            #
            # result = result + "}"

        connectionMysql.close()
        return data

    @classmethod
    def guardar_usuario(cls, row):
        connectionMysql = myconnutils.getConnectionMysql()
        cursor = connectionMysql.cursor()

        queryInsert = "INSERT INTO lime_tokens_896925 (participant_id, firstname, lastname, email, emailstatus, token, language, blacklisted, sent, remindersent, remindercount, completed, usesleft, validfrom, validuntil, mpid, attribute_1, attribute_2, attribute_3, attribute_4, attribute_5, attribute_6, attribute_7, attribute_8, attribute_9, attribute_10, attribute_11, attribute_12, attribute_13, attribute_14, attribute_15, attribute_16) VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s)"

        cursor.execute(queryInsert,
                       (row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                        row[14],
                        row[15],
                        row[16],
                        row[17],
                        row[18],
                        row[19],
                        row[20],
                        row[21],
                        row[22],
                        row[23],
                        row[24],
                        row[25],
                        row[26],
                        row[27],
                        row[28],
                        row[29],
                        row[30],
                        row[31],
                        row[32]
                        )
                       )
        connectionMysql.commit()
        connectionMysql.close()


class EstudiantesPreGradoResource(Resource):
    def get(self):
        estudiantes_pregrado_list = self.obtener_estudiantes_encuestas()
        return {'estudiantes': estudiantes_pregrado_list}, HTTPStatus.OK

    def post(self):

        data = request.get_json()
        ini_string = json.dumps(data)
        data1 = json.loads(ini_string)
        respuesta = self.guardar_estudiantes_encuestas(data1['cedulas'])
        return respuesta

    @classmethod
    def guardar_estudiantes_encuestas(cls, cedulas):

        data = []
        cedula_list = []
        ya_existentes = []
        cedulas_buscar = []
        data_final = []
        for cedula in cedulas:
            cedula_text = str(cedula)
            if len(cedula_text) < 10:
                cedula_text = "0" + str(cedula_text)

            cedulas_buscar.append(cedula_text)

            estudiante_encuesta = EstudiantePreGrado.find_by_cedula_ekudemic(cedula_text)
            if estudiante_encuesta:
                data.append(estudiante_encuesta)
                cedula_list.append(cedula_text)
            else:
                ya_existentes.append({"mensaje": "{} ya esta en la base de datos de encuesta".format(cedula_text)})

        if data:

            connectionMysql = myconnutils.getConnectionMysql()
            cursor = connectionMysql.cursor()

            queryInsert = "INSERT INTO lime_tokens_896925 (participant_id, firstname, lastname, email, emailstatus, token, language, blacklisted, sent, remindersent, remindercount, completed, usesleft, validfrom, validuntil, mpid, attribute_1, attribute_2, attribute_3, attribute_4, attribute_5, attribute_6, attribute_7, attribute_8, attribute_9, attribute_10, attribute_11, attribute_12, attribute_13, attribute_14, attribute_15, attribute_16) VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s)"
            for row in data:
                cursor.execute(queryInsert,
                               (row[1],
                                row[2],
                                row[3],
                                row[4],
                                row[5],
                                row[6],
                                row[7],
                                row[8],
                                row[9],
                                row[10],
                                row[11],
                                row[12],
                                row[13],
                                row[14],
                                row[15],
                                row[16],
                                row[17],
                                row[18],
                                row[19],
                                row[20],
                                row[21],
                                row[22],
                                row[23],
                                row[24],
                                row[25],
                                row[26],
                                row[27],
                                row[28],
                                row[29],
                                row[30],
                                row[31],
                                row[32]
                                )
                               )
                connectionMysql.commit()

            for cedula in cedula_list:
                queryEncuestas = "SELECT  * FROM `lime_tokens_896925` where token = %s"
                cursor.execute(queryEncuestas, (cedula,))

                row = cursor.fetchone()
                if row:
                    estudianteEnc = EstudianteEncuesta(
                        row['tid'],
                        row['participant_id'],
                        row['firstname'],
                        row['lastname'],
                        row['email'],
                        row['emailstatus'],
                        row['token'],
                        row['language'],
                        row['blacklisted'],
                        row['sent'],
                        row['remindersent'],
                        row['remindercount'],
                        row['completed'],
                        row['usesleft'],
                        row['validfrom'],
                        row['validuntil'],
                        row['mpid'],
                        row['attribute_1'],
                        row['attribute_2'],
                        row['attribute_3'],
                        row['attribute_4'],
                        row['attribute_5'],
                        row['attribute_6'],
                        row['attribute_7'],
                        row['attribute_8'],
                        row['attribute_9'],
                        row['attribute_10'],
                        row['attribute_11'],
                        row['attribute_12'],
                        row['attribute_13'],
                        row['attribute_14'],
                        row['attribute_15'],
                        row['attribute_16']
                    )
                    data_final.append(estudianteEnc.data)

            connectionMysql.close()
        return {'estudiantes_new': data_final,
                'ya_existentes': ya_existentes
                }

    @classmethod
    def obtener_estudiantes_encuestas(cls):
        connectionMysql = myconnutils.getConnectionMysql()
        cursor = connectionMysql.cursor()
        queryEncuestas = "SELECT * FROM `lime_tokens_896925`"

        cursor.execute(queryEncuestas)

        rows = cursor.fetchall()

        data = []

        for row in rows:
            estudianteEnc = EstudianteEncuesta(
                row['tid'],
                row['participant_id'],
                row['firstname'],
                row['lastname'],
                row['email'],
                row['emailstatus'],
                row['token'],
                row['language'],
                row['blacklisted'],
                row['sent'],
                row['remindersent'],
                row['remindercount'],
                row['completed'],
                row['usesleft'],
                row['validfrom'],
                row['validuntil'],
                row['mpid'],
                row['attribute_1'],
                row['attribute_2'],
                row['attribute_3'],
                row['attribute_4'],
                row['attribute_5'],
                row['attribute_6'],
                row['attribute_7'],
                row['attribute_8'],
                row['attribute_9'],
                row['attribute_10'],
                row['attribute_11'],
                row['attribute_12'],
                row['attribute_13'],
                row['attribute_14'],
                row['attribute_15'],
                row['attribute_16']
            )
            data.append(estudianteEnc.data)

        connectionMysql.close()
        return data