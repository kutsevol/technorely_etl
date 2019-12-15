from invoke import task

from utils.config import check_exist_env_file, dump, parse


@task
def create_dot_env(c,
                   host_db='localhost',
                   db_name='postgres',
                   user_db="postgres",
                   pass_db="postgres",
                   port_db=5432,
                   rewrite=False
                   ):
    """
    Create .env file from template with the ability to change a several
    parameters
    :param c: context (invoke variable)
    :param host_db: to set custom host name for postgres (default=localhost)
    :param db_name: to set custom db name for postgres (default=postgres)
    :param user_db: to set custom user db name for postgres (default=postgres)
    :param pass_db: to set custom pass user for postgres (default=postgres)
    :param port_db: to set custom port db for postgres (default=5432)
    :param rewrite: re-write exist .env file (default=False)
    """
    kwargs = {
        "host_db": host_db,
        "db_name": db_name,
        "user_db": user_db,
        "pass_db": pass_db,
        "port_db": port_db
    }

    if not rewrite and check_exist_env_file():
        raise FileExistsError(
            "Check exist version of .env file in config folder"
        )

    parse_result = parse()

    dump(
        parse_data=parse_result,
        **kwargs,
    )
