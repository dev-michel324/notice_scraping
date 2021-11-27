from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField

# Create your models here.
CHOICES = (
    ('technology','technology'),
    ('health', 'health'),
    ('economy', 'economy'),
    ('science', 'science'),
)

class Notice(models.Model):
    category = models.CharField(choices=CHOICES, max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    date = DateTimeField(auto_now_add=True)
    date_post = models.CharField(max_length=155)

    def __str__(self):
        return self.title