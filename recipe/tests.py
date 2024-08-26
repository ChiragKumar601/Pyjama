from django.test import TestCase
from django.contrib.auth import get_user_model
from recipe.models import Recipe, RecipeCategory, RecipeLike

class RecipeModelTests(TestCase):
    def setUp(self):
        # Ensuring a new user is created with a unique email.
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123',
            username='testuser'
        )
        # Ensuring a unique recipe category is created.
        self.category, created = RecipeCategory.objects.get_or_create(name='Desserts')
        # Creating a recipe and a like for it.
        self.recipe = Recipe.objects.create(
            author=self.user,
            category=self.category,
            title='Chocolate Cake',
            desc='Delicious chocolate cake',
            cook_time='00:45:00',
            ingredients='Flour, Sugar, Cocoa, etc.',
            procedure='Mix and bake.',
        )
        # Ensuring a unique like is created for the recipe.
        self.recipe_like, created = RecipeLike.objects.get_or_create(
            user=self.user,
            recipe=self.recipe
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Chocolate Cake')
        self.assertEqual(self.recipe.get_total_number_of_likes(), 1)

    def test_get_total_number_of_likes(self):
        self.assertEqual(self.recipe.get_total_number_of_likes(), 1)

    def test_get_total_number_of_bookmarks(self):
        self.assertEqual(self.recipe.get_total_number_of_bookmarks(), 0)  # Assuming no bookmarks in setup

    def test_recipe_str_method(self):
        self.assertEqual(str(self.recipe), 'Chocolate Cake')
