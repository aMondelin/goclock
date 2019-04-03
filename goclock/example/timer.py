import time


class AbstractTimer(object):

    def __init__(self, turn_duration, grace_duration):
        self.turn_duration = turn_duration
        self.grace_duration = grace_duration
        self._start_time = 0
        self._gauge = turn_duration
        self._game_started = False
        self._turn_active = False

    def update(self):
        self._gauge = self.turn_duration - self.elapsed

    @property
    def elapsed(self):
        if self._game_started:
            return time.time() - self._start_time

        return 0

    def time_left(self):
        if not self._game_started:
            return -1

        if not self._turn_active:
            return self._gauge

        self.update()

        return self._gauge

    def begin_turn(self):
        if not self._game_started:
            self._game_started = True

        if not self._turn_active:
            self._turn_active = True

        self._start_time = time.time()

    def _end_turn_specific(self):
        pass

    def end_turn(self):
        self._turn_active = False
        self.update()
        self._end_turn_specific()

    def __repr__(self):
        return "<{}(turn_duration={}, grace_duration={}, elapsed={})>".format(
            self.__class__.__name__, self.turn_duration, self.grace_duration, self.elapsed
        )


class FischerTimer(AbstractTimer):

    def __init__(self, turn_duration, grace_duration):
        AbstractTimer.__init__(self, turn_duration, grace_duration)

    def _end_turn_specific(self):
        self._gauge += self.grace_duration


class BronsteinTimer(AbstractTimer):

    def __init__(self, turn_duration, grace_duration):
        AbstractTimer.__init__(self, turn_duration, grace_duration)

    def _end_turn_specific(self):
        if self.elapsed >= self.grace_duration:
            self._gauge += self.grace_duration


class ByoyomiTimer(AbstractTimer):

    def __init__(self, turn_duration, grace_duration, grace_count):
        AbstractTimer.__init__(self, turn_duration, grace_duration)
        self.grace_count = grace_count
        self._is_byoyomi = False

    def _end_turn_specific(self):

        if not self._is_byoyomi and self._gauge < 0:
            self._is_byoyomi = True

        if self._is_byoyomi and self.elapsed <= self.grace_duration:
            self._gauge = self.grace_duration

        if self._is_byoyomi and self.elapsed > self.grace_duration:
            self.grace_count -= 1
            self._gauge = self.grace_duration

        if self._is_byoyomi and self.grace_count == 0:
            self._gauge = 0

    def __repr__(self):
        return "<{}(turn_duration={}, grace_duration={}, elapsed={}, is_byoyomi={}, grace_count={})>".format(
            self.__class__.__name__, self.turn_duration, self.grace_duration, self.elapsed,
            self._is_byoyomi, self.grace_count
        )


if __name__ == '__main__':
    timer = ByoyomiTimer(5, 2, 2)

    print(timer)

    timer.begin_turn()
    time.sleep(5.1)
    timer.end_turn()

    print(timer)

    timer.begin_turn()
    time.sleep(1)
    timer.end_turn()

    timer.begin_turn()
    time.sleep(3)
    timer.end_turn()

    print(timer)
