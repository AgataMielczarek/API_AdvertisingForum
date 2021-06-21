from rest_framework import serializers
from ads.models import Advertisement
from django.contrib.auth.models import User


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ('id','user','likes')


class UserSerializer(serializers.ModelSerializer):
        ads = serializers.PrimaryKeyRelatedField(many=True, 
        queryset=Advertisement.objects.all())
        class Meta:
            model = User
            fields = ('id', 'username', 'password', 'ads')

