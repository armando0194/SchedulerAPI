from .. import db
import threading

class Token(db.Model):
    """ Schedule Model for storing schdule related details """
    __tablename__ = "token"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), nullable=False)
    
    def set_token(self, token):
        self.token = token



    