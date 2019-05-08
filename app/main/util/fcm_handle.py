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
        api_key = 'AAAAk7lGlsY:APA91bFoHT7RYJUZhlV-dK_GuxqloWB-UswAq3AIpxPVkzia3Ng43xImFUYCR_9UIxWmkk8G_Z3ZJjucwZ43E4Ba_93t_s18-MhL28izDN7Z13gmFDZokGF4W0q5_oRbO_r-gPp-zxxo'
      
        push_service = FCMNotification(api_key=api_key)
        # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
        message_title = "Happy Paw"
        message_body = "Your dog was fed :)"
        result = push_service.notify_single_device(registration_id=self.registration_id, message_title=message_title, message_body=message_body)
        # print(result)

# class FCMHandler():
     
#     @staticmethod
#     def send_notification(registration_id):
#         api_key = 'AAAAk7lGlsY:APA91bFoHT7RYJUZhlV-dK_GuxqloWB-UswAq3AIpxPVkzia3Ng43xImFUYCR_9UIxWmkk8G_Z3ZJjucwZ43E4Ba_93t_s18-MhL28izDN7Z13gmFDZokGF4W0q5_oRbO_r-gPp-zxxo'
      
#         push_service = FCMNotification(api_key=api_key)

#         # OR initialize with proxies

#         proxy_dict = {
#                 "http"  : "http://127.0.0.1",
#                 "https" : "http://127.0.0.1",
#                 }
#         push_service = FCMNotification(api_key=api_key, proxy_dict=proxy_dict)

#         # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
#         message_title = "Happy Paw"
#         message_body = "Your dog was feeded :)"
#         result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

