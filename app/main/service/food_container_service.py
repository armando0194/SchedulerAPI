
from app.main import db
from app.main.model.food_container import FoodContainer
import json

def get_food_container_percentage():
    food_container = FoodContainer.query.all()[0]

    if food_container:
        response_object = {
            'status': 'success',
            'message': 'Food container ata was succesfully retrived',
            'data': {
                'id': food_container.id,
                'capacity': food_container.capacity,
                'percentage': food_container.food_percentage
            }
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Food container does not exists',
        }
        return response_object, 400