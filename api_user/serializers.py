from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Profile, FriendRequest

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','email','password')
        extra_kwargs= {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model=Profile
        fields = ('id', 'nickName', 'userPro', 'created_on', 'img')
        extra_kwargs = {'userPro': {'read_only': True}}

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id','askFrom','askTo','approved')
        extra_kwargs = {'askFrom': {'read_only': True}}