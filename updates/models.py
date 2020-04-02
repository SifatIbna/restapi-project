from django.conf import settings
from django.db import models

# Create your models here.


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)


class Update(models.Model):
    User            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,)
    content         = models.TextField()
    image           = models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content or ""
