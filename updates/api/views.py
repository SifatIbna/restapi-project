import json
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Updates as UpdateModel
from .mixins import CSRFExemptMixin
from restAPI.mixins import HttpResponseMixin

class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):

    is_json = True

    def get(self, request,id ,*args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data,status=400)

    def post(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data,status=400)


    def put(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data,status=400)
 #json

    def delete(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data,status=400)


class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):

    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self,request,*args, **kwargs):
        
        data = json.dumps({'content' : 'Nothing is real'})
        return self.render_to_response(data,status=400)

    def delete(self,request,*args, **kwargs):
        
        data = json.dumps({'content' : 'You can not delte an entire list'})
        status_code =403
        return self.render_to_response(data,status=status_code)
