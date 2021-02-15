from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with email is successful"""
        email = 'test@geeglee.net'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normalized_successful(self):
        """Test creating user with normalized email is successful"""

        email = 'test@GEEGLEE.net'
        user = get_user_model().objects.create_user(
            email=email,
            password='testpass123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser_successful(self):
        """Test creating superuser is successful"""

        user = get_user_model().objects.create_superuser(
            email='test@geeglee.net',
            password='super123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
