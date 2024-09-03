from djitellopy import Tello
import time

tello = Tello()

tello.connect()
tello.takeoff()

# tello.rotate_counter_clockwise(360)
# tello.move_left(75)
# time.sleep(2)
# tello.move_right(75)
# time.sleep(2)
# tello.move_forward(25)
# time.sleep(2)
# tello.move_back(25)
# time.sleep(2)

tello.land()
