from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Dish

# Create your views here.

class HomeView(TemplateView):
    template_name='recipes/home.html'

# Cravings Section

class Barbecue_fishDetailView(TemplateView):
    template_name= 'cravings/Barbecue_fish.html'

class Bacon_eggsDetailView(TemplateView):
    template_name= 'cravings/Bacon_eggs.html'

class Jollof_riceDetailView(TemplateView):
    template_name= 'cravings/Jollof_rice.html'

class Goat_meat_pepper_soupDetailView(TemplateView):
    template_name= 'cravings/Goat_meat_pepper_soup.html'

class Italia_smoked_sandwhichDetailView(TemplateView):
    template_name= 'cravings/Italia_smoked_sandwhich.html'