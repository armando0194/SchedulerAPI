from flask_restplus import Api
from flask import Blueprint


from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.food_container_controller import api as food_ns
from .main.controller.schedule_controller import api as schedule_ns
from .main.controller.feed_controller import api as feed_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title= "Scheduler API",
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )
scheduler = None

api.add_namespace(user_ns, path='/api/user')
api.add_namespace(auth_ns, path='/api')
api.add_namespace(food_ns, path='/api/food')
api.add_namespace(schedule_ns, path='/api/schedule')
api.add_namespace(feed_ns, path='/api/feed')