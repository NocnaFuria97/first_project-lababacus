from django.test import TestCase, Client
from django.urls import reverse
from lababacus_app.models import Owner, Animal, Blood, Nosema

class AddOwnerViewTest(TestCase):
    def test_get(self):
        client = Client()
        response = client.get(reverse('add_owner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_owner.html')

    def test_post(self):
        client = Client()
        response = client.post(reverse('add_owner'), {'name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owners.html')
        self.assertEqual(Owner.objects.count(), 1)
        self.assertEqual(Owner.objects.first().name, 'John')



class DeleteOwnerViewTest(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(name='John')

    def test_get(self):
        client = Client()
        response = client.get(reverse('delete_owner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_owner.html')

    def test_post(self):
        client = Client()
        response = client.post(reverse('delete_owner'), {'owner_id': self.owner.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_owner.html')
        self.assertEqual(Owner.objects.count(), 0)


class AddAnimalViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Owner.objects.create(name='John')

    def test_get(self):
        client = Client()
        response = client.get(reverse('add_animal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_animal.html')


    def test_post(self):
        client = Client()
        owner = Owner.objects.first()
        response = client.post(reverse('add_animal'), {'name_or_number': 'Animal 1', 'owner_id': owner.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_animal.html')
        self.assertEqual(Animal.objects.count(), 1)
        self.assertEqual(Animal.objects.first().name_or_number, 'Animal 1')
        self.assertEqual(Animal.objects.first().owner, owner)


class HomeViewTest(TestCase):
    def test_get(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


