"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

# global variables
is_not_moving = True


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball,
                        x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)
        self.__is_moving = False

        # Draw bricks
        self.total_bricks = brick_cols*brick_rows
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i <= 1:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif i <= 3:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif i <= 5:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif i <= 7:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                elif i <= 9:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick,
                                x=0+j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))

    def paddle_move(self, mouse):
        if self.window.width-self.paddle.width/2 >= mouse.x >= self.paddle.width/2:
            self.paddle.x = mouse.x-self.paddle.width/2

    def start(self, mouse):
        if self.__is_moving:
            self.reset_velocity()
        self.__is_moving = True

    def get_status(self):
        return self.__is_moving

    def reset_ball(self):
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.__is_moving = False

    def reset_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def check_object(self):
        for i in range(0, self.ball.width+1, self.ball.width):
            for j in range(0, self.ball.height+1, self.ball.height):
                object_hit = self.window.get_object_at(self.ball.x+i, self.ball.y+j)
                if object_hit is not None:
                    return object_hit

    def lose_game(self):
        lose = GLabel('YOU LOSE!')
        lose.font = '-60'
        self.window.clear()
        self.window.add(lose, x=(self.window.width-lose.width)/2, y=(self.window.height+lose.height)/2)

    def win(self):
        win = GLabel('YOU WIN!!!')
        win.font = '-60'
        self.window.clear()
        self.window.add(win, x=(self.window.width - win.width) / 2, y=(self.window.height + win.height) / 2)

