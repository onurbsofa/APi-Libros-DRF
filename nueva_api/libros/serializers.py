from rest_framework import serializers
from.models import Libro
from django.contrib.auth.models import User

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields="__all__"
        read_only_fields = (
            "id", 
            "created_at",
            "updated_at"
        )
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    libros = serializers.PrimaryKeyRelatedField(many=True, queryset=Libro.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username','libros')