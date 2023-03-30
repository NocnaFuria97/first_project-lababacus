from django.test import TestCase

from lababacus_app.models import Owner

class OwnerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        Owner.objects.create(name='Jan')

    def test_name_label(self):
        owner = Owner.objects.get(id=1)
        field_label = owner._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

# class AnimalModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#
#         Animal.objects.create(owner= 'Jan', name_or_number='Reksio')
#
#     def test_name_label(self):
#         animal = Animal.objects.get(id=1)
#         field_label = animal._meta.get_field('name_or_number').verbose_name
#         self.assertEqual(field_label, 'name_or_number')


