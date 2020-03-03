import click
from environment import env
from functions import log


@click.group(short_help='-  restart services')
def restart():
    pass


@restart.command(options_metavar='<options>')
@click.argument('services', nargs=-1, metavar='<services>')
def api(services):
    """
    Restart docker services
    """
    for serv in services:
        if serv == 'all' or serv == 'web':
            print('Restarting %s services' % serv)
            for each in env.service_map[serv]:
                print('Restarting: %s' % env.service_map[each])
            break
        else:
            try:
                print('Restarting: %s' % env.service_map[serv])
            except:
                log(f'{serv} is not a valid service', 'red')


@restart.command(options_metavar='<options>')
def explorer():
    """
    Restart entity explorer
    """
    print('Restarting entity explorer')
