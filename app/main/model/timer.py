from .. import db
import threading

class Timer(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_per_day = db.Column(db.Integer, nullable=False)
    first_meal_hour = db.Column(db.Integer, nullable=False)
    first_meal_minute = db.Column(db.Integer, nullable=False)
    interval_hour = db.Column(db.Integer, nullable=False)
    interval_minute = db.Column(db.Integer, nullable=False)


    