from app.lib.table_view import TableView
from app.lib.utils import now


class Rooms(TableView):
    def __init__(self):
        self.table_name = 'rooms'
        self.count = 1000
        self.max_players = 9

        super().__init__()

    def id_by_max_players(self):
        """ Get a room with max players playing and is not full

        Returns
        -------
        int
            Id of the room found
        """
        # TODO: check if not full
        return self.find(['id'],
                         order_by='CARDINALITY(player_id_list) DESC').id

    def add_player(self, room_id, pid):
        """ Add player into player_id_list of the room

        Parameters
        ----------
        room_id : int
            Id of the room to add the player in
        pid : int
            Id of the player to add in room
        """
        vals = {'player_id_list': "array_append(player_id_list, %(pid)s)"}
        self.update_by_existing(vals, 'id=%(rid)s',
                                {'pid': pid, 'rid': room_id})

        RoomLog.log_entry(room_id, pid)

    def remove_player(self, room_id, pid):
        """ Remove player from player_id_list of the room

        Parameters
        ----------
        room_id : int
            Id of the room to remove the player from
        pid : int
            Id of the player to remove from room
        """
        vals = {'player_id_list': "array_remove(player_id_list, %(pid)s)"}
        self.update_by_existing(vals,
                                'id=%(rid)s',
                                {'rid': room_id, 'pid': pid})

        RoomLog.log_leave(room_id, pid)

    def run_awaiting(self):
        """ Run rooms that have players inside but are not running yet """
        self.update({'is_running': True},
                    "is_running = FALSE AND "
                    "ARRAY_LENGTH(player_id_list, 1) > 0")

    def all_running(self):
        """ Get the list of running rooms
        Returns
        -------
        list
            List of running rooms
        """
        return self.all(['id'], 'is_running = TRUE')

    def close_empty(self):
        """ Close rooms that are running but have no players inside """
        self.update({'is_running': False}, "is_running = TRUE AND "
                    "ARRAY_LENGTH(player_id_list, 1) IS NULL")


class RoomLog(TableView):
    """ Class to insert/handle data in 'room_log' table.
    Responsible for logging room entries and leaves.
    """
    def __init__(self):
        self.table_name = 'room_log'
        super().__init__()

    def log_entry(self, room_id, pid):
        """ Log in db, that player has joined some room

        Parameters
        ----------
        room_id : int
            Id of the room player has joined
        pid : int
            Id of the player joining the room
        """
        self.insert({'room_id': room_id,
                     'player_id': pid,
                     'entry_date': now(),
                     'leave_date': None})

    def log_leave(self, room_id, pid):
        """ Log in db, that player has left the room he joined previously

        Parameters
        ----------
        room_id : int
            Id of the room the player has left
        pid : int
            Id of the player that has left the room
        """
        last_entry_id = self.find(['id'],
                                  'room_id=%(rid)s AND player_id=%(pid)s',
                                  {'rid': room_id, 'pid': pid},
                                  order_by='entry_date DESC').id

        self.update_by_id({'leave_date': now()}, last_entry_id)


class ChatMessages:
    pass
