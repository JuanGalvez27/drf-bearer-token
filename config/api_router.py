from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from drf_jgp.users.api.views import UserViewSet
from drf_jgp.polls.api.views import PollModelViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("polls", PollModelViewSet)



app_name = "api"
urlpatterns = router.urls
