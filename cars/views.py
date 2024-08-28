
from django.shortcuts import render
from cars.models import Car

def cars_view(request):

    print(request)
    print(type(request))
    req = request.GET.get('search')
    print(req)
    print(request.GET)
    ## Sintaxe para passar parametros
    #http://localhost:8000/cars/?search=bily&name=john

    cars = Car.objects.all()

    #cars = Car.objects.filter(model__contains='opa')
    #cars = Car.objects.filter(brand__name='fiat')
    #cars = Car.objects.filter(model='kwid')
    

    return render(request,'cars.html',{'cars': cars})
