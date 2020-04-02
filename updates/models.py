from django.db import models
from django.conf import settings
# Create your models here.


class Updates(models.Model):
    User            = models.ForeignKey(settings.AUTH_USER_MODEL)
    
