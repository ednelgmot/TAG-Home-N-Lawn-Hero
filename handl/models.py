from django.db import models
from django.contrib.auth.models import User

# Use to classify an event type
EVENT_CHOICES = (
    ('S', 'Seasonal'),
    ('A', 'Annual'),
    ('M', 'Maintenance'),
)

# Use to create multiple instances of an event/task
REPEAT_CHOICES =  (
    ('Y','Yes'),
    ('N','No'),
)

MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    tasktype = models.CharField('Type of Task',max_length=2, choices=EVENT_CHOICES, null=True, blank=True,
                                            help_text="Classify the event")
    repeatevent = models.CharField('Task repeats?', max_length=2, choices=REPEAT_CHOICES, null=True, blank=True,
                                            help_text="Select if the event repeats or not")
    moyval = models.CharField('Month it repeats',max_length=9, choices=MONTH_CHOICES, null=True, blank=True,
                                            help_text="Select Month event repeats in")
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'   