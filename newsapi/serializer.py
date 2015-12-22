from rest_framework import serializers
from .models import SavedEmbed

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedEmbed