from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm

# Create your tests here.

# recipeapp/tests.py


class RecipeTests(TestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            author='Test Author',
            genre='Test Genre',
            url='https://djangoproject.com',
        )
        
    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)  #200 = successful page load
        self.assertContains(response, 'Test Recipe')
        self.assertTemplateUsed(response, 'recipeapp/recipe_list.html')
        self.assertContains(response, 'https://djangoproject.com')

    def test_recipe_create_view(self):
        recipe_count = Recipe.objects.count()
        response = self.client.post(reverse('recipe_create'), {
            'title': 'New Recipe',
            'author': 'New Author',
            'genre': 'New Genre',
            'url': 'https://newrecipe.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(Recipe.objects.count(), recipe_count + 1)
        new_recipe = Recipe.objects.last()
        self.assertEqual(new_recipe.title, 'New Recipe')
        self.assertEqual(new_recipe.url, 'https://newrecipe.com')


    def test_recipe_update_view(self):
        response = self.client.post(reverse('recipe_update', args=[self.recipe.id]), {
            'title': 'Updated Recipe',
            'author': 'Updated Author',
            'genre': 'Updated Genre',
            'url' : 'https://badURL-UPDATE.com',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, 'Updated Recipe')
        self.assertEqual(self.recipe.url, 'https://badURL-UPDATE.com')

    def test_recipe_delete_view(self):
        recipe_count = Recipe.objects.count()
        response = self.client.post(reverse('recipe_delete', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertEqual(Recipe.objects.count(), recipe_count - 1)
        self.assertFalse(Recipe.objects.filter(id=self.recipe.id).exists())


class RecipeModelTests(TestCase):

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title='Test Recipe',
            author='Test Author',
            genre='Test Genre',
            url='https://djangoproject.com',
        )
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.author, 'Test Author')
        self.assertEqual(self.recipe.genre, 'Test Genre')
        self.assertEqual(self.recipe.url, 'https://djangoproject.com')


class RecipeModelTests(TestCase):

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title='Test Recipe',
            author='Test Author',
            genre='Test Genre',
            url='https://testrecipe.com'
        )
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.author, 'Test Author')
        self.assertEqual(recipe.genre, 'Test Genre')
        self.assertEqual(recipe.url, 'https://testrecipe.com')

class RecipeFormTests(TestCase):

    def test_valid_form(self):
        data = {
            'title': 'Test Recipe',
            'author': 'Test Author',
            'genre': 'Test Genre',
            'url': 'https://testrecipe.com'
        }
        form = RecipeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'title': '',
            'author': 'Test Author',
            'genre': 'Test Genre',
            'url': 'invalid-url',
        }
        form = RecipeForm(data=data)
        self.assertFalse(form.is_valid())