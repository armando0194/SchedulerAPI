from .. import db
import threading

class Schedule(db.Model):
    """ Schedule Model for storing schdule related details """
    __tablename__ = "schedule"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_per_day = db.Column(db.Integer, nullable=False)
    first_meal_hour = db.Column(db.Integer, nullable=False)
    first_meal_minute = db.Column(db.Integer, nullable=False)
    interval_hour = db.Column(db.Integer, nullable=False)
    interval_minute = db.Column(db.Integer, nullable=False)

    def set_meal_per_day(self, meal_per_day):
        self.meal_per_day = meal_per_day
    
    def set_first_meal_hour(self, first_meal_hour):
        self.first_meal_hour = first_meal_hour
    
    def set_first_meal_minute(self, first_meal_minute):
        self.first_meal_minute = first_meal_minute

    def set_interval_hour(self, interval_hour):
        self.interval_hour = interval_hour
    
    def set_interval_minute(self, interval_minute):
        self.interval_minute = interval_minute


    