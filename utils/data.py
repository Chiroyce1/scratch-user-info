from requests import get, head

_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; https://github.com/Chiroyce1/scratch-user-data; Intel Mac OS X 10.15) Firefox/98.0"
}


def api(username):
    return get(f'https://api.scratch.mit.edu/users/{username}', headers=_headers).json()


def format_time(time):
    return time.replace("T", " at ").replace("Z", "")


def my_ocular(username):
    data = get(f'https://my-ocular.jeffalo.net/api/user/{username}').json()
    if 'error' in data:
        return {"status": None, "colour": None}
    return {
        "status": data["status"],
        "colour": data["color"]
    }


def ocular_circle(colour):
    return f'[{colour}]●[/{colour}]'


def validate_username(username):
    api = get(
        f'https://api.scratch.mit.edu/users/{username}', headers=_headers)
    if api.status_code == 200:
        # Status 200: Means that the user has existed at one point
        profile = head(
            f'https://scratch.mit.edu/users/{username}/', headers=_headers)
        if profile.status_code == 404:
            # Status 404: Means that the account has been deleted
            return "deleted"
        else:
            return "valid"
    else:
        return "invalid"


def forum_info(username):
    data = get(
        f'https://scratchdb.lefty.one/v3/forum/user/info/{username}')
    if data.status_code != 200:
        return {"count":"Unknown - ScratchDB error", "rank":"Unknown - ScratchDB error"}

    data = data.json()
    info = {}
    if "error" not in data:
        info['count'] = data['counts']['total']['count']
        info['rank'] = data['counts']['total']['rank']
    else:
        info['count'] = 0
        info['rank'] = None
    return info
