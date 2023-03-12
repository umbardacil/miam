from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Map
from api.serializers import MapSerializer

class MapList(APIView):
  def get(self, request, format=None):
    # ajouter filtre utilisateur
    maps = Map.objects.all()
    serializer = MapSerializer(maps, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    serializer = MapSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MapDetail(APIView):
  def get_object(self, pk):
    try:
      return Map.objects.get(pk=pk)
    except Map.DoesNotExist:
      raise Http404
  
  def get(self, request, pk, format=None):
    map = self.get_object(pk)
    serializer = MapSerializer(map)
    return Response(serializer.data)
  
  def put(self, request, pk, format=None):
    map = self.get_object(pk)
    serializer = MapSerializer(map, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk, format=None):
    map = self.get_object(pk)
    map.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
