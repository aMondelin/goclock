from timer import TimerFischer


class Player(object):

    def __init__(self, name, duration, grace):
        self.name = name
        self.timer = TimerFischer(duration, grace)
