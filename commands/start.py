import click
from environment import env
from functions import log_service_list, service_picker, log


@click.group(short_help='-  start services')
def start():
    pass


@start.command(options_metavar='<options>')
@click.option('--all', '-a', is_flag=True, help='All api services.')
@click.option('--web', '-w', is_flag=True, help='Only services required by 5Series Web.')
@click.option('--multiple', '-m', is_flag=True, help='Choose which services ti start.')
@click.option('--service', '-s')
def api(all, web, multiple, service):
    """
    Start api services
    """
    print('')
    if all:
        log_service_list(env.all_services, 'starting', 'green')
    elif web:
        log_service_list(env.web_services, 'starting', 'green')
    elif multiple:
        services = service_picker()
        log_service_list(services, 'starting', 'green')
    elif service:
        log(f'Starting {env.service_map[service].replace("-", " ")}', 'green')
        print('')
    else:
        log_service_list(env.all_services, 'starting', 'green')


@start.command(options_metavar='<options>')
@click.argument('parts', nargs=-1, metavar='<services>')
def web(parts):
    """
    Start 5Series Web
    """
    for part in parts:
        try:
            print('Starting: %s' % part)
        except:
            print('%s is not part of entity explorer' % part)
