from flask import request
from flask_restplus import Resource
from ..util.dto import ScheduleDto
from ..service.schdeule_service import get_next_schedule, set_schedule

from ..util.decorator import token_required

api = ScheduleDto.api
_schedule = ScheduleDto.schedule

@api.route('/')
class Schedule(Resource):

    @api.doc('Set timer for the food container')
    @api.expect(_schedule, validate=True)
    @token_required
    def post(self):
        """ Saves timer and runs thread """
        data = request.json
        return set_schedule(data=data)
    
    @token_required
    def get(self):
        return get_next_schedule()