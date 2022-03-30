import utils.data as data

def get_info(username):
    info = {
        "my_ocular": data.my_ocular(username),
        "forum_info": data.forum_info(username),
        "scratch": data.api(username),
        "user_agent": data.user_agent(username)
    }
    return info