from rest_framework import generics, viewsets
from apps.posts.models import News, AdditionalCourses, Media, Awards, Professions, Contact
from apps.posts.serializers import NewsSerializer, AdditionalCoursesSerializer, MediaSerializer, AwardsSerializer, ProfessionsSerializer, ContactSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
class ProfessionsViewSet(viewsets.ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer
    
class AdditionalCoursesAPIView(generics.CreateAPIView):
    queryset = AdditionalCourses.objects.all()
    serializer_class = AdditionalCoursesSerializer
    
class AwardsAPIView(generics.CreateAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer