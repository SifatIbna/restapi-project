import json
from django.views.generic import View
from django.http import HttpResponse

from updates.forms import UpdateModelForm
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
        data =json.dumps({"message":"not allowed, please use the api/update endpoint"})
        return self.render_to_response(data,status=403)


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
        # print(request.POST)
        form = UpdateModelForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data,status=201)

        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)

        data = {"message":"Not Allowed"}
        return self.render_to_response(data,status=400)

    def delete(self,request,*args, **kwargs):
        
        data = json.dumps({'content' : 'You can not delte an entire list'})
        status_code =403
        return self.render_to_response(data,status=status_code)
