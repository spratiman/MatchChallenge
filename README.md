# MatchChallenge
NoticeConnect Tech Challenge

## Pre-requisites
1. Python 3.x
2. Pip
3. Git
4. virtualenv

## Project Setup

1. Git clone https://github.com/spratiman/MatchChallenge.git
2. cd MatchChallenge
3. virtualenv venv
4. source venv/bin/activate
5. cd match_challenge
6. pip install -r requirements.txt
7. python manage.py migrate app
8. python manage.py loaddata notice_dummy
9. python manage.py runserver

## Test Suite
1. python manage.py test app/tests

## API
Following details can be accessed via https://127.0.0.1:8000/doc/

### GET /api/v1/matches/
Returns list of matches, where type has the following values:\
1= Strong,\
2= Possible\
3= Weak\
\
Response:\
[
  {
    "id": 0,
    "type": 1,
    "record": 0,
    "notice": 0
  }
]

### GET /api/v1/matches/?type={type}/
Returns list of matches filtered by specific ,match type, where type has the following values:\
1= Strong,\
2= Possible\
3= Weak\
\
Response:\
[
  {
    "id": 0,
    "type": 1,
    "record": 0,
    "notice": 0
  }
]

### POST /api/v1/records/
Creates a record entry\
Headers:\
{Content-Type=application\json}\
\
Request Body:\
{
  "first_name": "string",
  "last_name": "string",
  "date_of_birth": "2019-08-24",
  "province": "st"
}

### DELETE /api/v1/records/{id}/
Deletes a record entry

## Notice Dummy Data
This can be found in match_challenge/fixtures/notice_dummy.json\
This is also loaded as part of the setup process

## Future Improvements
1. Add Authentication to secure API calls
2. If a validation is needed for not creating duplicate records (same first name, last name), I would add that validation upon Record creation
and consequently not create duplicate Match
3. Add an Admin Page
4. Use mock objects instead of creating true records for unittesting

FYI: I had to create a new repository and make commits again due to a conflict in my original repository