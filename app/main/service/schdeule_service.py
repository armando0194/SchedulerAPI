import uuid
import datetime
import time

from app.main import db
from app.main.model.schedule import Schedule
from app.main.util.fcm_handle import FCMHandler
from app.main.model.token import Token

import threading
import time
import schedule

class Scheduler(threading.Thread):

    def __init__(self, sched, token):
        super(Scheduler, self).__init__()
        self._stop_event = threading.Event()
        self.sched = sched
        self.jobs = []
        self.token = token
        self.set_up_schedule()
        
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def set_up_schedule(self):
        schedule.clear()
        meal_per_day = self.sched.meal_per_day    
        
        curr_hour = self.sched.first_meal_hour
        curr_minute = self.sched.first_meal_minute
        self.scheule_specific_time(curr_hour, curr_minute)
        
        for _ in range(meal_per_day - 1): 
            minutes = curr_minute + self.sched.interval_minute
            curr_hour += self.sched.interval_hour + (minutes / 60)
            curr_minute = minutes % 60
            self.scheule_specific_time(curr_hour, curr_minute)

    def scheule_specific_time(self, h, m):
        print ("{:02d}:{:02d}".format(h, m))
        self.jobs.append({"h":h, "m":m})
        print(self.jobs)
        schedule.every().day.at("{:02d}:{:02d}".format(h, m)).do(self.feed)

    def feed(self):
        print("feed")

    def run(self):
        while(True):
            seconds = (schedule.next_run() - datetime.datetime.now() ).total_seconds() 
            time.sleep(seconds)
            schedule.run_pending()
            client = FCMHandler(self.token)
            client.start()                                    

scheduler = None

def set_schedule(data):
    global scheduler
    sched = Schedule.query.all()[0]
    token = Token.query.all()[0]
    if sched:
        sched.set_meal_per_day(data['meal_per_day'])
        sched.set_first_meal_hour(data['first_meal_hour'])
        sched.set_first_meal_minute(data['first_meal_minute'])
        sched.set_interval_hour(data['interval_hour'])
        sched.set_interval_minute(data['interval_minute'])

        db.session.add(sched)
        db.session.commit()

        if scheduler is not None:
            scheduler.stop()
        
        scheduler = Scheduler(sched, token.token) 
        scheduler.start()

        response_object = {
            'status': 'success',
            'message': 'Schedule was updated',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Schedule could not be updated',
        }
        return response_object, 400

def get_next_schedule():
    sched = Schedule.query.all()[0]
    if scheduler is not None:
        response_object = {
            'status': 'success',
            'message': 'Success next run retrived',
            'data': {
                'next_feed_time': time.mktime(schedule.next_run().timetuple()) * 1000.0,
                'meal_per_day': sched.meal_per_day
            }
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Scheduler is not running',
        }
        return response_object, 400

# def get_next_schedule():

#     if scheduler is not None:
#         response_object = {
#             'status': 'Success',
#             'message': 'Schedule was updated',
#             'data':  scheduler.next_run()
#         }
#         return response_object, 200
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'Scheduler is not running',
#         }
#         return response_object, 408

# def save_changes(data):
#     db.session.add(data)    
#     db.session.commit()

