from rest_framework import serializers
from .models import Column, Task

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'title', 'order', 'project']

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("El título de la columna debe tener al menos 2 caracteres.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'column', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título de la tarea debe tener al menos 5 caracteres.")
        return value

    def validate(self, data):
        if 'title' in data and 'description' in data:
            if data['title'] == data['description']:
                raise serializers.ValidationError("El título y la descripción de la tarea no pueden ser iguales.")
        return data
