import sys
import click
from colorama import init

from commands.build import build
from commands.start import start
from commands.stop import stop
from commands.restart import restart
from commands.remove import remove
from commands.service import service
from commands.config import config
from commands.layout import layout

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(short_help='- list services', context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Type scr layout for a command overview
    """


cli.add_command(build)
cli.add_command(start)
cli.add_command(stop)
cli.add_command(restart)
cli.add_command(remove)
cli.add_command(service)
cli.add_command(config)
cli.add_command(layout)

if __name__ == '__main__':
    cli()
