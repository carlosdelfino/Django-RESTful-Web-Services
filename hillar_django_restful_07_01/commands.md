## Passo 1
python manage.py makemigrations drones

python manage.py migrate

## Passo 2
http POST :8000/drones/drone-categories/ name="Quadcopter"

http POST :8000/drones/pilots/ name="Penelope Pitstop" gender="F" races_count=0

## Passo 3
http POST :8000/drones/drones/ name="Need for Speed" drone_category="Quadcopter" manufacturing_date="2017-01-20T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="Eclipse" drone_category="Octocopter" manufacturing_date="2017-02-18T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="Gossamer Albatross" drone_category="Quadcopter" manufacturing_date="2017-03-20T02:02:00.716312Z" has_it_competed=false 
http POST :8000/drones/drones/ name="Dassault Falcon 7X" drone_category="Octocopter" manufacturing_date="2017-04-18T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="Gulfstream I" drone_category="Quadcopter" manufacturing_date="2017-05-20T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="RV-3" drone_category="Octocopter" manufacturing_date="2017-06-18T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="Dusty" drone_category="Quadcopter" manufacturing_date="2017-07-20T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="Ripslinger" drone_category="Octocopter" manufacturing_date="2017-08-18T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/drones/ name="Skipper" drone_category="Quadcopter" manufacturing_date="2017-09-20T02:02:00.716312Z" has_it_competed=false

## Passo 4
http GET :8000/drones/drones/

## Passo 5
http GET ":8000/drones/drones/?offset=0"

http GET ":8000/drones/drones/?limit=4&offset=0"

## Passo 6
http GET ":8000/drones/drones/?limit=4&offset=4"

http GET ":8000/drones/drones/?offset=4"

## Passo 7
http GET ":8000/drones/drones/?limit=500"

## Passo 8
pip install django-filter