from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'tournaments', views.TournamentViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'coachs', views.CoachViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]