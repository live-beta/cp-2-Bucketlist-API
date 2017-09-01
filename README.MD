
# Bucket List Application Programming Interface
[![Build Status](https://travis-ci.org/live-beta/cp-2-Bucketlist-API.svg?branch=develop)](https://travis-ci.org/live-beta/cp-2-Bucketlist-API)

According to Merriam-Webster Dictionary, a Bucketlist is a list of things that one has not done before but wants to do before dying.
This is an Application Programming Interface for an online Bucket List service using the Flask framework

## Getting Started

The following are steps to follow in order to successfully run the Application Programming Interface
### Prerequisites

Install the requirements for running the Application, preferably in a Virtual environment running python3.x and activate it

```
pip install -r requirements.txt

```
### Installing

Set up the database
```
python manage.py db init

```
Migrate the data into the database by running

```
python manage.py db migrate

```
Upgrade the database

```
python manage.py db upgrade

```

### Running Tests

In order to run the tests, type the following in a terminal with an an activated `bucketlist` virtual environment

```
python manage.py test

```
Ensure that you are in the same directory as manage.py


### Running the application

Start the server

```
python manage.py runserver

```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [FLASK](http://flask.pocoo.org/) - The web framework used
* [NOSE](http://nose.readthedocs.io/en/latest/) - Testing framework
* [COVERALLS](https://coveralls.io/) - Used to generate RSS Feeds


## Versioning

The API is currently in its first version (v1)

## Authors

* **Sammy Wanjala** - [live-beta](https://github.com/live-beta)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
