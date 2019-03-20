from .main import ActionLog


def log_login(pid):
    ActionLog.log_login(pid)


def log_logout(pid):
    ActionLog.log_logout(pid)
