"""
File: draw_line.py
Name: Allen Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 30


# Global variables
window = GWindow()
oval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    line = GLine(oval.x+oval.width/2, oval.y+oval.height/2, mouse.x, mouse.y)
    if window.get_object_at(oval.x+oval.width/2, oval.y+oval.height/2) is None:
        window.add(oval, x=mouse.x-oval.width/2, y=mouse.y-oval.height/2)
    elif window.get_object_at(oval.x+oval.width/2, oval.y+oval.height/2) is oval:
        window.add(line)
        window.remove(oval)
    else:
        window.add(oval, x=mouse.x-oval.width/2, y=mouse.y-oval.height/2)


if __name__ == "__main__":
    main()
