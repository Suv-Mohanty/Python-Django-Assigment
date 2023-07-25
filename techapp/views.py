from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def statepage(request):
    data=State.objects.all()
    return render(request,'state.html',{'data':data})

def stateform(request):
    if request.method=='GET':
        return render(request,'stateform.html')
    else:
        State(
            name=request.POST['statename']
        ).save()
        return redirect(statepage)

def updatestate(request,state_id):
    updatedata=State.objects.get(state_id=state_id)
    return render(request,'updatingstatepage.html',{'data':updatedata})

def updatingstate(request,state_id):
    updatedata=State.objects.get(state_id=state_id)
    updatedata.name=request.POST['statename']
    updatedata.save()
    return redirect(statepage)

def deletestate(request,state_id):
    updatedata=State.objects.get(state_id=state_id)
    updatedata.delete()
    return redirect(statepage)

def citypage(request):
    data=City.objects.all()
    return render(request,'city.html',{'data':data})

def cityform(request):
    states = State.objects.all()
    if request.method == 'POST':
        name = request.POST['cityname']
        state_id = request.POST['stateid']

        state = State.objects.filter(state_id=state_id).first()
        if state:
            city = City.objects.create(name=name, state_id=state)
            return redirect(citypage)
    
    return render(request, 'cityform.html', {'states': states})

def updatecity(request, city_id):
    city = get_object_or_404(City, pk=city_id)

    if request.method == 'POST':
        name = request.POST['cityname']
        state_id = request.POST['stateid']

        state = State.objects.filter(state_id=state_id).first()
        if state:
            city.name = name
            city.state_id = state
            city.save()
            return redirect(citypage)

    states = State.objects.all()
    return render(request, 'updatingcitypage.html', {'city': city, 'states': states})

def deletecity(request,city_id):
    updatedata=City.objects.get(city_id=city_id)
    updatedata.delete()
    return redirect(citypage)

def branchpage(request):
    data=Branch.objects.all()
    return render(request,'branch.html',{'data':data})

def branchform(request):
    cities = City.objects.all()
    if request.method == 'POST':
        name = request.POST['branchname']
        description = request.POST['description']
        city_id = request.POST['cityid']

        city = City.objects.filter(city_id=city_id).first()
        if city:
            branch = Branch.objects.create(name=name, description=description, city_id=city)
            return redirect(branchpage)
    
    return render(request, 'branchform.html', {'cities': cities})

def updatebranch(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)

    if request.method == 'POST':
        name = request.POST['branchname']
        description = request.POST['description']
        city_id = request.POST['cityid']

        city = City.objects.filter(city_id=city_id).first()
        if city:
            branch.name = name
            branch.description = description
            branch.city_id = city
            branch.save()
            return redirect(branchpage)

    cities = City.objects.all()
    return render(request, 'updatingbranchpage.html', {'branch': branch, 'cities': cities})

def deletebranch(request,branch_id):
    updatedata=Branch.objects.get(branch_id=branch_id)
    updatedata.delete()
    return redirect(branchpage)