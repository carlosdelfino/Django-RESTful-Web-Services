## Passo 1
http -v :8000/toys/ "Accept:text/html"

curl -vH "Accept: text/html" -iX GET localhost:8000/toys/

## Passo 2
{
  "name": "Surfer girl",
  "description": "Surfer girl doll",
  "toy_category":"Dolls",
  "was_included_in_home": "false",
  "release_date": "2017-10-29T12:11:25.090335Z"
}

## Passo 3
{
  "name": "Surfer girl",
  "description": "Surfer girl doll (includes pink surfboard)",
  "toy_category":"Dolls",
  "was_included_in_home": "false",
  "release_date": "2017-10-29T12:11:25.090335Z"
}