# Trading Journal

Trading journal allows you to keep track of your trading activity by saving all the relevant
information on the trades (like key trade information, commentary, tax information, comission
charged by broker, currency, exchange rate etc.) for future analysis (or visualization on a personal
dashboard) plattforms into an sqlite DB. It also helps you manage your taxes (by keeping track of how much of your allowed tax
exemption sum you have used up and how much taxes are due (calculated for Germany). Apart from that
it helps make decisions on trades by providing relevant information on the stock like earnings
surprise in the last quarters, calculating risk (also for certificates) or calculating the best entry price (minimum for the last 10 days). 

## Features

- add brokers you use to DB with:
```shell
$ (trading) python trading.py new-broker-entry
```
- add new exemption amount to DB with:
```shell
$ (trading) python trading.py new-exemption-entry
```
- add new trade (stock) with:
```shell
$ (trading) python trading.py new-stock-entry
```
- edit a trade entry (stock) with:
```shell
$ (trading) python trading.py edit-stock-entry
```
- list all your trades (entries) with:
```shell
$ (trading) python trading.py list-entries
```
- show your exemption balance (how much used up this year) with:
```shell
$ (trading) python trading.py exemption-balance
```
- show statistics on your trades with:
```shell
$ (trading) python trading.py stats
```
- list last 4 earnings for a specified stock with:
```shell
$ (trading) python trading.py list-last-4-earnings [SYMBOL]
```

## Initial Dev Setup

1. clone the repo and cd into the folder
1. run `pipenv sync` to install the packages from the Pipfile.lock
1. activate the virtual environment with `pipenv shell`
1. now that the virtual environment is active you should see the **(trading)** prefix in your shell
1. apply database migrations to create the needed sqlite database
```shell
$ (trading) alembic upgrade head
```
6. run the app with
```shell
$ (trading) python trading.py --help`
```

## How to create new database migrations

In order to have a reproducible database schema this project uses the alembic to create
database migrations. If you want to change the database schema please do so though a migration.

To create a new migration with the virtual environment active run:

```shell
$ (trading) alembic revision -m "init stocks table"
```

Where *"init stocks table"* is a sentence describing what is changing.
This will create a new empty migration under the **./migrations** folder. Edit that file
with the sql statements you wish then apply it with:

```shell
$ (trading) alembic upgrade head
```

If something gets messed up you can always wipe the database with:

```shell
$ (trading) python trading.py migrate wipe
```

You can read more on the [alembic docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html#creating-an-environment)

## Unit Testing

Run tests with:
```shell
$ pytest
```

docs on creating tests [here](https://docs.pytest.org/en/latest/getting-started.html)

## Dev Links

- [SQL Lite ORM SQL Alchemy](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#version-check)
