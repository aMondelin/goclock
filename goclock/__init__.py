import sys
import time
from PySide.QtGui import *


MODES_ORDER = ['time_left', 'type_increment', 'increment_count_left', 'increment_time_left']
TYPE_INCREMENT = ['byoyomi', 'bronstein', 'fischer']
PLUS_OPERATOR = '+'
MINUS_OPERATOR = '-'


class Player(object):
    def __init__(self, player_number):
        self.player_number = player_number
        self.change_mode_active = True
        self.mode_active = 0
        self.additional_time_type = 0
        self.global_time_left = 1200.0
        self.begin_move_time = 0
        self.additional_time_left_count = 5
        self.additional_time_left = 30.0


def increment_number(current_number, operator, max_value):
    if operator == PLUS_OPERATOR:
        if current_number < max_value:
            return (current_number + 1)
        else:
            return 0

    elif operator == MINUS_OPERATOR:
        if current_number > 0:
            return (current_number - 1)
        else:
            return max_value


def switch_global_mode(player, operator, mode_ui):
    current_mode = player.mode_active
    limit_mode_order = len(MODES_ORDER) - 1

    new_value = increment_number(current_mode, operator, limit_mode_order)

    if new_value == 2 and player.additional_time_type != 0:
        if operator == PLUS_OPERATOR:
            new_value += 1
        elif operator == MINUS_OPERATOR:
            new_value -= 1

    player.mode_active = new_value
    mode_ui.setText(str(MODES_ORDER[new_value]))


def edit_increment_type(player, operator, mode_ui):
    current_mode = player.additional_time_type
    limit_mode_order = len(TYPE_INCREMENT) - 1

    new_value = increment_number(current_mode, operator, limit_mode_order)
    player.additional_time_type = new_value

    mode_ui.setText(str(TYPE_INCREMENT[new_value]))


def update_player_time_left(player, time_ui):
    time_ui.setText(str(player.global_time_left))


def update_player_increment_count(player, time_ui):
    time_ui.setText(str(player.additional_time_left_count))


def edit_time_left(player, operator, time_ui):
    current_player_time_left = player.global_time_left

    if operator == PLUS_OPERATOR and current_player_time_left < 6000.0:
        player.global_time_left += 1

    elif operator == MINUS_OPERATOR and current_player_time_left > 1.0:
        player.global_time_left -= 1

    update_player_time_left(player, time_ui)


def toggle_mode_player(player):
    player.change_mode_active = not player.change_mode_active


def edit_count_increment_left(player, operator, increment_ui):
    current_increment_count = player.additional_time_left_count

    if operator == PLUS_OPERATOR:
        player.additional_time_left_count += 1

    elif operator == MINUS_OPERATOR and current_increment_count != 1:
        player.additional_time_left_count -= 1

    update_player_increment_count(player, increment_ui)


def update_player_increment_time(player, time_ui):
    time_ui.setText(str(player.additional_time_left))


def edit_time_increment(player, operator, time_ui):
    current_increment_time = player.additional_time_left

    if operator == PLUS_OPERATOR:
        player.additional_time_left += 1

    elif operator == MINUS_OPERATOR and current_increment_time > 1:
        player.additional_time_left -= 1

    update_player_increment_time(player, time_ui)


def edit_mode_player(player, operator, mode_ui, time_ui, increment_ui):
    edit_mode_player_state = player.change_mode_active

    if edit_mode_player_state == False:
        current_mode_player = player.mode_active

        if current_mode_player == 0:
            edit_time_left(player, operator, time_ui)

        elif current_mode_player == 1:
            edit_increment_type(player, operator, mode_ui)

        elif current_mode_player == 2:
            edit_count_increment_left(player, operator, increment_ui)

        elif current_mode_player == 3:
            edit_time_increment(player, operator, time_ui)

    else:
        switch_global_mode(player, operator, mode_ui)


def players_time_left(player):
    global_time_left = player.global_time_left

    current_time = time.time()
    difference_time_left = current_time - player.begin_move_time

    update_global_time_left = global_time_left - difference_time_left

    return update_global_time_left


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self._game_running = False
        self.player_1 = Player(True)
        self.player_2 = Player(False)

        self.init_ui()

    def closeEvent(self, event):
        self._game_running = False

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

        self.chrono_label_1 = QLabel(str(self.player_1.global_time_left))
        self.chrono_byoyomi_label_1 = QLabel(str(self.player_1.additional_time_left_count))
        self.chrono_pause = QPushButton('Pause')
        self.chrono_label_2 = QLabel(str(self.player_2.global_time_left))
        self.chrono_byoyomi_label_2 = QLabel(str(self.player_2.additional_time_left_count))

        self.chrono_layout.addWidget(self.chrono_label_1)
        self.chrono_layout.addWidget(self.chrono_byoyomi_label_1)
        self.chrono_layout.addWidget(self.chrono_pause)
        self.chrono_layout.addWidget(self.chrono_label_2)
        self.chrono_layout.addWidget(self.chrono_byoyomi_label_2)

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

    def change_mode_1(self):
        toggle_mode_player(self.player_1)

    def add_button_1(self):
        edit_mode_player(self.player_1,
                         PLUS_OPERATOR,
                         self.infos_player_1,
                         self.chrono_label_1,
                         self.chrono_byoyomi_label_1)

    def substract_button_1(self):
        edit_mode_player(self.player_1,
                         MINUS_OPERATOR,
                         self.infos_player_1,
                         self.chrono_label_1,
                         self.chrono_byoyomi_label_1)

    def change_mode_2(self):
        toggle_mode_player(self.player_2)

    def add_button_2(self):
        edit_mode_player(self.player_2,
                         PLUS_OPERATOR,
                         self.infos_player_2,
                         self.chrono_label_2,
                         self.chrono_byoyomi_label_2)

    def substract_button_2(self):
        edit_mode_player(self.player_2,
                         MINUS_OPERATOR,
                         self.infos_player_2,
                         self.chrono_label_2,
                         self.chrono_byoyomi_label_2)

    def launch_game(self):
        # Initial game state
        player_1 = Player(1)

        self._game_running = True
        while self._game_running:
            # check UI changes
            QApplication.processEvents()
            # Update game state from Ui
            current_time = players_time_left(player_1)
            # Update game state from engine
            pass
            # Update Ui
            print(int(current_time))


def main():
    app = QApplication(sys.argv)

    main_ui = MainUi()
    main_ui.show()
    main_ui.launch_game()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
