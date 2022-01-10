import sys
VERSION = str('1.6')

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white


def banner():
    print(f"""{C}
   _____                _       _       _    _                 _____        _        
  / ____|              | |     | |     | |  | |               |  __ \      | |       
 | (___   ___ _ __ __ _| |_ ___| |__   | |  | |___  ___ _ __  | |  | | __ _| |_ __ _ 
  \___ \ / __| '__/ _` | __/ __| '_ \  | |  | / __|/ _ \ '__| | |  | |/ _` | __/ _` |
  ____) | (__| | | (_| | || (__| | | | | |__| \__ \  __/ |    | |__| | (_| | || (_| |
 |_____/ \___|_|  \__,_|\__\___|_| |_|  \____/|___/\___|_|    |_____/ \__,_|\__\__,_|
                                                                                                                                                               
{G}=========================================================
{G}[>] {C} Version    : {W}{VERSION}
{G}[>] {C} Created by : {W}Chiroyce
{G}=========================================================
    """)

banner()

if sys.platform == 'win32':
    print(f"""
    {C}[i]{W} If you're using Command Prompt on Windows,
    {C}[i]{W} then the coloured text will not work.
    {C}[i]{W} You will have to use the Windows Terminal App.
    """)

print(f"{C}[+] Checking dependencie(s) . . .")
try:
    import requests
except ModuleNotFoundError:
    sys.exit(f"\n{R}Requests module not found\n\nPlease install https://pypi.org/project/requests/ for this to work.\n")
print(f"{C}[+] Dependencie(s) are up to date . . . {G}requests>=2.27.1\n")

version = requests.get('https://raw.githubusercontent.com/Chiroyce1/scratch-user-data/main/version.txt').text

if float(VERSION) < float(version):
    print("Update available for Scratch User Data.\nYou can continue to use this version,\nbut updating is recommended.")

if  len(sys.argv) > 1:
    username = sys.argv[1]
    print(f"{C}[+] Input taken from sys args: {G}{username}")
else:
    username = input(f"\n{C}Enter USERNAME\n>>> {G}")

print(f"\n{C}[+] Validating username . . . (1/3)")
response = requests.get(f'https://api.scratch.mit.edu/users/{username}/projects').json()
print(f"\n{C}[+] Checking for valid shared projects . . (2/3)\n")
try:
    projectID = response[0]['id']
    date = response[0]['history']['modified']
    hasProjects = True
except IndexError:
    hasProjects = False
    details = f"{G}{username} {C}has no shared projects. \n"
except KeyError:
    sys.exit(f"{R}{username} is an invalid username.\n")

if hasProjects:
    response = requests.get(f'https://projects.scratch.mit.edu/{projectID}/').json()
    userAgent = response['meta']['agent']
print("[+] Getting user data . . . (3/3)\n")
response = requests.get(f'https://api.scratch.mit.edu/users/{username}/').json()
postData = requests.get(f'https://scratchdb.lefty.one/v3/forum/user/info/{username}').json()
ocularData = requests.get(f'https://my-ocular.jeffalo.net/api/user/{username}').json()
print("===============================================\n")
print(f"{C}Username                 - {G}{username}\n")
print(f"{C}User ID                  - {G}{response['id']}\n")
print(f"{C}Joined date              - {G}{response['history']['joined']}\n")
print(f"{C}Country                  - {G}{response['profile']['country']}\n")
print(f"{C}Scratch Team Member?     - {G}{response['scratchteam']}\n")
if hasProjects != True:
    print(details)
try:
    print(f"{C}Total Forum Posts        - {G}{postData['counts']['total']['count']}\n")
except KeyError:
    print(f"{C}Total Forum posts   - {G}0")
try:
    print(f"{C}Forum Leaderboard Rank   - {G}{postData['counts']['total']['rank']}\n")
except KeyError:
    print(f"{C}Forum Leaderboard Rank    - {G}NA | {R} User has no posts")
if hasProjects != False:
    print(f"{C}User-Agent - \n{G}{userAgent}\n")
    print(f"{C}User-Agent lastUpdate    - {G}{date}\n")
try:
    print(f"{C}Ocular Status -            \n{G}{ocularData['status']}\n")
except KeyError:
    print(f"{C}Ocular Status -            \n{G}NA | {R}User has no Ocular Status\n")
try:
    print(f"{C}Ocular lastUpdate        -           {G}{ocularData['meta']['updated']}\n")
except KeyError:
    print(f"{C}Ocular lastUpdate -            \n{G}NA | {R}User has no Ocular Status\n")
print(f"{C}About Me -            \n{G}{response['profile']['bio']}\n")
print(f"{C}What I'm working on - \n{G}{response['profile']['status']}\n")
print('\n')
input(f"{C}Press enter to exit\n")
