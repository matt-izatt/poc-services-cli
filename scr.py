import sys
import click

from tabulate import tabulate
from colorama import init, Fore, Style

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

all_services = ["gateway", "identity", "entity", "standing", "workflow", "timesheet", "discovery"]

web_services = ["gateway", "identity", "entity", "standing", "workflow"]

service_map = {
    "gateway": "api-gateway",
    "identity": "identity-service",
    "entity": "entity-service",
    "standing": "standing-data-service",
    "workflow": "workflow-service",
    "timesheet": "timesheet-service",
    "discovery": "discovery-service",
    "explorer": "entity-explorer",
    "all": all_services,
    "web": web_services
}

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(short_help='- list services', context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Type scr layout for a command overview
    """


# --------------- #
# ---- Build ---- #
# --------------- #
@click.group(short_help='-  build services')
def build():
    pass


@build.command(options_metavar='<options>')
@click.argument('services', nargs=-1, metavar='<services>')
def api(services):
    """
    Build api services and run them in docker
    """
    for serv in services:
        if serv == 'all' or serv == 'web':
            print('Building %s services' % serv)
            for each in service_map[serv]:
                print('Building: %s' % service_map[each])
            break
        else:
            try:
                print('Building: %s' % service_map[serv])
            except:
                print(Fore.RED + '%s is not a valid service' % serv + Style.RESET_ALL)


@build.command(options_metavar='<options>')
@click.argument('parts', nargs=-1, metavar='<services>')
def explorer(parts):
    """
    Build entity explorer in docker
    """
    for part in parts:
        try:
            print('Building: %s' % part)
        except:
            print('%s is not part of entity explorer' % part)


# --------------- #
# ---- Start ---- #
# --------------- #
@click.group(short_help='-  start services')
def start():
    pass


@start.command(options_metavar='<options>')
@click.argument('services', nargs=-1, metavar='<services>')
def api(services):
    """
    Start docker services
    """
    for serv in services:
        if serv == 'all' or serv == 'web':
            print('Starting %s services' % serv)
            for each in service_map[serv]:
                print('Starting: %s' % service_map[each])
            break
        else:
            try:
                print('Starting: %s' % service_map[serv])
            except:
                print(Fore.RED + '%s is not a valid service' % serv + Style.RESET_ALL)


@start.command(options_metavar='<options>')
def explorer():
    """
    Start entity explorer
    """
    print('Starting entity explorer')


# -------------- #
# ---- Stop ---- #
# -------------- #
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
            for each in service_map[serv]:
                print('Stopping: %s' % service_map[each])
            break
        else:
            try:
                print('Stopping: %s' % service_map[serv])
            except:
                print(Fore.RED + '%s is not a valid service' % serv + Style.RESET_ALL)


@stop.command(options_metavar='<options>')
def explorer():
    """
    Stop entity explorer
    """
    print('Stopping entity explorer')


# ----------------- #
# ---- Restart ---- #
# ----------------- #
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
            for each in service_map[serv]:
                print('Restarting: %s' % service_map[each])
            break
        else:
            try:
                print('Restarting: %s' % service_map[serv])
            except:
                print(Fore.RED + '%s is not a valid service' % serv + Style.RESET_ALL)


@restart.command(options_metavar='<options>')
def explorer():
    """
    Restart entity explorer
    """
    print('Restarting entity explorer')


# ---------------- #
# ---- Remove ---- #
# ---------------- #
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
            for each in service_map[serv]:
                print('Removing: %s' % service_map[each])
            break
        else:
            try:
                print('Removing: %s' % service_map[serv])
            except:
                print(Fore.RED + '%s is not a valid service' % serv + Style.RESET_ALL)


@remove.command(options_metavar='<options>')
def explorer():
    """
    Remove entity explorer
    """
    print('Removing entity explorer')


# ----------------- #
# ---- Service ---- #
# ----------------- #
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
        print('Logs for: %s' % service_map[serv])


@service.command(options_metavar='<options>')
@click.argument('container', nargs=1, metavar='<container>')
def inspect(container):
    """
    Inspect service
    """
    print('Inspect: %s' % service_map[container])


@service.command(options_metavar='<options>')
@click.option('-a', '--all', is_flag=True)
@click.option('-w', '--web', is_flag=True)
def ls(all, web):
    """
    List all services
    """
    print('')
    if all:
        for each in service_map['all']:
            print (Fore.BLUE + service_map[each] + Style.RESET_ALL)
    elif web:
        for each in service_map['web']:
            print (Fore.BLUE + service_map[each] + Style.RESET_ALL)
    else:
        table = []
        for x in service_map:
            if x != 'all' and x != 'web':
                table.append([x, service_map[x]])
            else:
                table.append([x, '(see ls --%s)' % x])
        print(Fore.BLUE + tabulate(table, headers=['ALIAS', 'SERVICE / GROUP'], tablefmt="presto") + Style.RESET_ALL)
    print('')


# ---------------- #
# ---- Config ---- #
# ---------------- #
@click.group(short_help='-  change config options')
def config():
    pass


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
    print(Fore.CYAN + message + Style.RESET_ALL)
    print('')


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
