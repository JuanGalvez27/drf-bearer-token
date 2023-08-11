from rest_framework.serializers import ModelSerializer

from drf_jgp.polls.models import Poll, Choice

class PollSerializer(ModelSerializer):
    class Meta:
        model=Poll
        fields=["id","question"]

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model=Choice
        fiels=["question", "choice"]
        