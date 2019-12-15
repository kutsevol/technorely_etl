import click

from main import run_etl


@click.command()
@click.option("-u", "--url", help="Path to repository")
def main(url):
    """
    Run to ETL program
    """
    run_etl(url)


if __name__ == "__main__":
    main()
