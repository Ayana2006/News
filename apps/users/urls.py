from django.urls import path
from apps.users.views import ParentsAPIView

urlpatterns = [
    path('parents/', ParentsAPIView.as_view()),
    
]