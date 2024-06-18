from rest_framework import serializers
from pydantic import ValidationError
from datetime import datetime

from .models import User
from .schemas import CreateUserSchema

class CreateUserSerializer (serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = [
            "type_id", "status_id", 'user_name', 'first_name', 'last_name', 
            'email', 'phone', 'ci','password', 'address', 'birthdate'
            ]
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def validate(self, attrs):
        
        try:
            
            valid_data = CreateUserSchema(**attrs)
            
            if User.objects.filter(user_name= valid_data.user_name):
                raise serializers.ValidationError({'user_name': 'user_name already exists'})
            
            if User.objects.filter(email= valid_data.email):
                raise serializers.ValidationError({'email': 'email already exists'})
            
            if User.objects.filter(phone= valid_data.phone):
                raise serializers.ValidationError({'phone': 'phone already exists'})
            
            if User.objects.filter(ci= valid_data.ci):
                raise serializers.ValidationError({'ci': 'ci already exists'})
            
            # validate age, must be over 16 years old
            birthdate = valid_data.birthdate
            today = datetime.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            
            if age < 16:
                raise serializers.ValidationError({'age': 'the user must be over 16 years old'})
            
        except ValidationError as e:
            raise serializers.ValidationError(e)
        
        return attrs