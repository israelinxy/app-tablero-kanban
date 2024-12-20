from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .pagination import CustomPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'created_at']
    ordering_fields = ['name', 'created_at']
    pagination_class = CustomPagination
    
    @extend_schema(
        description="List all projects",
        parameters=[
            OpenApiParameter(name="name", description="Filter by project name", required=False, type=str),
            OpenApiParameter(name="created_at", description="Filter by creation date", required=False, type=str),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Create a new project")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Retrieve a specific project")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(description="Update a project")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Partially update a project")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(description="Delete a project")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @extend_schema(
        description="List projects owned by the current user",
        responses={200: ProjectSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def my_projects(self, request):
        projects = Project.objects.filter(owner=request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
