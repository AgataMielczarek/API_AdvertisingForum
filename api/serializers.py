from rest_framework import serializers
from ads.models import Advertisement


class AdSerializer(serializers.ModelSerializer):
    model = Advertisement
    fields = '__all__'
    read_only_fields = ('id','user','likes')