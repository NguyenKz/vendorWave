from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password1', 'password2')
        extra_kwargs = {'password1': {'write_only': True}, 'password2': {'write_only': True}}
    
    def validate_email(self,value:str):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email has already been used.")
        return value
    
    def validate_username(self,value:str):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username has already been used.")
        return value
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password2":"Passwords do not match."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']  # Use 'password1' here
        )
        return user