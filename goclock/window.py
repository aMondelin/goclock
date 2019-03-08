from PySide.QtGui import *
from PySide.QtCore import QTimer
from player import Player


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self.players = [
            Player(200, 5),
            Player(200, 5)
        ]

        self.switch_player_1 = QPushButton('PLAYER 1')
        self.switch_player_1.clicked.connect(self._switch_player)
        self.switch_player_1.player = 0
        self.switch_player_2 = QPushButton('PLAYER 2')
        self.switch_player_2.clicked.connect(self._switch_player)
        self.switch_player_2.player = 1

        self.chrono_label_1 = QLabel('chrono01')
        self.chrono_byoyomi_label_1 = QLabel('byo01')
        self.chrono_pause = QPushButton('Pause')
        self.chrono_pause.clicked.connect(self._pause_game)
        self.chrono_label_2 = QLabel('chrono02')
        self.chrono_byoyomi_label_2 = QLabel('byo02')

        self.infos_player_1 = QLabel('time_left')
        self.infos_player_2 = QLabel('time_left')

        self.minus_button_player_1 = QPushButton('-')
        self.mode_button_player_1 = QPushButton('MODE')

        self.minus_button_player_2 = QPushButton('-')
        self.mode_button_player_2 = QPushButton('MODE')
        self.plus_button_player_2 = QPushButton('+')
        self.plus_button_player_1 = QPushButton('+')

        layout = QGridLayout(self)

        layout.addWidget(self.switch_player_1, 0, 0, 1, 3)
        layout.addWidget(self.switch_player_2, 0, 3, 1, 3)
        layout.addWidget(self.chrono_label_1, 1, 0)
        layout.addWidget(self.chrono_byoyomi_label_1, 1, 1)
        layout.addWidget(self.chrono_pause, 1, 2, 1, 2)
        layout.addWidget(self.chrono_label_2, 1, 4)
        layout.addWidget(self.chrono_byoyomi_label_2, 1, 5)
        layout.addWidget(self.infos_player_1, 2, 0, 1, 2)
        layout.addWidget(self.infos_player_2, 2, 3, 1, 2)
        layout.addWidget(self.minus_button_player_1, 3, 0)
        layout.addWidget(self.mode_button_player_1, 3, 1)
        layout.addWidget(self.plus_button_player_1, 3, 2)
        layout.addWidget(self.minus_button_player_2, 3, 3)
        layout.addWidget(self.mode_button_player_2, 3, 4)
        layout.addWidget(self.plus_button_player_2, 3, 5)

        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self._timeout)
        self.refresh_timer.start(100)

    def _switch_player(self):
        self.players[not self.sender().player].timer.begin_turn()
        self.players[self.sender().player].timer.end_turn()

    def _pause_game(self):
        for player in self.players:
            player.timer.end_turn()

    def _timeout(self):
        player1_time_left = self.players[0].timer.time_left()
        if player1_time_left == -1:
            self.chrono_label_1.setText('Not started')
        else:
            self.chrono_label_1.setText('Time left {}'.format(int(player1_time_left)))

        player2_time_left = self.players[1].timer.time_left()
        if player2_time_left == -1:
            self.chrono_label_2.setText('Not started')
        else:
            self.chrono_label_2.setText('Time left {}'.format(int(player2_time_left)))


if __name__ == '__main__':
    app = QApplication([])

    main_ui = MainUi()
    main_ui.show()

    app.exec_()
