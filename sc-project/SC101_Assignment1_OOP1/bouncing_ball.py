"""
File: bouncing_ball.py
Name: Allen Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
is_not_bouncing = True
num = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(drop_ball)


def drop_ball(mouse):
    global is_not_bouncing
    global num
    vy = 0
    if num == 3:
        pass
        # The function will do nothing after it have run 3 times.
    elif is_not_bouncing:
        is_not_bouncing = False
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y >= window.height-ball.height:
                if vy > 0:
                    vy = -vy*REDUCE
            pause(DELAY)
            if ball.x > window.width:
                num += 1
                break
        window.add(ball, START_X, START_Y)
        is_not_bouncing = True


if __name__ == "__main__":
    main()
