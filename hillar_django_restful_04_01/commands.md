## Passo 1
http :8000/toys/ Accept:text/html

curl -H "Accept: text/html" -iX GET localhost:8000/toys/

## Passo 2
http :8000/toys/ Accept:application/json

curl -H "Accept: application/json" -iX GET localhost:8000/toys/

## Passo 3
http OPTIONS :8000/toys/

curl -iX OPTIONS localhost:8000/toys/

## Passo 4
http OPTIONS :8000/toys/2

curl -iX OPTIONS localhost:8000/toys/2

## Passo 5
http -f POST :8000/toys/ name="Ken in Rome" description="Ken loves Rome" toy_category="Dolls" was_included_in_home=false release_date="2017-10-09T12:11:37.090335Z"

## Passo 6
http PATCH :8000/toys/

curl -iX PATCH localhost:8000/toys/