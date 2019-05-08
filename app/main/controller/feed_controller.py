from flask import request
from flask_restplus import Resource
from ..util.dto import FeedDto
from ..service.feed_service import feed

from ..util.decorator import token_required

api = FeedDto.api

@api.route('/')
class Schedule(Resource):    
    @token_required
    def get(self):
        return feed()