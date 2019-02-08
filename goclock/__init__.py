import sys
import time
from PySide.QtGui import *


MODES_ORDER = ['time_left', 'type_increment', 'increment_count_left', 'increment_time_left']
TYPE_INCREMENT = ['byoyomi', 'bronstein', 'fischer']


class Player(object):
    def __init__(self, player_number):
        self.player_number = player_number
        self.change_mode_active = False
        self.mode_active = 'time_left'
        self.additional_time_type = 0
        self.global_time_left = 10.0
        self.begin_move_time = 0
        self.additional_time_left_count = 0
        self.additional_time_left = 0


def switch_modes(player, label_,switch_mode):
    find_mode_index = MODES_ORDER.index(player.mode_active)
    limit_mode_order = len(MODES_ORDER) - 1

    if switch_mode == "+":
        if find_mode_index < limit_mode_order:
            player.mode_active = MODES_ORDER[find_mode_index + 1]
        else:
            player.mode_active = MODES_ORDER[0]

    elif switch_mode == "-":
        if find_mode_index > 0:
            player.mode_active = MODES_ORDER[find_mode_index - 1]
        else:
            player.mode_active = MODES_ORDER[len(MODES_ORDER)-1]

    label_.setText(player.mode_active)


def toggle_mode_player(player):
    player.change_mode_active = not player.change_mode_active


def edit_mode_player(player, switch_mode, label_):
    change_mode_player = toggle_mode_player(player)

    if change_mode_player == True:
        pass

    else:
        switch_modes(player, label_, switch_mode)


def players_time_left(player):
    global_time_left = player.global_time_left

    current_time = time.time()
    difference_time_left = current_time - player.begin_move_time

    update_global_time_left = global_time_left - difference_time_left

    return update_global_time_left


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self.player_1 = Player(True)
        self.player_2 = Player(False)

        self.init_ui()
        # self.launch_game()

    def init_ui(self):
        self.resize(300, 150)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.switch_widget = QWidget()
        self.switch_layout = QHBoxLayout()
        self.switch_widget.setLayout(self.switch_layout)

        self.switch_player_1 = QPushButton('PLAYER 1')
        self.switch_player_2 = QPushButton('PLAYER 2')
        self.switch_layout.addWidget(self.switch_player_1)
        self.switch_layout.addWidget(self.switch_player_2)

        self.chrono_widget = QWidget()
        self.chrono_layout = QHBoxLayout()
        self.chrono_widget.setLayout(self.chrono_layout)

        self.chrono_label_1 = QLabel(str(self.player_1.begin_move_time))
        self.chrono_label_2 = QLabel(str(self.player_2.begin_move_time))

        self.chrono_layout.addWidget(self.chrono_label_1)
        self.chrono_layout.addWidget(self.chrono_label_2)

        self.infos_widget = QWidget()
        self.infos_layout = QHBoxLayout()
        self.infos_widget.setLayout(self.infos_layout)

        self.infos_player_1 = QLabel('time_left')
        self.infos_player_2 = QLabel('time_left')
        self.infos_layout.addWidget(self.infos_player_1)
        self.infos_layout.addWidget(self.infos_player_2)

        self.buttons_widget = QWidget()
        self.button_layout = QHBoxLayout()
        self.buttons_widget.setLayout(self.button_layout)

        self.minus_button_player_1 = QPushButton('-')
        self.mode_button_player_1 = QPushButton('MODE')
        self.plus_button_player_1 = QPushButton('+')
        self.button_layout.addWidget(self.minus_button_player_1)
        self.button_layout.addWidget(self.mode_button_player_1)
        self.button_layout.addWidget(self.plus_button_player_1)

        self.minus_button_player_2 = QPushButton('-')
        self.mode_button_player_2 = QPushButton('MODE')
        self.plus_button_player_2 = QPushButton('+')
        self.button_layout.addWidget(self.minus_button_player_2)
        self.button_layout.addWidget(self.mode_button_player_2)
        self.button_layout.addWidget(self.plus_button_player_2)

        main_layout.addWidget(self.switch_widget)
        main_layout.addWidget(self.chrono_widget)
        main_layout.addWidget(self.infos_widget)
        main_layout.addWidget(self.buttons_widget)

        #CONNECTIONS
        self.minus_button_player_1.clicked.connect(self.substract_button_1)
        self.mode_button_player_1.clicked.connect(self.change_mode_1)
        self.plus_button_player_1.clicked.connect(self.add_button_1)

        self.minus_button_player_2.clicked.connect(self.substract_button_2)
        self.mode_button_player_2.clicked.connect(self.change_mode_2)
        self.plus_button_player_2.clicked.connect(self.add_button_2)

        self.show()

    def change_mode_1(self):
        toggle_mode_player(self.player_1)

    def add_button_1(self):
        edit_mode_player(self.player_1, '+', self.infos_player_1)

    def substract_button_1(self):
        edit_mode_player(self.player_1, '-', self.infos_player_1)

    def change_mode_2(self):
        toggle_mode_player(self.player_2)

    def add_button_2(self):
        pass

    def substract_button_2(self):
        pass

    def launch_game(self):
        game_freeze = False

        # last_player = False
        # player_active = True
        # player_1.begin_move_time = time.time()

        while not game_freeze:
            pass
            # if player_active != last_player:
            #     current_time = players_time_left(player_1)
            #
            #     print(int(current_time))


def generate_ui():
    app = QApplication(sys.argv)
    main_ui = MainUi()
    sys.exit(app.exec_())


if __name__ == '__main__':
    generate_ui()