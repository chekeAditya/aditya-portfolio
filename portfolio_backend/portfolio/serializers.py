from rest_framework import serializers
from .models import Project, Skill


# Converts database objects ↔ JSON Android Equivalent: Like Gson/Moshi converters in Retrofit Background: Handles all the JSON parsing automatically
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
