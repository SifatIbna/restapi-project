

from django.urls import path

from .views import StatusAPIView

urlpatterns = [
    
    path('',StatusAPIView.as_view()),

    # path('create/',StatusCreateAPIView.as_view()),
    # path('<int:id>/',StatusListAPIView.as_view()),
    # path('<int:id>/update/',StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/',StatusUpdateAPIView.as_view()),

]

#/api/status
#api/status/create
#api/status/12/update
#api/status/12/delete
#api/status/12

