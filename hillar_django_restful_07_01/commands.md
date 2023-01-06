## Passo 1
python manage.py makemigrations drones

python manage.py migrate

## Passo 2
http POST :8000/drones/drone-categories/ name="Quadcopter"

http POST :8000/drones/pilots/ name="Penelope Pitstop" gender="F" races_count=0