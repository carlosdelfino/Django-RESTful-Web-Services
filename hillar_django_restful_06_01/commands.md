## Passo 1
python manage.py startapp drones

## Passo 2
Instale o PostgreSQL

## Passo 3
sudo -u postgres createdb drones

## Passo 4
psql

CREATE ROLE username WITH LOGIN PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE drones TO username;
ALTER USER username CREATEDB;
\q

## Passo 5
        'ENGINE': 'django.db.backends.postgresql',
        # Replace drones with your desired database name
        'NAME': 'drones',
        # Replace username with your desired user name
        'USER': 'carlosdelfino',
        # Replace password with your desired password
        'PASSWORD': 'senha1234',
        # Replace 127.0.0.1 with the PostgreSQL host
        'HOST': '127.0.0.1',
        # Replace 5432 with the PostgreSQL configured port
        # in case you aren't using the default port
        'PORT': '5432',

## Passo 6
pip install psycopg2

## Passo 7
python manage.py makemigrations drones
python manage.py migrate
psql --username=username --dbname=drones --command="\dt"

## Passo 8 
psql --username=username --dbname=drones --command="SELECT * FROM drones_dronecategory;"
psql --username=username --dbname=drones --command="SELECT * FROM drones_drone;"
psql --username=username --dbname=drones --command="SELECT * FROM drones_pilot;"
psql --username=username --dbname=drones --command="SELECT * FROM drones_competition;"

## Passo 9
http POST :8000/drones/drone-categories/ name="Quadcopter"

curl -iX POST -H "Content-Type: application/json" -d
'{"name":"Quadcopter"}' localhost:8000/drones/drone-categories/

## Passo 10
http POST :8000/drones/drones/ name="WonderDrone" drone_category="Quadcopter" manufacturing_date="2017-07-20T02:02:00.716312Z" has_it_competed=false

http POST :8000/drones/drones/ name="Atom" drone_category="Quadcopter" manufacturing_date="2017-08-18T02:02:00.716312Z" has_it_competed=false

curl -iX POST -H "Content-Type: application/json" -d '{"name":"WonderDrone", "drone_category":"Quadcopter", "manufacturing_date": "2017-07-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/drones/

curl -iX POST -H "Content-Type: application/json" -d '{"name":"Atom", "drone_category":"Quadcopter", "manufacturing_date": "2017-08-18T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/drones/

## Passo 11
http :8000/drones/drone-categories/1

curl -iX GET localhost:8000/drones/drone-categories/1

## Passo 12
http POST :8000/drones/drones/ name="Noisy Drone" drone_category="Octocopter" manufacturing_date="2017-10-23T02:03:00.716312Z" has_it_competed=false

curl -iX POST -H "Content-Type: application/json" -d '{"name":"Noisy Drone", "drone_category":"Octocopter", "manufacturing_date": "2017-10-23T02:03:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/drones/

## Passo 13
http POST :8000/drones/pilots/ name="Penelope Pitstop" gender="F" races_count=0
http POST :8000/drones/pilots/ name="Peter Perfect" gender="M" races_count=0

curl -iX POST -H "Content-Type: application/json" -d '{"name":"Penelope Pitstop", "gender":"F", "races_count": 0}' localhost:8000/drones/pilots/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Peter Perfect", "gender":"M", "races_count": 0}' localhost:8000/drones/pilots/

## Passo 14

http POST :8000/drones/competitions/ distance_in_feet=800 distance_achievement_date="2017-10-20T05:03:20.776594Z" pilot="Penelope Pitstop" drone="Atom"

http POST :8000/drones/competitions/ distance_in_feet=2800 distance_achievement_date="2017-10-21T06:02:23.776594Z" pilot="Penelope Pitstop" drone="WonderDrone"

http POST :8000/drones/competitions/ distance_in_feet=790 distance_achievement_date="2017-10-20T05:43:20.776594Z" pilot="Peter Perfect" drone="Atom"

## Passo 15
http :8000/drones/pilots/1