from timers import *


class Player(object):
    def __init__(self, global_time, increment_time):
        self.timer = TimerFischer(global_time, increment_time)
