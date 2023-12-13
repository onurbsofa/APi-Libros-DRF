from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libros import views


router = DefaultRouter()
router.register(r'libros', views.LibroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]