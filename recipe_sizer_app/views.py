from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
#also check for author=owner permission on Update and Delete

from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseForbidden

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_sizer_app/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_sizer_app/recipe_form.html', {'form': form})

@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_sizer_app/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if (recipe.owner != request.user ):
        return HttpResponseForbidden("You are not allowed to delete other Authors's work")
   
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    
    return render(request, 'recipeapp/recipe_confirm_delete.html' , {recipe : recipe})

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'