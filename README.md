# DEMO - .env vs .toml

This is working example code as shown on my blog [mattwalsh.dev](https://mattwalsh.dev/python-env-vs-toml-for-parsing-environment-constants/).

## How to setup and run with Pipenv

`pip install pipenv`

download and cd to project

create a blank .venv folder if you want the virtual environment to setup in the folder, as opposed to your home directory

`pipenv install`

`pipenv shell`

`python3 main.py`

`mypy main.py`

\# to exit venv  
`exit`

## How to setup and run with Python venv

download and cd to project

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip install --upgrade pip`

`pip install --upgrade setuptools`

`pip install wheel`

`pip install -r requirements.txt`

`python3 main.py`

`mypy main.py`

\# to exit venv  
`deactivate`
