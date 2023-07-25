from .models import *
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):
    state_id=serializers.ReadOnlyField()
    class Meta:
        model=State
        fields='__all__'

class CitySerializer(serializers.ModelSerializer):
    city_id=serializers.ReadOnlyField()
    class Meta:
        model=City
        fields='__all__'

class BranchSerializer(serializers.ModelSerializer):
    branch_id=serializers.ReadOnlyField()
    class Meta:
        model=Branch
        fields='__all__'