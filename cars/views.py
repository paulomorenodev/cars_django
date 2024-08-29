
from django.shortcuts import render, redirect
from cars.forms import CarForm
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model_year')#com o sinal de menos antes do model inverte a seleção
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__contains=search)
# outra opção abaixo para o codigo
#Car.objects.filter(model__contains=search) if search else Car.objects.all() 

    return render(request,'cars.html',{'cars': cars})

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        #print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(request, 'new_car.html', { 'new_car_form' : new_car_form})