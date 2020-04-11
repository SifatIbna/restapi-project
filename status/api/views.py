from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer

class StatusListSearchAPIView(APIView):
    permission_classes      = []
    authentication_classes  = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

class StatusAPIView(generics.ListAPIView):
    permission_classes      =[]
    authentication_classes  =[]
    serializer_class        = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes      =[]
    authentication_classes  =[]
    queryset                = Status.objects.all()
    serializer_class        = StatusSerializer
    
class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes      =[]
    authentication_classes  =[]
    queryset                = Status.objects.all()
    serializer_class        = StatusSerializer

    # lookup_field            ='id'

    def get_object(self, *args,**kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Status.objects.get(id=kw_id)


    '''
        in urls.py if you want to use id , you have to use lookup_field or get_object method to get the id

        or

        just use 'pk' in urls.py

    '''

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes      =[]
    authentication_classes  =[]
    queryset                = Status.objects.all()
    serializer_class        = StatusSerializer
    lookup_field            ='id'

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes      =[]
    authentication_classes  =[]
    queryset                = Status.objects.all()
    serializer_class        = StatusSerializer
    lookup_field            ='id'