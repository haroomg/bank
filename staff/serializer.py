from rest_framework import serializers
from pydantic import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .schemas import CreateStaffSchema

class CreateStaffSerializer (serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    
    def validate(self, attrs):
        
        try:
            valid_data = CreateStaffSchema(**attrs)
            # ...
        except ValidationError as e:
            raise serializers.ValidationError(e)
        
        return attrs
