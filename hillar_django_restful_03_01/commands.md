# CURL e HTTPie

## Passo 1
http :8000/toys/17500

curl -iX GET localhost:8000/toys/17500

## Passo 2
http POST :8000/toys/ name="PvZ 2 puzzle" description="Plants vs Zombies 2 puzzle" toy_category="Puzzle" was_included_in_home=false release_date="2017-10-08T01:01:00.776594Z"

curl -iX POST -H "Content-Type: application/json" -d '{"name":"PvZ
2 puzzle", "description":"Plants vs Zombies 2 puzzle",
"toy_category":"Puzzle", "was_included_in_home": "false",
"release_date": "2017-10-08T01:01:00.776594Z"}'
localhost:8000/toys/

## Passo 3
http PUT :8000/toys/4 name="PvZ 3 puzzle" description="Plants vs Zombies 3 puzzle" toy_category="Puzzles & Games" was_included_in_home=false release_date="2017-10-08T01:01:00.776594Z"

curl -iX PUT -H "Content-Type: application/json" -d '{"name":"PvZ 3 puzzle", "description":"Plants vs Zombies 3 puzzle", "toy_category":"Puzzles & Games", "was_included_in_home": "false", "release_date": "2017-10-08T01:01:00.776594Z"}' localhost:8000/toys/4

## Passo 4
http PUT :8000/toys/4 name="PvZ 4 puzzle"

curl -iX PUT -H "Content-Type: application/json" -d '{"name":"PvZ 4 puzzle"}' localhost:8000/toys/4

## Passo 5
http DELETE :8000/toys/4

curl -iX DELETE localhost:8000/toys/4

# Postman
## Passo 1
http://localhost:8000/toys/

## Passo 2
{
"name": "Wonderboy puzzle",
"description":"The Dragon's Trap puzzle",
"toy_category":"Puzzles & Games",
"was_included_in_home": "false",
"release_date": "2017-10-03T01:01:00.776594Z"
}