from django.test import TestCase

from lababacus_app.models import Owner, Animal, Blood, Nosema

class OwnerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        Owner.objects.create(name='Jan')

    def test_name_label(self):
        owner = Owner.objects.get(id=1)
        field_label = owner._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

from django.test import TestCase
from lababacus_app.models import Animal, Blood, Nosema

class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        owner = Owner.objects.create(name='Jan')
        Animal.objects.create(name_or_number='Animal 1', owner=owner)

    def test_name_or_number_label(self):
        animal = Animal.objects.get(id=1)
        field_label = animal._meta.get_field('name_or_number').verbose_name
        self.assertEqual(field_label, 'name or number')

    def test_owner_relationship(self):
        animal = Animal.objects.get(id=1)
        related_owner = animal.owner
        self.assertEqual(related_owner.name, 'Jan')


class BloodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        owner = Owner.objects.create(name='Jan')
        animal = Animal.objects.create(name_or_number='Animal 1', owner=owner)
        Blood.objects.create(
            animal=animal,
            no_neutro_seg=1,
            no_neutro_non_seg=2,
            no_bazo=3,
            no_eozyno=4,
            no_limfo=5,
            no_mono=6,
            no_trombo=7
        )

    def test_no_neutro_seg(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_neutro_seg, 1)

    def test_no_neutro_non_seg(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_neutro_non_seg, 2)

    def test_no_bazo(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_bazo, 3)

    def test_no_eozyno(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_eozyno, 4)

    def test_no_limfo(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_limfo, 5)

    def test_no_mono(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_mono, 6)

    def test_no_trombo(self):
        blood = Blood.objects.get(id=1)
        self.assertEqual(blood.no_trombo, 7)

class NosemaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        owner = Owner.objects.create(name='Jan')
        animal = Animal.objects.create(name_or_number='Animal 1', owner=owner)
        Nosema.objects.create(animal=animal, apis=1, cerane=2)

    def test_apis(self):
        nosema = Nosema.objects.get(id=1)
        self.assertEqual(nosema.apis, 1)

    def test_cerane(self):
        nosema = Nosema.objects.get(id=1)
        self.assertEqual(nosema.cerane, 2)


