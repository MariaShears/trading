# Trading Journal

## Initial Dev Setup

1. clone the repo and cd into the folder
1. run `pipenv sync` to install the packages from the Pipfile.lock
1. activate the virtual environment with `pipenv shell`
1. now that the virtual environment is active you should see the **(trading)** prefix in your shell
1. apply database migrations to create the needed sqlite database
```shell
$ (trading) python trading.py migrate apply`
```
6. run the app with
```shell
$ (trading) python trading.py --help`
```

## How to create new database migrations

In order to have a reproducible database schema this project uses the yoyo-migrations to create
database migrations. If you want to change the database schema please do so though a migration.

To create a new migration with the virtual environment active run:

```shell
$ (trading) yoyo new ./migrations -m "Add timestamps to journal table"
```

Where *"Add timestamps to journal table"* is a sentence describing what is changing.
This will create a new empty migration under the **./migrations** folder. Edit that file
with the sql statements you wish then apply it with:

```shell
$ (trading) python trading.py migrate apply
```

If something gets messed up you can always wipe the database with:

```shell
$ (trading) python trading.py migrate wipe
```
