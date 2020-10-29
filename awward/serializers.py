from rest_framework import serializers
from .models import Project, Profile

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'