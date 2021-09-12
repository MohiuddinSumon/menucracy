# Menucracy
A menu voting system for organizational employee and restaurant.

# Project Setup Guideline
Please follow the following guideline to set up this application

## System Requirements
* `Python Version >= 3.8`

## Manual Virtualenv Setup Process
* **OS == LINUX**
  * `mkdir venv`
  * `pip3 install virtualenv --user`
  * `virtualenv -p python3 venv/venv`
  * `source venvs/venv/bin/activate`
* **OS == WINDOWS**
  * `mkdir \venvs`
  * `pip install virtualenv`
  * `virtualenv \venvs\venv`
  * `\venvs\venv\Scripts\activate`

Or, just use PyCharm Professional version 


## Project Setup
* `git clone https://github.com/MohiuddinSumon/menucracy.git`
* `cd menucracy`
* `pip install -r requirements.txt`
* `touch db.sqlite3`
* `python3 manage.py migrate`
* `python3 manage.py createsuperuser`
* `python3 manage.py runserver`

Then you will be on the homepage from there it is straight forward. First login with your superuser, it will give you access and refresh token.
We have used jwt authentication (with DRF Simple Jwt) so you will take the access token and click ** Authorize ** button.
There you will give the token as: Bearer <access token> and click authorize. It will logged your superuser to the system.

Then you can create employee type and owner type user, restaurants and menus for those restaurants, give vote and see winner.


## Improvement Scope:
There are a lot of improvement scope exists for example: normally lunch will have some specific time. So we can add conditions like shop must create menu
before 11:00 AM, then user can give vote till say 1:30 PM. 


