from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIViews

from api.models import Point
from api.serializers import PointSerializer


class PointList(APIView):
  def get(self, request, format=None):
    # Appliquer filtre map
    points = Point.objects.all()
    serializer = PointSerializer(points, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    serializer = PointSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class PointDetail(APIView):
  def 
