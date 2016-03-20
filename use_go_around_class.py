__author__ = 'kanehiro'
from ev3dev.auto import *
from time import sleep
from classed_go_around import GoAround

if __name__ == "__main__":
    # We will need to check EV3 buttons state
    btn = Button()
    gd = GoAround()
    gd.start()
    while not btn.any():
        distance = gd.us_value
        # Go Forward
        if distance < 100:
            gd.back()
            gd.turn()
        gd.forward()
        sleep(0.1)
    gd.stop()