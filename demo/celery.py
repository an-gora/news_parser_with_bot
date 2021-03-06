import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.signals import worker_ready

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

app = Celery('demo')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# @worker_ready.connect
# def at_start(sender, **k):
#     with sender.app.connection() as conn:
#          sender.app.send_task('news.tasks.start_bot',connection=conn)



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'add-every-15-seconds': {
        'task': 'news.tasks.update_news_base',
        'schedule': 60.0,
        'args': ()
    },
}

# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'news.tasks.update_news_base',
#         'schedule': crontab(hour=10, minute=5,),
#         'args': (),
#     },
# }

# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'news.tasks.update_news_base',
#         'schedule': 60.0,
#     },
# }

app.conf.timezone = 'UTC'
