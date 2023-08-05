import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nimble_test_task.settings')

app = Celery('Nimble_test_task')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-new-contacts': {
        'task': 'nimble.tasks.check_contacts',
        'schedule': crontab(hour='*/24'),
    },
}
