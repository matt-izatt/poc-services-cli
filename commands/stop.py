import click
from environment import env
from functions import log


@click.group(short_help='-  stop services')
def stop():
    pass


@stop.command(options_metavar='<options>')
@click.argument('services', nargs=-1, metavar='<services>')
def api(services):
    """
    Stop docker services
    """
    for serv in services:
        if serv == 'all' or serv == 'web':
            print('Stopping %s services' % serv)
            for each in env.service_map[serv]:
                print('Stopping: %s' % env.service_map[each])
            break
        else:
            try:
                print('Stopping: %s' % env.service_map[serv])
            except:
                log(f'{serv} is not a valid service', 'red')


@stop.command(options_metavar='<options>')
def explorer():
    """
    Stop entity explorer
    """
    print('Stopping entity explorer')
