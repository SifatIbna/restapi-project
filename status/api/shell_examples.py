from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

'''
    Serialize a single objects
'''

obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)

'''
    Serialize a queryset
'''

qs  =Status.objects.all()
serializer2 = StatusSerializer(qs,many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)

'''
create obj
'''

data = {"user":1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serilazer.save()

'''

update obj
'''
obj = Status.objects.first()
data = {"user":1,"content":"some new content"}
update_serializer = StatusSerializer(obj,data = data)
update_serializer.is_valid()
update_serializer.save()

'''
delete obj
'''

data = {"user":1,"content":"plese delete me"}
create_obj_serializer = StatusSerializer(data = data)
create_obj_serializer.is_valid()
create_obj=create_obj_serializer.save()
print(create_obj)
