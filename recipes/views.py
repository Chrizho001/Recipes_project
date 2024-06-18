from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Dish

# Create your views here.

class HomeView(TemplateView):
    template_name='recipes/home.html'

class RecipesListView(ListView):
    model=Dish