from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

ALL_STATUS = [
    ('start', 'Start'),
    ('in_process', 'In process'),
    ('is_finished', 'Is finished')
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=127, default='')
    description = models.TextField(max_length=1027, default='')
    dead_line = models.DateTimeField()
    status = models.CharField(choices=ALL_STATUS, default='Start', max_length=127)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.title)