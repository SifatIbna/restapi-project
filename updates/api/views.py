import json
from django.views.generic import View
from django.http import HttpResponse

from updates.forms import UpdateModelForm
from updates.models import Updates as UpdateModel

from .mixins import CSRFExemptMixin
from restAPI.mixins import HttpResponseMixin

from .utils import is_json

class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):

    is_json = True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None

        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        
        """
        Below handles a Does not Exist Exception too
        """

    def get(self, request,id ,*args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request,id,*args, **kwargs):
        data =json.dumps({"message":"not allowed, please use the api/update endpoint"})
        return self.render_to_response(data,status=403)


    def put(self, request,id,*args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid Data Sent, please sent using JSON"})
            return self.render_to_response(error_data,status=400)



        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)

        saved_data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)

        print(passed_data)
        print(saved_data)

        for key, value in passed_data.items():
            saved_data[key] = value
    
        # json_data = json.dumps(saved_data)

        form = UpdateModelForm(saved_data,instance=obj)

        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(saved_data)
            return self.render_to_response(obj_data,status=201)

        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)

        json_data = json.dumps({"message":"Something"})
        return self.render_to_response(json_data)

    def delete(self, request,id,*args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        deleted_, item_deleted = obj.delete()
        print(deleted_)

        if deleted_ == 1:
            json_data = json.dumps({"message":"Successfully Deleted"})
            return self.render_to_response(json_data,status=200)

        data = json.dumps({"message":"Could not delete"})
        return self.render_to_response(data,status=404)


class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):

    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self,request,*args, **kwargs):
        # print(request.POST)
        # print(request.body)
        valid_json = is_json(request.body)
        print(valid_json)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid Data Sent, please sent using JSON"})
            return self.render_to_response(error_data,status=400)

        data = json.loads(request.body)
        form = UpdateModelForm(data)

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
