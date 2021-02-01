import myconnutils
from flask_restful import Resource, reqparse

from resources.estudiantesEkudemic import Estudiante


class EstudiantePreGrado(Resource):

    def get(self, cedula):
        # item = next((item for item in items if item['name'] == name), None)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        estudiante_eku = self.find_by_cedula_ekudemic(cedula)
        if estudiante_eku:
            return {'test': 'Si hay data'}
        else:
            self.guardar_usuario(estudiante_eku)
            estudiante_encuesta = self.obtener_x_cedula(cedula)


        return {'message': 'Usuario no encontrado'}, 404

    @classmethod
    def find_by_cedula_ekudemic(cls, cedula):
        estudianteEkudemic = Estudiante.find_by_cedula(cedula)
        if estudianteEkudemic:
            print(estudianteEkudemic[6])
            connectionMysql = myconnutils.getConnectionMysql()
            cursor = connectionMysql.cursor()

            queryEncuestas = "SELECT  `token` FROM   `lime_tokens_896925` where token = %s"
            cursor.execute(queryEncuestas, (cedula,))
            row = cursor.fetchone()

            connectionMysql.close()

            if row is None:
                return True
            else:
                return False

    @classmethod
    def obtener_x_cedula(cls,cedula):
        connectionMysql = myconnutils.getConnectionMysql()
        cursor = connectionMysql.cursor()

        queryEncuestas = "SELECT  `tid` FROM   `lime_tokens_896925` where token = %s"
        cursor.execute(queryEncuestas, (cedula,))
        row = cursor.fetchone()

        connectionMysql.close()

        if row:
            return {'usuario': {
                'tid': row['tid']
                               }
            }

    @classmethod
    def guardar_usuario(cls, row):
        connectionMysql = myconnutils.getConnectionMysql()
        cursor = connectionMysql.cursor()
        queryInsert="INSERT INTO lime_tokens_896925 (participant_id, firstname, lastname, email, emailstatus, token, language, blacklisted, sent, remindersent, remindercount, completed, usesleft, validfrom, validuntil, mpid, attribute_1, attribute_2, attribute_3, attribute_4, attribute_5, attribute_6, attribute_7, attribute_8, attribute_9, attribute_10, attribute_11, attribute_12, attribute_13, attribute_14, attribute_15, attribute_16) VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s)"
        cursor.execute(queryInsert,
                       (row[0],
                        row[1],
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




