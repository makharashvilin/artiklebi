from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    create_date = models.DateField(default=datetime.now)
