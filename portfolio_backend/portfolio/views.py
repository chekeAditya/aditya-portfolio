from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Skill
from .serializers import ProjectSerializer, SkillSerializer

# Contains your API logic Android Equivalent: Like your Repository pattern methods Background: Processes requests and returns responses

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@api_view(['GET'])
def get_profile(request):
    """Your profile information"""
    profile_data = {
        "name": "Aditya Cheke",
        "title": "Senior Android Developer",
        "bio": "Passionate about building amazing mobile experiences",
        "email": "your-email@example.com",
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/yourusername"
    }
    return Response(profile_data)
