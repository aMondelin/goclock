import time


class TimerFischer(object):
    def __init__(self, global_time, increment_time):
        self.global_time = global_time
        self.increment_time = increment_time
        self._start_time = 0
        self._current_time = 0
        self._game_running = False
        self._active_player = False

    def time_left(self):
        if not self._active_player:
            return self._current_time

        time_spent = time.time() - self._start_time
        self._current_time = self.global_time - time_spent
        return self._current_time

    def begin_turn(self):
        if not self._game_running:
            self._game_running = True
            self._current_time = self.global_time

        if not self._active_player:
            self._active_player = True

        self._start_time = time.time()

    def end_turn(self):
        self._active_player = False
        self._current_time += self.increment_time
