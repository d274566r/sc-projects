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
from campy.gui.events.timer import pause
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 15       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
DELAY = 10

class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=(self.window_width-PADDLE_WIDTH)/2,
                            y=self.window_height-PADDLE_OFFSET+paddle_height)
        self.paddle.color = 'Navy'
        self.paddle.filled = True
        self.paddle.fill_color = 'Navy'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball = GOval(width=2*ball_radius, height=2*ball_radius, x=self.window_width/2-ball_radius,
                          y=(self.window_height-PADDLE_HEIGHT)/2)
        self.ball.filled = True
        self.ball.color = 'red'
        self.ball.fill_color = 'red'
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        self.ball_radius = BALL_RADIUS
        self.switch = False

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)
        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.window.add(self.brick, x=(brick_width+brick_spacing)*j,
                                y=BRICK_OFFSET+(brick_height+brick_spacing)*i)
                self.brick.filled = True
                if i <= 1:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif 2 <= i <= 3:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif 4 <= i <= 5:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif 6 <= i <= 7:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                elif 8 <= i <= 9:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                else:
                    self.brick.color = 'grey'
                    self.brick.fill_color = 'grey'
        self.check_hit_object()
        self.brick_counts = BRICK_ROWS * BRICK_COLS

    def check_hit_object(self):
        a = self.window.get_object_at(self.ball.x, self.ball.y)
        b = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y)
        c = self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius)
        d = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius)
        if c is self.paddle or d is self.paddle:
            self.__dy = -1 * self.__dy
        elif a is not None and a is not self.paddle:
            self.window.remove(a)
            self.__dy = -1 * self.__dy
            self.brick_counts -= 1
        elif b is not None and b is not self.paddle:
            self.window.remove(b)
            self.__dy = -1 * self.__dy
            self.brick_counts -= 1
        elif c is not None and c is not self.paddle:
            self.window.remove(c)
            self.__dy = -1 * self.__dy
            self.brick_counts -= 1
        elif d is not None and d is not self.paddle:
            self.window.remove(d)
            self.__dy = -1 * self.__dy
            self.brick_counts -= 1

    def get_vy(self):
        return self.__dy

    def get_vx(self):
        return self.__dx

    def start(self, event):
        self.switch = True

    def ball_move(self, vx, vy):
        self.ball.move(dx=vx, dy=vy)

    def paddle_move(self, mouse):
        if self.paddle.width/2 < mouse.x <= self.window.width-(self.paddle.width / 2):
            self.paddle.x = mouse.x-self.paddle.width/2
        elif mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width-(self.paddle.width/2):
            self.paddle.x = self.window.width-self.paddle.width

    def set_vx(self, new_speed):
        self.__dx = new_speed

    def set_vy(self, new_speed):
        self.__dy = new_speed

    def reset(self):
        self.switch = False
        self.ball.x = self.window_width/2-self.ball_radius
        self.ball.y = (self.window_height-PADDLE_HEIGHT)/2