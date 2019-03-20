from .main import Players


def login_player(uname, pwd):
    return Players().login_player(uname, pwd)


def register_player(uname, pwd):
    return Players().register_player(uname, pwd)
