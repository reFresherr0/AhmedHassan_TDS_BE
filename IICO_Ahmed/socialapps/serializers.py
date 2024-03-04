from rest_framework import serializers
from .models import SocialApps

class SocialAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialApps
        fields = '__all__'
        read_only_fields = ['user']