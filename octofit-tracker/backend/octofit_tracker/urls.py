"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os

from .views import (
    TeamViewSet,
    UserProfileViewSet,
    ActivityViewSet,
    LeaderboardEntryViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserProfileViewSet, basename='user')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardEntryViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')
@api_view(['GET'])
def api_root(request, format=None):
    """API root that builds absolute URLs using the Codespace hostname when available.

    If the environment variable `CODESPACE_NAME` is present we return URLs
    using the Codespaces forwarded host (https://$CODESPACE_NAME-8000.app.github.dev).
    Otherwise fall back to the incoming request host/scheme.
    """
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        host = f"{codespace}-8000.app.github.dev"
        scheme = 'https'
    else:
        host = request.get_host()
        scheme = request.scheme

    def make_url(name):
        path = reverse(name, request=None, format=format)
        return f"{scheme}://{host}{path}"

    return Response({
        'teams': make_url('team-list'),
        'users': make_url('user-list'),
        'activities': make_url('activity-list'),
        'leaderboard': make_url('leaderboard-list'),
        'workouts': make_url('workout-list'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
