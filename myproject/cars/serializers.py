from rest_framework import serializers
from cars.models import Car

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('vin', 'user' , 'color' , 'brand' , 'car_type')

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'