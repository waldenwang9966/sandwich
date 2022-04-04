from django.shortcuts import render
from django.http import Http404
from django.views import View
import random
ingredients = {
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'peppers', 'pickles']
}

# Create your views here.
class SandwichappView(View):
    def get(self, request):
        if request.method == "GET":
            return render(
                request=request,
                template_name="sandwichapp.html",
                context={"ingredients": ingredients.keys()},
            )


class IngredientsView(View):
    def get(self, request, ingredient_type):
        if request.method == "GET":
            if ingredient_type not in ingredients:
                raise Http404(f"No such ingredient: {ingredient_type}")

            return render(
                request=request,
                template_name="ingredients_list.html",
                context={
                    "ingredients": ingredients[ingredient_type],
                    "ingredient_type": ingredient_type,
                },
            )
