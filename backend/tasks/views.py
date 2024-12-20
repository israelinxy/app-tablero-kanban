from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Column, Task
from .serializers import ColumnSerializer, TaskSerializer
from .permissions import IsProjectOwnerOrReadOnly
from projects.models import Project
from .pagination import CustomPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['project', 'title']
    ordering_fields = ['order', 'title']
    pagination_class = CustomPagination

    @extend_schema(
        description="List all columns",
        parameters=[
            OpenApiParameter(name="project", description="Filter by project ID", required=False, type=int),
            OpenApiParameter(name="title", description="Filter by column title", required=False, type=str),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Create a new column")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Retrieve a specific column")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(description="Update a column")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Partially update a column")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(description="Delete a column")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        description="Get columns by project",
        parameters=[
            OpenApiParameter(name="project_id", description="Project ID", required=True, type=int),
        ],
        responses={200: ColumnSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def by_project(self, request):
        project_id = request.query_params.get('project_id')
        if project_id:
            columns = Column.objects.filter(project_id=project_id)
            serializer = self.get_serializer(columns, many=True)
            return Response(serializer.data)
        return Response({"error": "project_id is required"}, status=400)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['column', 'title']
    ordering_fields = ['created_at', 'updated_at', 'title']
    pagination_class = CustomPagination

    @extend_schema(
        description="List all tasks",
        parameters=[
            OpenApiParameter(name="column", description="Filter by column ID", required=False, type=int),
            OpenApiParameter(name="title", description="Filter by task title", required=False, type=str),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Create a new task")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Retrieve a specific task")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(description="Update a task")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Partially update a task")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(description="Delete a task")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        description="Get tasks by project",
        parameters=[
            OpenApiParameter(name="project_id", description="Project ID", required=True, type=int),
        ],
        responses={200: TaskSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def by_project(self, request):
        project_id = request.query_params.get('project_id')
        if project_id:
            tasks = Task.objects.filter(column__project_id=project_id)
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)
        return Response({"error": "project_id is required"}, status=400)

    @extend_schema(
        description="Move a task to a new column",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'new_column_id': {'type': 'integer'}
                },
                'required': ['new_column_id']
            }
        },
        responses={200: {'type': 'object', 'properties': {'message': {'type': 'string'}}}}
    )
    @action(detail=True, methods=['POST'])
    def move(self, request, pk=None):
        task = self.get_object()
        new_column_id = request.data.get('new_column_id')
        if new_column_id:
            new_column = get_object_or_404(Column, id=new_column_id)
            task.column = new_column
            task.save()
            return Response({"message": "Task moved successfully"})
        return Response({"error": "new_column_id is required"}, status=400)
