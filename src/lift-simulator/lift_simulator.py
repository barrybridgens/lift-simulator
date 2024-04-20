# Lift simulator

import time
from lift import Lift

test_lift = Lift(8)


test_lift.floor_button_pressed(5)
test_lift.floor_button_pressed(2)

while (True):
    test_lift.time_step()
    print(test_lift.floor)
    print(test_lift.is_moving())
    print(test_lift.inter_floor_position)
    print(test_lift.target_floors)
    if test_lift.doors_open:
        print("Doors Open")
    print("---------------------------------------")
    time.sleep(1)

