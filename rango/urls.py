from django.urls import path
from . import views

urlpatterns = [
    path('my-data-page/', views.my_view, name='my_data_page'),
]
