from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('projects', views.ProjectViewSet)

# Maps URLs to functions Android Equivalent: Like Retrofit's @GET("/api/projects") Background: Django's router that directs traffic
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/profile/', views.get_profile),
]