from requests import get, head

def api(username):
    return get(f'https://api.scratch.mit.edu/users/{username}').json()

def my_ocular(username):
    data = get(f'https://my-ocular.jeffalo.net/api/user/{username}').json()
    if 'error' in data:
        return {"status":None, "colour":None}
    return {
        "status":data["status"],
        "colour":data["color"]
    }

def ocular_circle(colour):
    return f'[{colour}]●[/{colour}]'

def validate_username(username):
    api = get(f'https://api.scratch.mit.edu/users/{username}')
    if api.status_code == 200:
        # Status 200: Means that the user has existed at one point
        profile = head(f'https://scratch.mit.edu/users/{username}/')
        if profile.status_code == 404:
            # Status 404: Means that the account has been deleted
            return "deleted"
        else:
            return "valid"
    else:
        return "invalid"
    
def user_agent(username):
    response = get(f'https://api.scratch.mit.edu/users/{username}/projects').json()
    if len(response) == 0:
        return {'has_projects':False}
    else:
        id = response[0]['id']
        response = get(f"https://projects.scratch.mit.edu/{id}/").json()
        return {
            'has_projects':True, 
            'user_agent': response['meta']['agent']
        }

def forum_info(username):
    data = get(f'https://scratchdb.lefty.one/v3/forum/user/info/{username}').json()
    info = {}
    if "error" not in data:
        info['count'] = data['counts']['total']['count']
        info['rank'] = data['counts']['total']['rank']
    else:
        info['count'] = 0
        info['rank'] = None
    return info