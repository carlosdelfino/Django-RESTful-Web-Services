## Passo 1
python manage.py createsuperuser

## Passo 2

psql --username=carlosdelfino --dbname=drones --command="SELECT id FROM auth_user WHERE username = 'carlosdelfino';"

python manage.py makemigrations drones

python manage.py migrate

## Passo 3

python manage.py shell

from django.contrib.auth.models import User
user = User.objects.create_user('user01', 'user01@example.com', 'user01password')
user.save()

## Passo 4
http POST :8000/drones/drones/ name="Python Drone" drone_category="Quadcopter" manufacturing_date="2017-07-16T02:03:00.716312Z" has_it_competed=false

## Passo 5
http -a "carlosdelfino":"senha1234" POST :8000/drones/drones/ name="Python Drone" drone_category="Quadcopter" manufacturing_date="2017-07-16T02:03:00.716312Z" has_it_competed=false

## Passo 6
http -a "user01":"user01password" PATCH :8000/drones/drones/12 has_it_competed=true

http -a "user01":"user01password" GET :8000/drones/drones/12

## Passo 7
http://localhost:8000/drones/drones/12

{
    "has_it_competed": "true"
}

## Passo 8
python manage.py migrate

## Passo 9
python manage.py shell

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Replace user01 with the name you configured for this user
user = User.objects.get(username="user01")
token = Token.objects.create(user=user)
print(token.key)

e7b94c10e1c92263c8775e6abccd8274d7c1e7b5
## Passo 10
http :8000/drones/pilots/

http :8000/drones/pilots/ "Authorization: Token e7b94c10e1c92263c8775e6abccd8274d7c1e7b5"