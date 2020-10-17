"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics(brick_cols=10, brick_rows=10)

    # Add animation loop here!
    lives = NUM_LIVES
    while lives > 0:
        pause(FRAME_RATE)
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        if graphics.switch is True:
            graphics.ball_move(vx, vy)
            graphics.check_hit_object()
            if graphics.ball.y-graphics.ball.height <= 0:
                graphics.set_vy(-vy)
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
                graphics.set_vx(-vx)
            if graphics.ball.y > graphics.window.height:
                graphics.reset()
                lives -= 1
            if graphics.brick_counts == 0:
                break


if __name__ == '__main__':
    main()
