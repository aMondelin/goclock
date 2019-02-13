from PySide.QtGui import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PySide.QtCore import QTimer
from player import Player


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.players = [
            Player('Antho', 30, 5),
            Player('Tanguy', 30, 5)
        ]

        self.button_begin1 = QPushButton("1 Begin")
        self.button_begin1.clicked.connect(self._begin)
        self.button_begin1.player = 0

        self.button_end1 = QPushButton("1 End")
        self.button_end1.clicked.connect(self._end)
        self.button_end1.player = 0

        self.button_begin2 = QPushButton("2 Begin")
        self.button_begin2.clicked.connect(self._begin)
        self.button_begin2.player = 1

        self.button_end2 = QPushButton("2 End")
        self.button_end2.clicked.connect(self._end)
        self.button_end2.player = 1

        self.label_status1 = QLabel()
        self.label_status2 = QLabel()

        layout = QGridLayout(self)

        layout.addWidget(self.label_status1, 0, 0, 1, 2)
        layout.addWidget(self.button_begin1, 1, 0)
        layout.addWidget(self.button_end1, 1, 1)

        layout.addWidget(self.label_status2, 0, 2, 1, 2)
        layout.addWidget(self.button_begin2, 1, 2)
        layout.addWidget(self.button_end2, 1, 3)

        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self._timeout)
        self.refresh_timer.start(100)

    def _begin(self):
        self.players[self.sender().player].timer.begin_turn()

    def _end(self):
        self.players[self.sender().player].timer.end_turn()

    def _timeout(self):
        time_left1 = self.players[0].timer.time_left()
        if time_left1 == -1:
            self.label_status1.setText("Not started")
        else:
            self.label_status1.setText("Time left {}".format(int(time_left1)))

        time_left2 = self.players[1].timer.time_left()
        if time_left2 == -1:
            self.label_status2.setText("Not started")
        else:
            self.label_status2.setText("Time left {}".format(int(time_left2)))

if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.show()

    app.exec_()
