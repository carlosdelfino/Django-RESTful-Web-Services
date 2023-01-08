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

## Passo 9
http ":8000/drones/drone-categories/?search=Quadcopter"

## Passo 10
http ":8000/drones/drones/?drone_category=1&has_it_competed=False&ordering=-name"

## Passo 11
http ":8000/drones/competitions/?pilot_name=Penelope+Pitstop&drone_name=WonderDrone"

## Passo 12
http ":8000/drones/competitions/?min_distance_in_feet=700&max_distance_in_feet=9000&from_achievement_date=2017-10-18&to_achievement_date=2017-10-22&ordering=-achievement_date

## Passo 13
http ":8000/drones/drones?search=G"