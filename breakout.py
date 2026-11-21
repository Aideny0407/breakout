"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    count = 0
    bcount = 0
    graphics = BreakoutGraphics()
    while True:
        graphics.ball.move(graphics.vx, graphics.vy)
        pause(FRAME_RATE)

        maybe_brick1 = graphics.window.get_object_at(graphics.ball.x,graphics.ball.y)
        maybe_brick2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,graphics.ball.y)
        maybe_brick3 = graphics.window.get_object_at(graphics.ball.x,graphics.ball.y + graphics.ball.height)
        maybe_brick4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,graphics.ball.y + graphics.ball.height)

        if maybe_brick1 is not None and maybe_brick1 is not graphics.pad:
            graphics.vy *= -1
            graphics.window.remove(maybe_brick1)
            bcount += 1
        elif maybe_brick2 is not None and maybe_brick2 is not graphics.pad:
            graphics.vy *= -1
            graphics.window.remove(maybe_brick2)
            bcount += 1
        elif maybe_brick3 is not None and maybe_brick3 is not graphics.pad:
            graphics.vy *= -1
            graphics.window.remove(maybe_brick3)
            bcount += 1
        elif maybe_brick4 is not None and maybe_brick4 is not graphics.pad:
            graphics.vy *= -1
            graphics.window.remove(maybe_brick4)
            bcount += 1


        if maybe_brick3 is graphics.pad:
            graphics.vy *= -1
        elif maybe_brick4 is graphics.pad:
            graphics.vy *= -1

        if graphics.ball.x<0:
            graphics.vx *= -1
        if graphics.ball.x + graphics.ball.width>graphics.window.width:
            graphics.vx*= -1
        if graphics.ball.y<0:
            graphics.vy *= -1
        if graphics.ball.y>graphics.window.height:
            if count == 2:
                break
            graphics.ball.x = graphics.window.width/2 - graphics.ball.width/2
            graphics.ball.y = graphics.window.height/2 - graphics.ball.height/2
            graphics.vy = 0
            graphics.vx = 0
            count += 1
        if bcount == graphics.brick_cols*graphics.brick_rows:
            break
    if count == 2:
        graphics.u_lose()
    else:
        graphics.u_win()




if __name__ == '__main__':
    main()
