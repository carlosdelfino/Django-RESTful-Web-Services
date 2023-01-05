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