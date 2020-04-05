from django.core.serializers import serialize
from django.conf import settings
from django.db import models
import json
# Create your models here.


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        return serialize('json',qs, fields=('user','content','image','id','timestamp'))

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model,using=self._db)

class Updates(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,)
    content         = models.TextField()
    # image           = models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content

    def serialize(self):
        # return serialize("json", [self], fields=('id','content','image','timestamp')) 
        # try:
        #     image = self.image.url
        # except:
        #     image = ""

        data = {
            "id":self.pk,
            "content":self.content,
            "user":self.user_id,
            # "image":image
        }

        new_data = json.dumps(data)
        return new_data