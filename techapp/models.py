from django.db import models

class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

class Branch(models.Model):
    branch_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    city_id=models.ForeignKey(City,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
