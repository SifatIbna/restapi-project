from django.contrib import admin

from .forms import StatusForm
from .models import Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user','__str__','image']
    form = StatusForm
    
admin.site.register(Status)
