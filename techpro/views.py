from techapp.models import *
from techapp.serializers import StateSerializer,CitySerializer, BranchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes,action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StateView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,Format=None):
        queryset=State.objects.all()
        serializer_class=StateSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request,Format=None):
        serializer_class=StateSerializer(data=request.data,many=True)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Saved'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)

class StateViewID(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk,Format=None): 
        queryset=State.objects.get(pk=pk)
        serializer_class=StateSerializer(queryset)
        return Response(serializer_class.data)     

    def put(self,request,pk,Format=None):
        queryset=State.objects.get(pk=pk)
        serializer_class=StateSerializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Updated'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)
    
    def delete(self,request,pk,Format=None):
        queryset=State.objects.get(pk=pk)
        queryset.delete()
        return Response({'message':'Deleted Successfully'})

class CityView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,Format=None):
        queryset=City.objects.all()
        serializer_class=CitySerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request,Format=None):
        serializer_class=CitySerializer(data=request.data,many=True)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Saved'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)

class CityViewID(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk,Format=None): 
        queryset=City.objects.get(pk=pk)
        serializer_class=CitySerializer(queryset)
        return Response(serializer_class.data)

    def put(self,request,pk,Format=None):
        queryset=City.objects.get(pk=pk)
        serializer_class=CitySerializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Updated'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)
    
    def delete(self,request,pk,Format=None):
        queryset=City.objects.get(pk=pk)
        queryset.delete()
        return Response({'message':'Deleted Successfully'})

class BranchView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,Format=None):
        queryset=Branch.objects.all()
        serializer_class=BranchSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request,Format=None):
        serializer_class=BranchSerializer(data=request.data,many=True)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Saved'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)

class BranchViewID(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk,Format=None): 
        queryset=Branch.objects.get(pk=pk)
        serializer_class=BranchSerializer(queryset)
        return Response(serializer_class.data)

    def put(self,request,pk,Format=None):
        queryset=Branch.objects.get(pk=pk)
        serializer_class=BranchSerializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Updated'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)
    
    def delete(self,request,pk,Format=None):
        queryset=Branch.objects.get(pk=pk)
        queryset.delete()
        return Response({'message':'Deleted Successfully'})

class CityListView(APIView):
    def get(self,request,state_id):
        try:
            state=State.objects.get(pk=state_id)
            cities=City.objects.filter(state_id=state)
            serializer_class=CitySerializer(cities, many=True)
            return Response(serializer_class.data)
        except State.DoesNotExist:
            return Response({"error": "State not found"}, status=404)

class BranchListView(APIView):
    def get(self,request,city_id):
        try:
            city=City.objects.get(pk=city_id)
            queryset=Branch.objects.filter(city_id=city)
            serializer_class=BranchSerializer(queryset, many=True)
            return Response(serializer_class.data)
        except State.DoesNotExist:
            return Response({"error": "State not found"}, status=404)
