
from django.urls import path, include
from .views import HomeView, Smoked_Meat_Sandwhich_DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    # path('Recipes/Pasta_with_Shrimps_and_Scallops', Pasta_With_Shrimps_and_Scallops_DetailView.as_view(), name='pasta_with_shrimps_and_scallops' ),
    path('Recipes/Smoked_Meat_Sandwhich', Smoked_Meat_Sandwhich_DetailView.as_view(), name='smoked_meat_sandwhich' ),
]
