class EstudianteEncuesta:

    def llenar_objeto(self, tid, participant_id, firstname, lastname, email,
                 emailstatus, token, language, blacklisted, sent,
                 remindersent, remindercount, completed, usesleft, validfrom,
                 validuntil, mpid, attribute1, attribute2, attribute3,
                 attribute4, attribute5, attribute6, attribute7,
                 attribute8, attribute9, attribute10, attribute11, attribute12,
                 attribute13, attribute14, attribute15, attribute16
                 ):
        self.tid = tid
        self.participant_id = participant_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.emailstatus = emailstatus
        self.token = token
        self.language = language
        self.blacklisted = blacklisted
        self.sent = sent
        self.remindersent = remindersent
        self.remindercount = remindercount
        self.completed = completed
        self.usesleft = usesleft
        self.validfrom = validfrom
        self.validuntil = validuntil
        self.mpid = mpid
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.attribute5 = attribute5
        self.attribute6 = attribute6
        self.attribute7 = attribute7
        self.attribute8 = attribute8
        self.attribute9 = attribute9
        self.attribute10 = attribute10
        self.attribute11 = attribute11
        self.attribute12 = attribute12
        self.attribute13 = attribute13
        self.attribute14 = attribute14
        self.attribute15 = attribute15
        self.attribute16 = attribute16



    @classmethod
    def obtener_json(cls, row):

        if row[14]:
            row[14]=row[14].isoformat()

        if row[15]:
            row[15]=row[15].isoformat()

        return {'estudiante': {
            'tid': row[0],
            'participant_id': row[1],
            'firstname': row[2],
            'lastname': row[3],
            'email': row[4],
            'emailstatus': row[5],
            'token': row[6],
            'language': row[7],
            'blacklisted': row[8],
            'sent': row[9],
            'remindersent': row[10],
            'remindercount': row[11],
            'completed': row[12],
            'usesleft': row[13],
            'validfrom': row[14],
            'validuntil': row[15],
            'mpid': row[16],
            'attribute1': row[17],
            'attribute2': row[18].isoformat(),
            'attribute3': row[19],
            'attribute4': row[20],
            'attribute5': row[21],
            'attribute6': row[22],
            'attribute7': row[23],
            'attribute8': row[24],
            'attribute9': row[25],
            'attribute10': row[26],
            'attribute11': row[27],
            'attribute12': row[28],
            'attribute13': row[29],
            'attribute14': row[30],
            'attribute15': row[31],
            'attribute16': row[32]
        }
        }
