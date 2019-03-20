from flask import g

from app.lib.table_view import TableView
from app.lib.utils import now


class Player(TableView):
    """ Methods in this class assume 'player' is in g """
    def __init__(self):
        self.table_name = 'players'
        super().__init__()

    def quit_any_room(self):
        """ Quit the room currently in """
        room_id = g.player.room_id
        pid = g.player.id

        if room_id is not None:
            Rooms.remove_player(room_id, pid)
            self.update_by_id({'room_id': None}, pid)

    def join_some_room(self):
        """ Quit any room first, if inside one.
        Join the room with the most players playing currently
        """
        self.quit_any_room()

        pid = g.player.id
        room_id = Rooms.id_by_max_players()
        self.update_by_id({'room_id': room_id, 'last_checkup': now()}, pid)

        Rooms.add_player(room_id, pid)

        return room_id

    def are_bets_real(self):
        """
        Returns
        -------
        bool
            True if the next bets of the player will use the real balance,
            False if - demo_balance
        """
        return False

    def get_balance(self):
        """
        Returns
        -------
        int
            The balance or the demo_balance of the player.
        """
        return g.player.balance if self.are_bets_real() \
            else g.player.demo_balance

    def get_token(self):
        """
        Returns
        -------
        int
            Randomly generated token of the player
        """
        return self.find_by_id(g.player.id, ['token']).token
