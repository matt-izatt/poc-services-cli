from colorama import Fore


class Environment:

    all_services = ["gateway", "identity", "entity", "standing", "workflow", "timesheet", "discovery"]

    web_services = ["gateway", "identity", "entity", "standing", "workflow"]

    service_map = {
        "gateway": "api-gateway",
        "identity": "identity-service",
        "entity": "entity-service",
        "standing": "standing-data-service",
        "workflow": "workflow-service",
        "timesheet": "timesheet-service",
        "discovery": "discovery-service"
    }

    colour_map = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE
    }


env = Environment()
