"""lababacus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from lababacus_app.views import AddOwnerView, AddAnimalView, AddLabBloodTestView, AddLabNosemaTestView, OwnersView, OwnerAndAnimalView, HomeView, AnimalAndTestView, FindOwnerView, FindAnimalView, MyLoginView, MyLogoutView, DeleteOwnerView, DeleteAnimalView, DeleteBloodView, DeleteNosemaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_owner', AddOwnerView.as_view(), name = 'add_owner'),
    path('delete_owner', DeleteOwnerView.as_view(), name = 'delete_owner'),
    path('add_animal', AddAnimalView.as_view(), name = 'add_animal'),
    path('delete_animal', DeleteAnimalView.as_view(), name = 'delete_animal'),
    path('add_lab_blood_test', AddLabBloodTestView.as_view(), name='add_lab_blood_test'),
    path('delete_blood', DeleteBloodView.as_view(), name = 'delete_blood'),
    path('add_lab_nosema_test', AddLabNosemaTestView.as_view(), name = 'add_lab_nosema_test'),
    path('delete_nosema', DeleteNosemaView.as_view(), name = 'delete_nosema'),
    path('owners/', OwnersView.as_view(), name='owners'),
    path('owner_and_animal/<int:owner_id>/', OwnerAndAnimalView.as_view(), name='owner_and_animal'),
    path('animal_and_test/<int:animal_id>/', AnimalAndTestView.as_view(), name='animal_and_test'),
    path('find_owner', FindOwnerView.as_view(), name = 'find_owner' ),
    path('find_animal', FindAnimalView.as_view(), name = 'find_animal' ),
    path('home/', HomeView.as_view(), name='home'),
    path('my_login/', MyLoginView.as_view()),
    path('my_logout/', MyLogoutView.as_view())
]
