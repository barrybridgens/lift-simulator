# Lift class

class Lift:

    def __init__(self, floors):
        self.num_floors = floors
        self.floor = 1
        self.target_floors = []
        self.moving_up = False
        self.moving_down = False
        self.inter_floor_position = 0
        self.inter_floor_steps = 10
        self.doors_open = False

    def floor_button_pressed(self, floor_button):
        if self.target_floors.count(floor_button) == 0:
            if ((floor_button <= self.num_floors) and (floor_button >= 1) and (floor_button != self.floor)):
                self.target_floors.append(floor_button)

    def is_moving(self):
        moving = False
        if ((self.moving_up) or (self.moving_down)):
            moving = True
        return(moving)

    def time_step(self):
        if self.is_moving():
            # Moving - update lift position
            self.inter_floor_position = self.inter_floor_position + 1
            if self.inter_floor_position >= self.inter_floor_steps:
                # Next floor reached
                self.inter_floor_position = 0
                if self.moving_up:
                    self.floor = self.floor + 1
                if self.moving_down:
                    self.floor = self.floor - 1
            if self.floor == self.target_floors[0]:
                # Arrived at the target floor
                self.moving_up = False
                self.moving_down = False
                dummy = self.target_floors.pop(0)
        else:
            # Not moving - check for button preses
            if len(self.target_floors) != 0:
                if self.target_floors[0] > self.floor:
                    self.moving_up = True
                else:
                    self.moving_down = True
