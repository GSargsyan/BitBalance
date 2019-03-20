from app.lib.table_view import TableView
rom app import Players, Rounds


class Bets(TableView):
    # BET_TYPES in format
    # {'bet_type': (set_of_winning_vals, payout_coefficient)}
    BET_TYPES = {
        'red': ({1, 3, 5, 7, 9, 12, 14, 16, 18, 19,
                 21, 23, 25, 27, 30, 32, 34, 36}, 2),
        'black': ({2, 4, 6, 8, 10, 11, 13, 15, 17, 20,
                   22, 24, 26, 28, 29, 31, 33, 35}, 2),
        'even': ({2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
                  22, 24, 26, 28, 30, 32, 34, 36}, 2),
        'odd': ({1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
                 21, 23, 25, 27, 29, 31, 33, 35}, 2),
        'low': ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18}, 2),
        'high': ({19, 20, 21, 22, 23, 24, 25, 26, 27,
                  28, 29, 30, 31, 32, 33, 34, 35, 36}, 2),
        'col-1': ({1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34}, 3),
        'col-2': ({2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35}, 3),
        'col-3': ({3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36}, 3),
        'doz-1': ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 3),
        'doz-2': ({13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}, 3),
        'doz-3': ({25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36}, 3),
        'str-0': ({0}, 36),
        'str-1': ({1}, 36),
        'str-2': ({2}, 36),
        'str-3': ({3}, 36),
        'str-4': ({4}, 36),
        'str-5': ({5}, 36),
        'str-6': ({6}, 36),
        'str-7': ({7}, 36),
        'str-8': ({8}, 36),
        'str-9': ({9}, 36),
        'str-10': ({10}, 36),
        'str-11': ({11}, 36),
        'str-12': ({12}, 36),
        'str-13': ({13}, 36),
        'str-14': ({14}, 36),
        'str-15': ({15}, 36),
        'str-16': ({16}, 36),
        'str-17': ({17}, 36),
        'str-18': ({18}, 36),
        'str-19': ({19}, 36),
        'str-20': ({20}, 36),
        'str-21': ({21}, 36),
        'str-22': ({22}, 36),
        'str-23': ({23}, 36),
        'str-24': ({24}, 36),
        'str-25': ({25}, 36),
        'str-26': ({26}, 36),
        'str-27': ({27}, 36),
        'str-28': ({28}, 36),
        'str-29': ({29}, 36),
        'str-30': ({30}, 36),
        'str-31': ({31}, 36),
        'str-32': ({32}, 36),
        'str-33': ({33}, 36),
        'str-34': ({34}, 36),
        'str-35': ({35}, 36),
        'str-36': ({36}, 36),
        'spl-1-2': ({1, 2}, 18),
        'spl-2-3': ({2, 3}, 18),
        'spl-4-5': ({4, 5}, 18),
        'spl-5-6': ({5, 6}, 18),
        'spl-7-8': ({7, 8}, 18),
        'spl-8-9': ({8, 9}, 18),
        'spl-10-11': ({10, 11}, 18),
        'spl-11-12': ({11, 12}, 18),
        'spl-13-14': ({13, 14}, 18),
        'spl-14-15': ({14, 15}, 18),
        'spl-16-17': ({16, 17}, 18),
        'spl-17-18': ({17, 18}, 18),
        'spl-19-20': ({19, 20}, 18),
        'spl-20-21': ({20, 21}, 18),
        'spl-22-23': ({22, 23}, 18),
        'spl-23-24': ({23, 24}, 18),
        'spl-25-26': ({25, 26}, 18),
        'spl-26-27': ({26, 27}, 18),
        'spl-28-29': ({28, 29}, 18),
        'spl-29-30': ({29, 30}, 18),
        'spl-31-32': ({31, 32}, 18),
        'spl-32-33': ({32, 33}, 18),
        'spl-34-35': ({34, 35}, 18),
        'spl-35-36': ({35, 36}, 18),
        'spl-1-4': ({1, 4}, 18),
        'spl-4-7': ({4, 7}, 18),
        'spl-7-10': ({7, 10}, 18),
        'spl-10-13': ({10, 13}, 18),
        'spl-13-16': ({13, 16}, 18),
        'spl-16-19': ({16, 19}, 18),
        'spl-19-22': ({19, 22}, 18),
        'spl-22-25': ({22, 25}, 18),
        'spl-25-28': ({25, 28}, 18),
        'spl-28-31': ({28, 31}, 18),
        'spl-31-34': ({31, 34}, 18),
        'spl-2-5': ({2, 5}, 18),
        'spl-5-8': ({5, 8}, 18),
        'spl-8-11': ({8, 11}, 18),
        'spl-11-14': ({11, 14}, 18),
        'spl-14-17': ({14, 17}, 18),
        'spl-17-20': ({17, 20}, 18),
        'spl-20-23': ({20, 23}, 18),
        'spl-23-26': ({23, 26}, 18),
        'spl-26-29': ({26, 29}, 18),
        'spl-29-32': ({29, 32}, 18),
        'spl-32-35': ({32, 35}, 18),
        'spl-3-6': ({3, 6}, 18),
        'spl-6-9': ({6, 9}, 18),
        'spl-9-12': ({9, 12}, 18),
        'spl-12-15': ({12, 15}, 18),
        'spl-15-18': ({15, 18}, 18),
        'spl-18-21': ({18, 21}, 18),
        'spl-21-24': ({21, 24}, 18),
        'spl-24-27': ({24, 27}, 18),
        'spl-27-30': ({27, 30}, 18),
        'spl-30-33': ({30, 33}, 18),
        'spl-33-36': ({33, 36}, 18),
        'cor-1-2-4-5': ({1, 2, 4, 5}, 9),
        'cor-2-3-5-6': ({2, 3, 5, 6}, 9),
        'cor-4-5-7-8': ({4, 5, 7, 8}, 9),
        'cor-5-6-8-9': ({5, 6, 8, 9}, 9),
        'cor-7-8-10-11': ({7, 8, 10, 11}, 9),
        'cor-8-9-11-12': ({8, 9, 11, 12}, 9),
        'cor-10-11-13-14': ({10, 11, 13, 14}, 9),
        'cor-11-12-14-15': ({11, 12, 14, 15}, 9),
        'cor-13-14-16-17': ({13, 14, 16, 17}, 9),
        'cor-14-15-17-18': ({14, 15, 17, 18}, 9),
        'cor-16-17-19-20': ({16, 17, 19, 20}, 9),
        'cor-17-18-20-21': ({17, 18, 20, 21}, 9),
        'cor-19-20-22-23': ({19, 20, 22, 23}, 9),
        'cor-20-21-23-24': ({20, 21, 23, 24}, 9),
        'cor-22-23-25-26': ({22, 23, 25, 26}, 9),
        'cor-23-24-26-27': ({23, 24, 26, 27}, 9),
        'cor-25-26-28-29': ({25, 26, 28, 29}, 9),
        'cor-26-27-29-30': ({26, 27, 29, 30}, 9),
        'cor-28-29-31-32': ({28, 29, 31, 32}, 9),
        'cor-29-30-32-33': ({29, 30, 32, 33}, 9),
        'cor-31-32-34-35': ({31, 32, 34, 35}, 9),
        'cor-32-33-35-36': ({32, 33, 35, 36}, 9)
        }

    def __init__(self):
        self.table_name = 'bets'
        super().__init__()

    def insert_bets(self, bets, pid, round_id, is_real):
        """ Insert bet into 'bets' table

        Parameters
        ----------
        bets : dict
            Dict of bet type: bet amount pairs
        pid : int
            Player's id the did the bets
        round_id : int
            Round id during which player bet
        is_real : bool
            If True balance is used, if False - demo_balance
        """
        for bet_type, amount in bets.items():
            if bet_type not in self.BET_TYPES:
                continue
            if int(amount) != amount:
                continue

            vals = {}
            vals['player_id'] = pid
            vals['bet_on'] = bet_type
            vals['amount'] = amount
            vals['round_id'] = round_id
            vals['is_real'] = is_real
            self.insert(vals)

    def commit_round_bets(self, round_id):
        """ Get all bets of the round and commit them,
        changing player's balance and bet stats

        Parameters
        ----------
        round_id : int
            Round id whose bets are going to be committed
        """
        rnd = Rounds.find_by_id(round_id, ['id, outcome'])
        bets = self.all_by_field('round_id', rnd.id)
        for bet in bets:
            type_info = self.type_info(bet.bet_on)
            which_bal = 'balance' if bet.is_real else 'demo_balance'

            val = 0
            op = ''
            won = None
            if rnd.outcome not in type_info['winning_vals']:  # lost
                val = bet.amount
                op = '-'
                won = True
            else:  # won
                val = bet.amount * type_info['payout']
                op = '+'
                won = False

            Players.change_balance(bet.player_id, which_bal, op, val)
            Players.change_bet_stats(bet.player_id, bet.amount, won)
