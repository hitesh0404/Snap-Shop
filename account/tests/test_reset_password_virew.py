from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
class PasswordResetTests(TestCase):

    def setUp(self):
        self.client = Client()#request object
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_reset_password_get_valid_user(self):
        response = self.client.get(reverse('reset-password'), {'username': 'testuser'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/take_email.html')
        self.assertEqual(self.client.session['email'], 'test@example.com')
        self.assertEqual(self.client.session['username'], 'testuser')
        self.assertEqual(self.client.session['reset_password_attemp_count'], 3)