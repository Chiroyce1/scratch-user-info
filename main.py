import sys

from colorama import Back, Fore, Style, init

init()

VERSION = str('1.7')


def banner():
    print(f"""{Fore.CYAN}
   _____                _       _       _    _                 _____        _        
  / ____|              | |     | |     | |  | |               |  __ \      | |       
 | (___   ___ _ __ __ _| |_ ___| |__   | |  | |___  ___ _ __  | |  | | __ _| |_ __ _ 
  \___ \ / __| '__/ _` | __/ __| '_ \  | |  | / __|/ _ \ '__| | |  | |/ _` | __/ _` |
  ____) | (__| | | (_| | || (__| | | | | |__| \__ \  __/ |    | |__| | (_| | || (_| |
 |_____/ \___|_|  \__,_|\__\___|_| |_|  \____/|___/\___|_|    |_____/ \__,_|\__\__,_|
                                                                                                                                                               
{Fore.GREEN}=========================================================
{Fore.GREEN}[>] {Fore.CYAN} Version    : {Style.RESET_ALL}{VERSION}
{Fore.GREEN}[>] {Fore.CYAN} Created by : {Style.RESET_ALL}Chiroyce
{Fore.GREEN}=========================================================
    """)


banner()

print(f"{Fore.CYAN}[+] Checking dependencie(s) . . .")
try:
    import requests
    import requests
except ModuleNotFoundError:
    sys.exit(f"\n{Fore.RED}Requests module not found\n\nPlease install https://pypi.org/project/requests/ for this to work.\n")
print(
    f"{Fore.CYAN}[+] Dependencie(s) are up to date . . . {Fore.GREEN}requests>=2.27.1\n")

version = requests.get(
    'https://raw.githubusercontent.com/Chiroyce1/scratch-user-data/main/version.txt').text

if float(VERSION) < float(version):
    print("Update available for Scratch User Data.\nYou can continue to use this version,\nbut updating is recommended.")

if len(sys.argv) > 1:
    username = sys.argv[1]
    print(f"{Fore.CYAN}[+] Input taken from sys args: {Fore.GREEN}{username}")
else:
    username = input(f"\n{Fore.CYAN}Enter USERNAME\n>>> {Fore.GREEN}")

print(f"\n{Fore.CYAN}[+] Validating username . . . (1/3)")
response = requests.get(
    f'https://api.scratch.mit.edu/users/{username}/projects').json()
print(f"\n{Fore.CYAN}[+] Checking for valid shared projects . . (2/3)\n")
try:
    projectID = response[0]['id']
    date = response[0]['history']['modified']
    hasProjects = True
except IndexError:
    hasProjects = False
    details = f"{Fore.GREEN}{username} {Fore.CYAN}has no shared projects. \n"
except KeyError:
    sys.exit(f"{Fore.RED}{username} is an invalid username.\n")

if hasProjects:
    response = requests.get(
        f'https://projects.scratch.mit.edu/{projectID}/').json()
    userAgent = response['meta']['agent']
print("[+] Getting user data . . . (3/3)\n")
try:
    response = requests.get(
        f'https://api.scratch.mit.edu/users/{username}/').json()
    postData = requests.get(
        f'https://scratchdb.lefty.one/v3/forum/user/info/{username}').json()
    ocularData = requests.get(
        f'https://my-ocular.jeffalo.net/api/user/{username}').json()
except Exception as e:
    print(f"{Fore.RED}Could not get some details due to an error...\n")
print("===============================================\n")
print(f"{Fore.CYAN}Username                 - {Fore.GREEN}{username}\n")
print(f"{Fore.CYAN}User ID                  - {Fore.GREEN}{response['id']}\n")
print(
    f"{Fore.CYAN}Joined date              - {Fore.GREEN}{response['history']['joined']}\n")
print(
    f"{Fore.CYAN}Country                  - {Fore.GREEN}{response['profile']['country']}\n")
print(
    f"{Fore.CYAN}Scratch Team Member?     - {Fore.GREEN}{response['scratchteam']}\n")
if hasProjects != True:
    print(details)
try:
    print(
        f"{Fore.CYAN}Total Forum Posts        - {Fore.GREEN}{postData['counts']['total']['count']}\n")
except KeyError:
    print(f"{Fore.CYAN}Total Forum posts   - {Fore.GREEN}0")
try:
    print(
        f"{Fore.CYAN}Forum Leaderboard Rank   - {Fore.GREEN}{postData['counts']['total']['rank']}\n")
except KeyError:
    print(f"{Fore.CYAN}Forum Leaderboard Rank    - {Fore.GREEN}NA | {Fore.RED} User has no posts")
if hasProjects != False:
    print(f"{Fore.CYAN}User-Agent - \n{Fore.GREEN}{userAgent}\n")
    print(f"{Fore.CYAN}User-Agent lastUpdate    - {Fore.GREEN}{date}\n")
try:
    print(
        f"{Fore.CYAN}Ocular Status -            \n{Fore.GREEN}{ocularData['status']}\n")
except KeyError:
    print(f"{Fore.CYAN}Ocular Status -            \n{Fore.GREEN}NA | {Fore.RED}User has no Ocular Status\n")
try:
    print(
        f"{Fore.CYAN}Ocular lastUpdate        -           {Fore.GREEN}{ocularData['meta']['updated']}\n")
except KeyError:
    print(f"{Fore.CYAN}Ocular lastUpdate -            \n{Fore.GREEN}NA | {Fore.RED}User has no Ocular Status\n")
print(
    f"{Fore.CYAN}About Me -            \n{Fore.GREEN}{response['profile']['bio']}\n")
print(
    f"{Fore.CYAN}What I'm working on - \n{Fore.GREEN}{response['profile']['status']}\n")
print('\n')
input(f"{Fore.CYAN}Press enter to exit\n")
