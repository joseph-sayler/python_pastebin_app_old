# Pastebin clone in Python

This is a demo app showing my skills in using Flask, ORMs, databases, unit testing, software documentation, and devops related skills like setting up an online web server, accessing a database via API, setting up CI/CD pipelines, etc.

The plan is to develop this locally, using sqlite as the db. Then host this on Heroku and use an online, serverless database (Fauna) to hold all the data. In the process I plan on creating a CI/CD pipeline for unit testing and Heroku deployment.

Currently I am working on developing a class to act as an adapter between the ORM and faunadb library so the basic ORM (peewee) can be used for development and testing, but Fauna can be used when deployed to Heroku. Here are my notes on this process:
* ~~peewee orm can handle sqlite, mysql and postgresql, so class needs to be able to deal with that~~ decided to use SQLAlchemy here. initially i could not figure out how to prevent an error where peewee was complaining that the database was not correct when i tried initializing using fauna; but i figured it out with sqlalchemy; so i could go back to peewee but i dont want to mess with this anymore because it works fine, even tho sqlalchemy is a bit 'heavier' in my opinion
* ~~faunadb library does not utilize a class system like peewee, so this is where all the work will need to be done~~ i made my own class to handle this, see database.py!
    * ~~need to create a class similar to the one used by peewee~~
        * ~~i dont think can use same class as faunadb wouldnt understand the field types~~
    * ~~this class will be used to both save and fetch data from db~~
        * ~~so each field will have to be set-able and get-able from the object~~
        * ~~also peewee orm and faunadb use different methods to handle fetching and saving, ~~
            * ~~so need to create 2 subclasses and have one of them instantiated at runtime to handle all database activities based on configuration~~
* ~~activities common between peewee and faunadb~~ what i did here was create a class (see database.py) that mimmicked the commands sqlalchemy uses, so the same command structure (API i guess?) is used for both even if the underlying code is not the same. works great!
    * ~~these activities will go in an abstract class and methods will be written to handle them based on the db type~~
        * ~~read or query~~
        * ~~write or save~~
    * ~~will need to handle multiple tables as well~~ handling a user login table should be easy with the setup i now have
        * in future may want to add more tables (like user id table?)
        * need to make extensible so can add reads/writes for these tables as well
        * so maybe make a unique class per table? that is how peewee handles things, so mimmick that since this class will be an adapter of sorts??
* ~~how to handle 404s?~~ this is a non issue; sqlalchemy has a function to get or return 404 if not found, and i mimicked this in Fauna_DB (my class)
    * ~~peewee has a flask utility library to handle 404s when querying~~
    * ~~faunadb apparently does not have this~~
    * ~~so make a wrapper method for this that uses the 404 util for peewee and a try/except for faunadb~~
* DOCUMENT THE HELL OUT OF THIS CLASS
    * since it is the only piece (currently) that is not taken from another library
* THINK ABOUT UNIT TESTING WHEN DEVELOPING!
