from rest_framework.viewsets import ModelViewSet

from drf_jgp.polls.api.serializers import PollSerializer
from drf_jgp.polls.models import Poll


class PollModelViewSet(ModelViewSet):
    serializer_class=PollSerializer
    queryset=Poll.objects.all()
    http_method_names= ["get", "post", "delete", "put"]
