from django.test import TestCase
from lababacus_app.forms import MyLoginForm

class MyLoginFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'john',
            'password': 'secret'
        }
        form = MyLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_username(self):
        form_data = {
            'password': 'secret'
        }
        form = MyLoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_invalid_form_missing_password(self):
        form_data = {
            'username': 'john'
        }
        form = MyLoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)