import time


class TimerFischer(object):

    def __init__(self, turn_duration, grace_duration):
        self.type = None
        self.turn_duration = turn_duration
        self.grace_duration = grace_duration
        self._start_time = 0
        self._gauge = 0
        self._game_started = False
        self._turn_active = False

    def time_left(self):
        if not self._game_started:
            return -1

        if not self._turn_active:
            return self._gauge

        elapsed = time.time() - self._start_time
        self._gauge = self.turn_duration - elapsed
        return self._gauge

    def begin_turn(self):
        if not self._game_started:
            self._game_started = True
            self._gauge = self.turn_duration

        if not self._turn_active:
            self._turn_active = True

        self._start_time = time.time()

    def end_turn(self):
        self._turn_active = False
        self._gauge += self.grace_duration
