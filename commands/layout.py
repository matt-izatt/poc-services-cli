import click
from functions import log


@click.command(options_metavar='<options>', short_help='-  overview of the CLI')
def layout():
    click.clear()
    message = """
    ----------------------------

                MY CLI

    ----------------------------

    \b
    build
        |---explorer
            |---client
            |---server
            |---both
        |---api
            |---service
            |---web
            |---all

    ----------------------------

    start
    restart
    stop
    remove
        |---explorer
        |---api
            |---service
            |---web
            |---all

    ----------------------------

    service
        |---logs
            |---service
        |---inspect
            |---service
        |---ls
    """
    log(message, 'cyan')
    print('')
