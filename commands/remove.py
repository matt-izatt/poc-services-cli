import click
from environment import env
from functions import log


@click.group(short_help='-  remove services')
def remove():
    pass


@remove.command(options_metavar='<options>')
@click.argument('services', nargs=-1, metavar='<services>')
def api(services):
    """
    Remove docker services
    """
    for serv in services:
        if serv == 'all' or serv == 'web':
            print('Removing %s services' % serv)
            for each in env.service_map[serv]:
                print('Removing: %s' % env.service_map[each])
            break
        else:
            try:
                print('Removing: %s' % env.service_map[serv])
            except:
                log(f'{serv} is not a valid service', 'red')


@remove.command(options_metavar='<options>')
def explorer():
    """
    Remove entity explorer
    """
    print('Removing entity explorer')