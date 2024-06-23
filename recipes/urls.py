
from django.urls import path, include
from .views import HomeView, Barbecue_fishDetailView, Bacon_eggsDetailView,Italia_smoked_sandwhichDetailView,Jollof_riceDetailView, Goat_meat_pepper_soupDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    #Cravings Section
    path('Recipes/Bacon_and_eggs', Bacon_eggsDetailView.as_view(), name='Bacon_and_eggs' ),
    path('Recipes/Barbecue_Fish', Barbecue_fishDetailView.as_view(), name='Barbecue_Fish' ),
    path('Recipes/Italian_sandwhich', Italia_smoked_sandwhichDetailView.as_view(), name='Italian_sandwhich' ),
    path('Recipes/Goat_meat_pepper_soup', Goat_meat_pepper_soupDetailView.as_view(), name='Goat_meat_pepper_soup' ),
    path('Recipes/Jollof_rice', Jollof_riceDetailView.as_view(), name='Jollof_rice' ),
   
]
