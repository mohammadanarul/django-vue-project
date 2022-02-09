from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Account

class AccountRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = Account.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        password1 = validated_data['password1']
        password2 = validated_data['password2']
        
        if password1 != password2:
            raise serializers.ValidationError({"password": "Password didn't match."})
        user.set_password(password1)
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
    