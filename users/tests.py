from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile

class UserModelTests(TestCase):
    def setUp(self):
        # Creating a new user.
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123',
            username='testuser'
        )
        # Ensuring that a profile exists for the user, creating one if needed.
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={'bio': 'Test bio'}
        )

        # Fetching the profile again to ensure it has the correct `bio`.
        if not created:
            self.profile = Profile.objects.get(user=self.user)

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))

    def test_profile_creation(self):
        
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.bio, '')

    def test_user_str_method(self):
        self.assertEqual(str(self.user), 'testuser@example.com')

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), 'testuser')
