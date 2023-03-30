from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyLoginForm
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login, logout
from .models import Owner, Animal, Blood, Nosema

class AddOwnerView(View):
    def get(self, request):
        return render(request, 'add_owner.html')

    def post(self, request):
        name = request.POST.get("name")
        Owner.objects.create(name=name)
        owners = Owner.objects.all()
        return render(request, 'owners.html',  context= {"name":name, "owners":owners})


class DeleteOwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()
        return render(request, 'delete_owner.html', context= {"owners":owners})

    def post(self, request):
        owners = Owner.objects.all()
        owner_id = request.POST.get("owner_id")
        Owner.objects.filter(id=owner_id).delete()
        return render(request, 'delete_owner.html', context= {"owners":owners})


class AddAnimalView(View):
    def get(self, request):
        owners = Owner.objects.all()
        return render(request, 'add_animal.html', context= {"owners":owners})

    def post(self, request):
        owners = Owner.objects.all()
        name_or_number = request.POST.get("name_or_number")
        owner = Owner.objects.get(id=request.POST.get("owner_id"))
        Animal.objects.create(name_or_number=name_or_number, owner=owner)
        return render(request, 'add_animal.html', context= {"owners":owners})


class DeleteAnimalView(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(request, 'delete_animal.html', context= {"animals":animals})

    def post(self, request):
        animals = Animal.objects.all()
        animal_id = request.POST.get("animal_id")
        Animal.objects.filter(id=animal_id).delete()
        return render(request, 'delete_animal.html', context= {"animals":animals})


class AddLabBloodTestView(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(request, 'add_lab_blood_test.html', context= {"animals":animals})

    def post(self, request):
        animal = Animal.objects.get(id=request.POST.get("animal_id"))
        no_neutro_seg = request.POST.get("no_neutro_seg")
        no_neutro_non_seg = request.POST.get("no_neutro_non_seg")
        no_bazo = request.POST.get("no_bazo")
        no_eozyno = request.POST.get("no_eozyno")
        no_limfo = request.POST.get("no_limfo")
        no_mono = request.POST.get("no_mono")
        no_trombo = request.POST.get("no_trombo")
        Blood.objects.create(animal=animal, no_neutro_seg=no_neutro_seg, no_neutro_non_seg=no_neutro_non_seg, no_bazo=no_bazo, no_eozyno=no_eozyno, no_limfo=no_limfo, no_mono=no_mono, no_trombo=no_trombo)
        bloods = Blood.objects.filter(animal_id=animal)
        nosemas = Nosema.objects.filter(animal_id=animal)
        return render(request, 'animal_and_test.html', context= {"animal":animal, "no_neutro_seg":no_neutro_seg, "no_neutro_non_seg":no_neutro_non_seg, "no_bazo":no_bazo, "no_eozyno":no_eozyno, "no_limfo":no_limfo, "no_mono":no_mono, "no_trombo":no_trombo, "bloods":bloods, "nosemas":nosemas})

class DeleteBloodView(View):
    def get(self, request):
        bloods = Blood.objects.all()
        return render(request, 'delete_blood.html', context= {"bloods":bloods})

    def post(self, request):
        bloods = Blood.objects.all()
        blood_id = request.POST.get("blood_id")
        Blood.objects.filter(id=blood_id).delete()
        return render(request, 'delete_blood.html', context= {"bloods":bloods})

class AddLabNosemaTestView(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(request, 'add_lab_nosema_test.html', context= {"animals":animals})

    def post(self, request):
        animal = Animal.objects.get(id=request.POST.get("animal_id"))
        apis = request.POST.get("apis")
        cerane = request.POST.get("cerane")
        Nosema.objects.create(animal=animal, apis=apis, cerane=cerane)
        bloods = Blood.objects.filter(animal_id=animal)
        nosemas = Nosema.objects.filter(animal_id=animal)
        return render(request, 'animal_and_test.html', context= {"animal":animal, "apis":apis, "cerane":cerane, "bloods":bloods, "nosemas":nosemas})

class DeleteNosemaView(View):
    def get(self, request):
        nosemas = Nosema.objects.all()
        return render(request, 'delete_nosema.html', context= {"nosemas":nosemas})

    def post(self, request):
        nosemas = Blood.objects.all()
        nosema_id = request.POST.get("nosema_id")
        Nosema.objects.filter(id=nosema_id).delete()
        return render(request, 'delete_nosema.html', context= {"nosemas":nosemas})


class OwnersView(View):

    def get(self, request):
        owners = Owner.objects.all()
        return render(request, "owners.html", context= {"owners":owners})

class OwnerAndAnimalView(View):
    def get(self, request, owner_id):
        owner = Owner.objects.get(id=owner_id)
        animals = Animal.objects.filter(owner_id=owner)
        return render(request, "owner_and_animal.html", context={"owner": owner, "animals" : animals})

class AnimalAndTestView(View):
    def get(self, request, animal_id):
        animal = Animal.objects.get(id=animal_id)
        bloods = Blood.objects.filter(animal_id=animal)
        nosemas = Nosema.objects.filter(animal_id=animal)
        return render(request, "animal_and_test.html", context={"animal": animal, "bloods" : bloods, "nosemas":nosemas})

class FindOwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()
        return render(request, 'find_owner.html', context= {"owners":owners})

    def post(self, request):
        owner = Owner.objects.get(id=request.POST.get("owner_id"))
        animals = Animal.objects.filter(owner_id=owner)
        return render(request, 'owner_and_animal.html', context={"owner": owner, "animals": animals})

class FindAnimalView(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(request, 'find_animal.html', context= {"animals":animals})

    def post(self, request):
        animal = Animal.objects.get(id=request.POST.get("animal_id"))
        no_neutro_seg = request.POST.get("no_neutro_seg")
        no_neutro_non_seg = request.POST.get("no_neutro_non_seg")
        no_bazo = request.POST.get("no_bazo")
        no_eozyno = request.POST.get("no_eozyno")
        no_limfo = request.POST.get("no_limfo")
        no_mono = request.POST.get("no_mono")
        no_trombo = request.POST.get("no_trombo")
        apis = request.POST.get("apis")
        cerane = request.POST.get("cerane")
        bloods = Blood.objects.filter(animal_id=animal)
        nosemas = Nosema.objects.filter(animal_id=animal)
        return render(request, 'animal_and_test.html', context={"animal": animal, "no_neutro_seg":no_neutro_seg, "no_neutro_non_seg":no_neutro_non_seg, "no_bazo":no_bazo, "no_eozyno":no_eozyno, "no_limfo":no_limfo, "no_mono":no_mono, "no_trombo":no_trombo, "apis":apis, "cerane":cerane, "bloods":bloods, "nosemas":nosemas})


class HomeView(View):

    def get(self, request):
        return render(request, "home.html")

class MyLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = MyLoginForm
    success_url = '/home/'
    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            return HttpResponse('Nie udało się zalogować :(')
        return super().form_valid(form)

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')