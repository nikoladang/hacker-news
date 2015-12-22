from rest_framework import serializers
from .models import SavedEmbeds

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedEmbeds