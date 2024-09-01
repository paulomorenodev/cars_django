
from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import CardModelForm


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model_year')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        return render(request,'cars.html',{'cars': cars})

class NewcarView(View):

    def get(get, request):
        new_car_form = CardModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form} )
    
    def post(self, request):
        new_car_form = CardModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form} )