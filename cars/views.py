
from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model_year')#com o sinal de menos antes do model inverte a seleção
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__contains=search)
# outra opção abaixo para o codigo
#Car.objects.filter(model__contains=search) if search else Car.objects.all() 


    return render(request,'cars.html',{'cars': cars})
