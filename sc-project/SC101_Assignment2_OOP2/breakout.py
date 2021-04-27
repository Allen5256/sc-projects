"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball = graphics.ball
    paddle = graphics.paddle
    window = graphics.window
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    live = NUM_LIVES
    total_bricks = graphics.total_bricks

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.get_status():
            if graphics.check_object() is None:
                ball.move(dx, dy)
                if ball.x < 0 and dx < 0:
                    dx = -dx
                if ball.x > window.width-ball.width and dx > 0:
                    dx = -dx
                if ball.y < 0:
                    dy = -dy
                if ball.y > window.height-ball.height:
                    graphics.reset_ball()
                    live -= 1
                    if live == 0:
                        graphics.lose_game()
                        break
            elif graphics.check_object() is paddle:
                if ball.y+ball.height > paddle.y+paddle.height:
                    pass
                if dy > 0:
                    dy = -dy
                ball.move(dx, dy)
            elif graphics.check_object() is not paddle:
                object_removable = graphics.check_object()
                window.remove(object_removable)
                total_bricks -= 1
                dy = -dy
                ball.move(dx, dy)
            if total_bricks == 0:
                graphics.win()
                break


if __name__ == '__main__':
    main()

