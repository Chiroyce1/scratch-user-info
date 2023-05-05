import utils.data as data
import json

from sys import argv
from sys import exit
from requests import get
from utils.info import get_info
from rich.console import Console
from rich.table import Table
from os.path import isfile

from inspect import getsourcefile
from os.path import abspath

_config_path = abspath(getsourcefile(lambda:0).split("main.py")[0])
if not isfile(_config_path):
    _config_path = f'{__file__.split("main.py")[0]}config.json'

console = Console()
with open(_config_path) as file:
    config = json.load(file)
    messages = config["messages"]
    colours = config["colours"]


def quit():
    console.print("[red]Quitting.[/red]")
    exit()


def print_banner():
    console.print(f"""[blue][bold]
===========================[bold]
> Scratch User Data v{config['version']}
[cyan]> Made by[/cyan] [blue]Chiroyce[/blue]
===========================[/bold]
    """)


def check_for_updates():
    latest_version = get(config['update_url'])
    if latest_version.status_code == 404:
        latest_version = get(config['legacy_update_url']).text
    else:
        latest_version = latest_version.json()['version']

    current_version = config['version']

    if current_version == latest_version:
        return

    if current_version > latest_version:
        console.print(messages["develop"])
        return

    if latest_version > current_version:
        console.print(messages["update_available"].format(latest_version))
        return


def setup_username():
    if len(argv) > 1:
        console.print(f"[cyan][*] Username: [green]{argv[1]}")
        return argv[1]
    else:
        console.print("[cyan]Enter username[/cyan]")
        return input(">> ")


def validate_username(username):
    console.print("[cyan]Validating username...")
    status = data.validate_username(username)
    if status == "valid":
        return
    elif status == "deleted":
        console.print(messages["deleted_user"].format(username))
        quit()
    else:
        console.print(messages["invalid_user"].format(username))
        quit()


def render_info(info):
    username = info["scratch"]["username"]
    colour = info["my_ocular"]["colour"]
    if info["my_ocular"]["status"]:
        table = Table(
            title=f"[{colour}] {username}'s info [/{colour}]")
    else:
        table = Table(title=username)
    table.add_column("Info")
    table.add_column("Value")

    # Ocular Data
    if info["my_ocular"]["status"] and colour:
        table.add_row(f"[{colours['ocular']}]Ocular Status[/{colours['ocular']}]",
                      f'[i]{info["my_ocular"]["status"]} {data.ocular_circle(colour)}[/i]')
    else:
        table.add_row(f"[{colours['ocular']}]Ocular Status[/{colours['ocular']}]",
                      f'[i]{info["my_ocular"]["status"]}')

    # ScratchDB Post Count and Forum Leaderboard
    table.add_row(f"[{colours['scratch_db']}]Forum Post Count[/{colours['scratch_db']}]",
                  f'{info["forum_info"]["count"]}')
    table.add_row(f"[{colours['scratch_db']}]Forum Leaderboard Rank[/{colours['scratch_db']}]",
                  f'#{info["forum_info"]["rank"]}')

    # Scratch Info
    c = colours["scratch"]
    table.add_row(f"[{c}]Username[/{c}]", username)
    table.add_row(f"[{c}]UserID[/{c}]", str(info["scratch"]["id"]))
    table.add_row(f"[{c}]ScratchTeam?[/{c}]",
                  str(info["scratch"]["scratchteam"]))
    table.add_row(f"[{c}]Joined[/{c}]",
                  data.format_time(info["scratch"]["history"]["joined"]))
    table.add_row(f"[{c}]About Me[/{c}]", info["scratch"]["profile"]["bio"])
    table.add_row(f"[{c}]What I'm Working on[/{c}]",
                  info["scratch"]["profile"]["status"])

    console.print(table)


def main():
    print_banner()
    check_for_updates()
    username = setup_username()
    validate_username(username)
    console.print(
        f"[cyan][*] Getting [/cyan][green]{username}[/green][cyan]'s info...\n[/cyan]")
    render_info(get_info(username))


if __name__ == '__main__':
    main()
