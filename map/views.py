from django.shortcuts import render, get_object_or_404
from .serializers import MarkerSerializer
from .models import Marker
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class MarkerView(APIView):
    def get(self, request, format=None):
        marker = Marker.objects.all()
        serializer = MarkerSerializer(marker, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MarkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Marker.objects.get(pk=pk)
        except Marker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        marker = self.get_object(pk)
        serializer = MarkerSerializer(marker)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        marker = self.get_object(pk)
        serializer = MarkerSerializer(marker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erroes, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        marker = self.get_object(pk)
        marker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
