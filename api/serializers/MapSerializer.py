from rest_framework import serializers

from api.models import Maps


class MapSerializer(serializers.Serializer):
  class Meta:
    model = Maps
    fields = ["id", "name", "owner", "editors", "viewers"]
