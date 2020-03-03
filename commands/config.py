import click
from functions import test_bar


@click.group(short_help='-  change config options')
def config():
    pass


@config.command(options_metavar='<options>')
def test():
    """
    Test command
    """
    test_bar()
