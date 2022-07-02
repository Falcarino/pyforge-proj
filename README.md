# pyforge-proj
## Short description
A docker image running on Flask framework, the primary function being maintaining a database of different compound and their properties. The properites of the compounds are taken from https://www.ebi.ac.uk via API requests.
## Tools used
* Docker
* Python
* Flask web micro framework
* SQLAlchemy module
* Postgresql
## But how to even use it?
### Setting up
First of all, make sure `docker-compose` is installed on your machine and the version is **>= 2.2**. Next, `git clone` the repo onto your machine and run

`$ docker-compose up -d --build`

To check that the image is indeed running properly, check http://localhost:5000. The page should show you a JSON object kinda like this:

![image](https://user-images.githubusercontent.com/12386519/177014368-750ac905-008d-4516-8d3a-68ad1bdcf5a2.png)
### Interacting with the DB
After verifying all's up and good, create the database:

`$ docker-compose exec web python manage.py create_db`

Then, get the compound you want:

`$ docker-compose exec web python manage.py get_compound`

Don't forget you can use the '↑' key to get the previous command you executed, in case you want to get multiples compounds.

Once you've gotten enough entries in and want to actually see the data you've obtained, run:

`$ docker-compose exec db psql --username=postgres --dbname=postgres_dev`
