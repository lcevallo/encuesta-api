import pymysql
from flask_restful import Resource, reqparse
from flask import request
from util import SplitNombres


class Usuario(Resource):
    parser = reqparse.RequestParser()

    def get(self, token):
        # item = next((item for item in items if item['name'] == name), None)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        usuario_token = self.find_by_token(token)
        if usuario_token:
            return usuario_token
        return {'message': 'Usuario no encontrado'}, 404

    def post(self, token):
        if self.find_by_token(token):
            return {'message': "An item with name '{}' already exists.".format(token)}, 400

        data = request.get_json()
        separado= SplitNombres(data['alumno'])
        print(separado)
        usuario = {
                'token': token, 'nombres': data['alumno'],
                'email': data['email']
                }

        try:
            # self.insert(item)
            return {"message": "Hola moto"}, 200
        except:
            return {"message": "An error ocurred inserting the item"}, 500

        return usuario, 201

    @classmethod
    def find_by_token(cls, token):
        connection = pymysql.connect(
            host="10.0.0.8", port=3306, user="lcevallosc",
            charset='utf8mb4',
            passwd="Ulaica2019-", db="db_lime_276",
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connection.cursor()

        query = "SELECT `tid`,`participant_id`,`firstname`,`lastname`,`email`,`token`,`usesleft` from `lime_tokens_782729` WHERE `token`= %s "
        cursor.execute(query, (token,))
        row = cursor.fetchone()
        print(row)

        connection.close()

        if row:
            return {'usuario': {
                'tid': row['tid'], 'participant_id': row['participant_id'],
                'firstname': row['firstname'], 'lastname': row['lastname'],
                'email': row['email'], 'token': row['token'],
                'usesleft': row['usesleft']
            }}

    @classmethod
    def insert(cls, usuario):
        connection = pymysql.connect(
            host="10.0.0.8", port=3306, user="lcevallosc",
            charset='utf8mb4',
            passwd="Ulaica2019-", db="db_lime_276",
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connection.cursor()

        query = "INSERT INTO `lime_tokens_782729` (`firstname`, `lastname`, `email`, `emailstatus`, `token`, `language`, `sent`, `remindersent`, `remindercount`, `completed`, `usesleft`) VALUES (?, ?, ?, 'OK', ?, 'es-MX', 'N', 'N', 0, 'N', 10)"
        cursor.execute(query, (usuario['firstname'],
                               usuario['lastname'],
                               usuario['email'],
                               usuario['token']
                               ))

        connection.commit()
        connection.close()
