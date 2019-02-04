MODES_ORDER = ['time_left', 'type_increment', 'increment_count_left', 'increment_time_left']
TYPE_INCREMENT = ['fischer', 'bronstein', 'byoyomi']


class Player(object):
    def __init__(self, player_number):
        self.player_number = player_number
        self.mode_active = ''
        self.time_increment = 0
        self.global_time = 0
        self.time_left = 0
        self.additional_time_left_count = 0
        self.additional_time_left = 0


def change_mode(player):
    pass


def change_time_increment(player):
    time_increment = player.time_increment

    if time_increment < len(TYPE_INCREMENT):
        player.time_increment += 1

    else:
        player.time_increment = 0


if __name__ == '__main__':
    while True:
        player_1 = Player(0)
        player_2 = Player(1)
