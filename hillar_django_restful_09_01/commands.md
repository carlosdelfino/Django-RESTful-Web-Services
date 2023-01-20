## Passo 1
http :8000/drones/competitions/

## Passo 2
for i in {1..4}; do http :8000/drones/competitions/; done;

## Passo 3
http -a "carlosdelfino":"senha1234" :8000/drones/competitions/

## Passo 4
for i in {1..4}; do http -a "carlosdelfino":"senha1234" :8000/drones/competitions/; done;

## Passo 5
for i in {1..20}; do http :8000/drones/drones/; done;

## Passo 6
http :8000/drones/drones/1