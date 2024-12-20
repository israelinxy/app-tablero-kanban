from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at', 'updated_at']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del proyecto debe tener al menos 3 caracteres.")
        return value

    def validate(self, data):
        if 'name' in data and 'description' in data:
            if data['name'] == data['description']:
                raise serializers.ValidationError("El nombre y la descripción del proyecto no pueden ser iguales.")
        return data