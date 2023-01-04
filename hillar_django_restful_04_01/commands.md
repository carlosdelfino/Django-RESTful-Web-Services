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