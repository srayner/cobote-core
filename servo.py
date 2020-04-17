from datetime import datetime


class Servo:
    """ Servo class
        Servos have a position, a target and speed.
        Speed is used to move a servo towards its target at a controlled rate.
        Speed is measured in degrees/second."""

    def __init__(self):
        self.position = 0
        self.target = 0
        self.speed = 0
        self.updated = datetime.now()

    def set_target(self, target):
        self.target = target
        self.updated = datetime.now()

    def set_speed(self, speed):
        self.speed = speed

    def update_position(self):

        now = datetime.now()

        if self.position == self.target or self.speed == 0:
            self.updated = now
            return

        if self.position < self.target:
            direction = 1
        else:
            direction = -1

        delta = now - self.updated
        elapsed_seconds = int(delta.total_seconds())
        if elapsed_seconds > 0:
            degrees_to_move = elapsed_seconds * self.speed * direction
            next_position = self.position + degrees_to_move

            if direction == 1 and next_position > self.target:
                next_position = self.target

            if direction == -1 and next_position < self.target:
                next_position = self.target

            self.position = next_position
            self.updated = now
            print(self.position)
