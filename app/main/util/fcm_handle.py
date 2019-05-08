# Send to single device.
from pyfcm import FCMNotification
import threading

class FCMHandler(threading.Thread):

    def __init__(self, registration_id):
        super(FCMHandler, self).__init__()
        self._stop_event = threading.Event()
        self.registration_id = registration_id
        
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        api_key = ''
        push_service = FCMNotification(api_key=api_key)
        # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
        message_title = "Happy Paw"
        message_body = "Your dog was fed :)"
        result = push_service.notify_single_device(registration_id=self.registration_id, message_title=message_title, message_body=message_body)

