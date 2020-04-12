

from django.urls import path

from .views import (
    StatusAPIView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)

urlpatterns = [
    
    path('',StatusAPIView.as_view()),
    # path('<int:id>/',StatusDetailAPIView.as_view()),
   
]

#/api/status
#api/status/create
#api/status/12/update
#api/status/12/delete
#api/status/12

