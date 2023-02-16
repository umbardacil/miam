from django_rest import serializers

from api.models import Points


class PointSerializer(serializer.ModelSerializer):
  class Meta:
    model = Points
    fields = ["id", "name", "address", "description", "type", "map"]
