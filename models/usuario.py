from extensions import db


class User(db.Model):
    __tablename__ = "lime_tokens_782729"

    tid = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.String(50))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    email = db.Column(db.String())
    emailstatus = db.Column(db.String())
    token = db.Column(db.String(35))
    language = db.Column(db.String(25))
    blacklisted = db.Column(db.String(17))
    sent = db.Column(db.String(25))
    remindersent = db.Column(db.String(17))
    remindercount = db.Column(db.Integer)
    completed = db.Column(db.String(17))
    usesleft = db.Column(db.Integer)
    validfrom = db.Column(db.DateTime())
    validuntil = db.Column(db.DateTime())
    mpid = db.Column(db.Integer)

    @classmethod
    def get_by_username(cls, token):
        return cls.query.filter_by(token=token).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
