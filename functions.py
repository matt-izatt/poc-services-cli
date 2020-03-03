import sys
import time
import click
from environment import env
from tabulate import tabulate
from colorama import Fore, Style


def log(message: str, colour: str):
    print(env.colour_map[colour] + f'{message}' + Style.RESET_ALL)


def log_service_list(services: list, action: str, colour: str):
    service_list = []
    click.clear()
    for x in services:
        service_list.append([env.service_map[x]])
    print(env.colour_map[colour] + tabulate(service_list, headers=[f'{action.upper()}:'], tablefmt="rst", colalign=("center",)) + Style.RESET_ALL)
    print('')


def log_service_table(services, colour: str):
    service_table = []
    click.clear()
    for x in services:
        service_table.append([x, env.service_map[x]])
    print(env.colour_map[colour] + tabulate(service_table, headers=['ALIAS', 'SERVICE'], tablefmt="psql") + Style.RESET_ALL)
    print('')


def test_bar():
    # for x in ['Building...', 'Deploying...', 'Started']:
    #     sys.stdout.write("\033[K")
    #     print(x, end="\r")
    #     time.sleep(1)

    # print(Fore.RED)
    # print('   ------------------------------------   ')
    # print('   |             STOPPING             |   ')
    # print('   ------------------------------------   ')
    # print('')
    # with click.progressbar([1, 2, 3]) as bar:
    #     for x in bar:
    #         sys.stdout.write("\033[K")
    #         time.sleep(x)
    # print(Style.RESET_ALL)
    t_headers = ['   SERVICE   ', '   STATUS   ']
    service_table = []
    click.clear()
    for x in env.all_services:
        service_table.append([x.capitalize(), 'Waiting...'])
    print(env.colour_map['green'] + tabulate(service_table, headers=t_headers, tablefmt="psql") + Style.RESET_ALL)

    for x in range(0, len(service_table)):
        service_table[x] = [service_table[x][0], 'Building...']
        delete_table(service_table)
        print(env.colour_map['red'] + tabulate(service_table, headers=t_headers, tablefmt="psql") + Style.RESET_ALL)
        time.sleep(2)
        service_table[x] = [service_table[x][0], 'Deploying...']
        delete_table(service_table)
        print(env.colour_map['red'] + tabulate(service_table, headers=t_headers, tablefmt="psql") + Style.RESET_ALL)
        time.sleep(2)
        service_table[x] = [service_table[x][0], 'Started']
        delete_table(service_table)
        print(env.colour_map['red'] + tabulate(service_table, headers=t_headers, tablefmt="psql") + Style.RESET_ALL)


def delete_table(table):
    for x in range(0, (len(table) + 4)):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def service_picker():
    included = []
    for serv in env.service_map:
        if click.confirm(f'Build {env.service_map[serv]}?'):
            included.append(serv)
    return included
