# learning-flask

This project is made with Python 3.6.2 and Flask it utilizes the wikimedia map api and lets you search for 
any given location and populates the map with markers to display areas of possible interests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.
```
$ git clone https://github.com/Brian-Dennis/learning-flask.git
$ cd learning-flask
$ python -m venv venv
$ source venv/bin/activate (Unix)
$ source venv/scripts/activate (Windows)
(venv) $ pip install -r requirements.txt
(venv) $ python routes.py
```
![learning-flask](static/img/device.png?raw=True "Learning Flask")

### Prerequisites

Things you will need installed to make this application work is.

```
pip, flask, python, terminal, web browser
```

### Installing

A step by step series of instructions that tell you how to get a development env running

Step One. clone the repository

```
$ git clone https://github.com/Brian-Dennis/learning-flask.git
```

Step Two. Change Directories

```
$ cd learning-flask
```

Step Three. Create Virtual Environment for Python and Flask to run independantly from other instances of Python projects
```
$ python -m venv venv
```

Step Four. Depending on if you are on Windows or Unix based OS you want to activate the Virtual Environment
```
$ source venv/bin/activate (Unix)
$ source venv/scripts/activate (Windows)
```

Step Five. After activating the Virtual Environment you want to install the dependencies
```
(venv) $ pip install -r requirements.txt
```

Step Six. After installing the dependencies the you should be golden
```
(venv) $ python routes.py
```

TODO: STILL NEED TO ADD LOGIN LOGOUT LINKS FUNCTONALITY IS THERE JUST NEED TO VISIT THE PAGES VIA THE URL RIGHT NOW.

## Deployment

A project like this when It is finished I would deploy it to Heroku first try it out long before hosting it on your own server.
Unless you prefer configuring your own server, as this project wasn't created with the idea of being a production app.

## Built With

* [Flask](http://flask.pocoo.org/extensions/) - The web framework used
* [Python](https://docs.python.org/3/) - Server Side

## Authors

* **Brian Dennis** - *Initial work* - [Brian-Dennis](https://github.com/Brian-Dennis)

## License

This project is licensed under the MIT License

## Acknowledgments

* Hat tip to anyone who's code was used
