from django.test import TestCase, Client
from unittest.mock import patch
from users.models import CustomUser
from recipe.models import Recipe, RecipeCategory

class SendEmailViewTest(TestCase):
    def setUp(self):

        self.client = Client()
        self.send_email_url = '/email/send/'  
        self.category = RecipeCategory.objects.create(name='Test Category')
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            username='testuser'
        )
        self.recipe = Recipe.objects.create(
            author=self.user,
            category=self.category,
            picture='test.jpg',
            title='Test Recipe',
            desc='Test Description',
            cook_time='00:30:00',
            ingredients='Test Ingredients',
            procedure='Test Procedure'
        )

    @patch('send_mail_app.tasks.send_email_task.delay')
    def test_send_email_view_response(self, mock_send_email_task):
        """
        Test that hitting the /email/send endpoint returns the expected response.
        """
       
        mock_send_email_task.return_value = None

        
        with patch('recipe.models.Recipe.get_total_number_of_likes', return_value=5):
            response = self.client.get(self.send_email_url)

        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Emails sent asynchronously! Total users notified: 1', response.content.decode())
