from rest_framework import generics, viewsets
from apps.users.models import Team, Students, Parents, Stakeholder
from apps.users.serializers import TeamSerializer, StudentsSerializer, ParentsSerializer, StakeholderSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
class ParentsAPIView(generics.CreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    
class StakeholderViewSet(viewsets.ModelViewSet):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer