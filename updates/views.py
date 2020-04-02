from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from restAPI.mixins import JsonResponseMixin

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




class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
        "count":100,
        "content": "Some new content",
        }

        return self.render_to_json_response(data)