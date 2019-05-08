from flask import request
from flask_restplus import Resource
from ..util.dto import FoodContainerDto
from ..service.food_container_service import get_food_container_percentage

from ..util.decorator import token_required

api = FoodContainerDto.api

@api.route('/')
class FoodContainerPercentage(Resource):
    
    @api.doc('returns food container percentage')
    @token_required
    def get(self):
       return get_food_container_percentage()

