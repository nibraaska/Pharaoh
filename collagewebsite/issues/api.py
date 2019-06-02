from rest_framework import viewsets, permissions
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):

    queryset = Issue.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = IssueSerializer
