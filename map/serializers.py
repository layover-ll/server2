from .models import Marker
from rest_framework.serializers import ModelSerializer


class MarkerSerializer(ModelSerializer):
    class Meta:
        model = Marker
        fields = "__all__"
