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
After verifying all's up and good, create the database 
`$ docker-compose exec web python manage.py create_db`.
Just don't immediately execute the command after running the image, you might get a connection refused error message. Give it 3 seconds to properly set itself up or so.

Then, get the compound you want via 
`$ docker-compose exec web python manage.py get_compound`. 
Don't forget you can use the '↑' key to get the previous command you executed, in case you want to get multiples compounds.
As you use this command, it will be automatically logged. The log.txt file can be found in the services/web/logs directory.

Once you've gotten enough entries in and want to actually see the data you've obtained, run
`$ docker-compose exec web python manage.py get_db`. 
Keep in mind, any value that is more than 13 characters in length will be truncated. So, expect a lot ellipses along the way...
