from ..util.fcm_handle import FCMHandler
from ..model.token import Token

def feed():
    token = Token.query.all()[0]
    client = FCMHandler(token.token)
    client.start()

    try:

        response_object = {
            'status': 'success',
            'message': 'Successfully feed dog.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 400