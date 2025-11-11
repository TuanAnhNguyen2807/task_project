from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

# Custom pagination class
class TaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size' 
    max_page_size = 100

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    filterset_fields = ['is_completed']
    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
