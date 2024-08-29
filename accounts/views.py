
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})







# def register_view(request):
#     if request.method == "POST":
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('car_list')
#         else:
#             return render(request, 'register.html', {'user_form': user_form})


