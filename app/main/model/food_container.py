from .. import db


class FoodContainer(db.Model):
    """ FoodContainer Model for storing user related details """
    __tablename__ = "food_container"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_percentage = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=True)
    last_filled = db.Column(db.DateTime, nullable=False)