from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
]
