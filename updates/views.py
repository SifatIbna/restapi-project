
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from restAPI.mixins import JsonResponseMixin

from .models import Updates as UpdateModel

# Create your views here.


#def detail_view(request):
    #return HttpResponse(get_template().render({})) # return JSON DATA


def json_example_view(request):
    data = {
        "count":100,
        "content": "Some new content",
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        data = {
        "count":100,
        "content": "Some new content",
        }
        return JsonResponse(data)




class SerializedDetailView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        
        obj = UpdateModel.objects.get(id=4)
        json_data = obj.serialize()
        return HttpResponse(json_data,content_type='application/json')
        


class SerializedListView(View):
    def get(self,request,*args,**kwargs):
        json_data = UpdateModel.objects.all().serialize()
        return HttpResponse(json_data,content_type='application/json')
      
