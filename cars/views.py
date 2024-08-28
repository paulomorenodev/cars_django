from django.http import HttpResponse
from django.shortcuts import render
import os
from pathlib import Path

#url = Path(r'C:\Users\Paulo Moreno\Documents\Python\carros\cars\index.html')
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cars Site</title>
</head>
<body>
    <h1>Paulo Moreno Show</h1>
    <h2>Sistema de Carros</h2>
    <p>bla bla bla bla bla</p>

</body>
</html>
'''

def cars_view(request):
    return HttpResponse(html)