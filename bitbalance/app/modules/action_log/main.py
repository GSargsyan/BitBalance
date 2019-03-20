from flask import request

from app.lib.utils import now
from app.lib.table_view import TableView


class ActionLog(TableView):
    """ Class to insert/handle data in 'action_log' table.
    Responsible for logging player login and logout dates, ips
    """
    def __init__(self):
        self.table_name = 'action_log'
        super().__init__()

    def _log(self, pid, action, ip=None):
        """ Abstract function to be called by 'log_login' or 'log_logout' below

        Parameters
        ----------
        action : str
            Must be 'logout' or 'login'
        """
        self.insert({'player_id': pid,
                     'action': action,
                     'ip': ip,
                     'date': now()})

    def log_login(self, pid):
        """ Log in db, that the player has logged in.
        Should be called upon login.

        Parameters
        ----------
        pid : int
            Id of the player that logged in.
        """
        self._log(pid, 'login', request.remote_addr)

    def log_logout(self, pid):
        """ Log in db, that the player has logged out.
        Should be called upon logout.

        Parameters
        ----------
        pid : int
            Id of the player that logged out.
        """
        self._log(pid, 'logout')
