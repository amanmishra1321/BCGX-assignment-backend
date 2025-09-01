from rest_framework.serializers import ModelSerializer, Serializer
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields =("id", "email", "phone_no")

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_no", "password")
        extra_kwargs = {"password":{"write_only":True}}
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
        
      
class LoginUserSerializer(Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            print("Valid",user)
            return user
        
        raise serializers.ValidationError("Incorrect credentials!")
        
        
    
    