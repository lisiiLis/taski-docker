"""asd."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """asd."""

    class Meta:
        """asd."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
