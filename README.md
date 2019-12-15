**Description:**

Python command line utility that will create a database and perform a basic ETL process upon it.

**Technologies:**

- Python 3.7
- Pandas
- PostgreSQL
 
**Pre-requirements:**

Run docker container with PostgreSQL:

```docker run -d --name etl -p 5432:5432 postgres```

In an activated virtual environment:

```pip install poetry```

```poetry install --no-interaction --no-dev```

**How to get a .env?**

There is a `.env.template` in config folder.

You may run a invoke command to create `.env` file based on `.env.template` with default values.

```invoke create-dot-env```

To get all availability commands:

```invoke create-dot-env --help```


To create with custom values:

```invoke create-dot-env --db-name=my_db_name --host-db=my_local_machine --port-db=54321 --pass-db=very_strong_secret_pass```

If you have a exist `.env` file in `.config` folder and you would like to re-write this file you should use a `-r` flag.

```invoke create-dot-env -r```


**How to run?**

Required cli parameters:

```-u, --url``` - set path to repository

```python cli.py --url {url_to_repos_with_ndjsons}```

e.g.

```python cli.py -u https://github.com/smart-on-fhir/flat-fhir-files/blob/master/r3```