from django.urls import path
from apps.posts.views import AdditionalCoursesAPIView, AwardsAPIView

urlpatterns = [
    path('add_courses/', AdditionalCoursesAPIView.as_view()),
    path('awards/', AwardsAPIView.as_view()),
]