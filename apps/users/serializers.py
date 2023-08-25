from rest_framework import serializers
from apps.users.models import Team, Students, Parents, Stakeholder

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("__all__")
        
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("__all__")
        
class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ("__all__")
        
class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = ("__all__")
        
        