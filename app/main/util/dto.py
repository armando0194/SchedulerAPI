from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    token_auth = api.model('token_details', {
        'token': fields.String(required=True, description='Client ID'),
    })

class FoodContainerDto:
    api = Namespace('food', description='food container related operations')

class FeedDto:
    api = Namespace('feed', description='feed related operations')

class ScheduleDto:
    api = Namespace('timer', description='timer related operations')
    schedule = api.model('schedule_details', {
        'meal_per_day': fields.Integer(required=True, description='Number of meal per day'),
        'first_meal_hour': fields.Integer(required=True, description='Hour of the first meal'),
        'first_meal_minute': fields.Integer(required=True, description='Minute of the first meal'),
        'interval_hour': fields.Integer(required=True, description='Interval hour '),
        'interval_minute': fields.Integer(required=True, description='Interval minute'),
    })