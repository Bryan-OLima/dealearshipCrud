from django.shortcuts import render, redirect
from crud.forms import CarsForm
from crud.models import Cars

def home(request):
    data = {}
    data['db'] = Cars.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarsForm()
    return render(request, 'form.html', data)

def about(request):
    return render(request, 'about.html')

def create(request):
    form = CarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    data['form'] = CarsForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    form = CarsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
def delete(request, pk):
    db = Cars.objects.get(pk=pk)
    db.delete()
    return redirect('home')