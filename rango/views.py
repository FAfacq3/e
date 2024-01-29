from django.shortcuts import render
from .models import MyModel
from rango.models import Category
# Create your views here.
from django.http import HttpResponse


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict = ['boldmessage']= 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)


def my_view(request):
    data = MyModel.objects.all()
    return render(request, 'my_template.html', {'data': data})
