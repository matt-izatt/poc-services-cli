import click
from environment import env
from functions import log_service_list, log_service_table, log


@click.group(short_help='-  view information about services')
def service():
    pass


@service.command(options_metavar='<options>')
@click.argument('services', nargs=-1, metavar='<services>')
def logs(services):
    """
    View logs for services
    """
    for serv in services:
        print('Logs for: %s' % env.service_map[serv])


@service.command(options_metavar='<options>')
@click.argument('container', nargs=1, metavar='<container>')
def inspect(container):
    """
    Inspect service
    """
    print('Inspect: %s' % env.service_map[container])


@service.command(options_metavar='<options>')
@click.option('-a', '--all', is_flag=True)
@click.option('-w', '--web', is_flag=True)
def ls(all, web):
    """
    List all services
    """
    print('')
    if all:
        log_service_list(env.all_services, 'all services', 'blue')
    elif web:
        for each in env.web_services:
            log(env.service_map[each], 'blue')
    else:
        log_service_table(env.service_map.keys(), 'blue')
    print('')
