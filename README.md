Description:

- Title
      LabAbacus – simple counter created with django
- Introduction - the aim of the project 
      The aim of the project is to help laboratory technicians in their daily work. The application is designed to facilitate the counting of cells or other objects during microscopic examination. It also stores simple data and displays it to the user.
- Technologies
      Python, HTML
- Scope of functionality
      The application allows you to work with a small amount of data. Includes add/search/delete owner/pet/score and login/logout functions.

Installation:

Virtualenv

Install Python :
```sudo apt-get install -y python3```

Install virtualenv:
```pip3 install virtualenv```

Create a virtualenv:
```virtualenv -p python3 env```

Activate a virtualenv:
```source env/bin/activate```

Connecting to PostgreSQL

Create database:
```
sudo -u postgres createuser -s $(whoami) 
createdb test
psql test
```

In the Django settings.py you have the example how to connect to PostgreSQL database:
```
DATABASES = {
    'default': {
        'NAME': 'test',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1'
    }
}
```

Run project

Perform migrations using the following commands:
```
python manage.py makemigrations lababacus_app
python manage.py migrate
```

Create a user using the following commands: 
```
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_user('laborant', email='laborant@email.pl', password='password')
```

Run Django development server
```python3 manage.py runserver```

![image](https://user-images.githubusercontent.com/112506312/227701023-4d69796f-e868-4566-bef9-51228f16aa6b.png)

![image](https://user-images.githubusercontent.com/112506312/227701057-32ef415b-f53d-4140-9740-8f605d2d93b7.png)
