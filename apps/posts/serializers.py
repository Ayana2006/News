from rest_framework import serializers
from apps.posts.models import News, AdditionalCourses, Media, Awards, Professions, Contact

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("__all__")

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("__all__")
        
class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = ("__all__")
        
class AdditionalCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalCourses
        fields = ("__all__")
        
class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ("__all__")
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("__all__")