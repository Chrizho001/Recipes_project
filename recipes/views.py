from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Dish

# Create your views here.

class HomeView(TemplateView):
    template_name='recipes/home.html'

class Smoked_Meat_Sandwhich_DetailView(TemplateView):
    template_name= 'new_recipes/smoked_meat_sandwhich.html'

# class Pasta_With_Shrimps_and_Scallops_DetailView(TemplateView):
#     template_name= 'recipes/base_detail.html'

