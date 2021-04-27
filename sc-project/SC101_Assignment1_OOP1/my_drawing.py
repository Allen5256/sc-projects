"""
File: my_drawing.py
Name: Allen Lee
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


BASE_COLOR = 'red'
SKIN_COLOR = 'snow'


window = GWindow(1000, 800, title='My Drawing')


def main():
    """
    TODO:
    """
    background = GRect(1000, 800, x=0, y=0)
    background.filled = True

    outer_circle = GOval(400, 400, x=300, y=200)
    outer_circle.color = SKIN_COLOR
    outer_circle.filled = True
    outer_circle.fill_color = BASE_COLOR
    inner_circle = GOval(350, 350, x=325, y=225)
    inner_circle.filled = True
    inner_circle.fill_color = SKIN_COLOR

    head = GOval(200, 200, x=400, y=230)
    head.filled = True
    head.fill_color = BASE_COLOR
    head.color = BASE_COLOR

    ear1 = GPolygon()
    ear1.add_vertex((400, 330))
    ear1.add_vertex((600, 330))
    ear1.add_vertex((610, 350))
    ear1.add_vertex((390, 350))
    ear1.filled = True
    ear1.fill_color = BASE_COLOR
    ear1.color = BASE_COLOR

    ear2 = GRect(220, 80, x=390, y=350)
    ear2.filled = True
    ear2.fill_color = BASE_COLOR
    ear2.color = BASE_COLOR

    ear3 = GPolygon()
    ear3.add_vertex((390, 430))
    ear3.add_vertex((610, 430))
    ear3.add_vertex((590, 450))
    ear3.add_vertex((410, 450))
    ear3.filled = True
    ear3.fill_color = BASE_COLOR
    ear3.color = BASE_COLOR

    chin1 = GRect(180, 40, x=410, y=450)
    chin1.filled = True
    chin1.fill_color = BASE_COLOR
    chin1.color = BASE_COLOR

    chin2 = GPolygon()
    chin2.add_vertex((410, 490))
    chin2.add_vertex((590, 490))
    chin2.add_vertex((538, 560))
    chin2.add_vertex((462, 560))
    chin2.filled = True
    chin2.fill_color = BASE_COLOR
    chin2.color = BASE_COLOR

    forehead = GPolygon()
    forehead.add_vertex((460, 255)) #1
    forehead.add_vertex((480, 330)) #2
    forehead.add_vertex((520, 330)) #3
    forehead.add_vertex((540, 255)) #4
    forehead.add_vertex((590, 300)) #5
    forehead.add_vertex((580, 330)) #6
    forehead.add_vertex((580, 382)) #7
    forehead.add_vertex((525, 392)) #8
    forehead.add_vertex((475, 392)) #9
    forehead.add_vertex((420, 382)) #10
    forehead.add_vertex((420, 330)) #11
    forehead.add_vertex((410, 300)) #12
    forehead.filled = True
    forehead.fill_color = SKIN_COLOR
    forehead.color = SKIN_COLOR

    nose = GPolygon()
    nose.add_vertex((592, 305)) #1
    nose.add_vertex((585, 330)) #2
    nose.add_vertex((585, 390)) #3
    nose.add_vertex((580, 400))
    nose.add_vertex((530, 405)) #4
    nose.add_vertex((525, 397)) #5
    nose.add_vertex((475, 397)) #6
    nose.add_vertex((470, 405)) #7
    nose.add_vertex((420, 400))
    nose.add_vertex((415, 390)) #8
    nose.add_vertex((415, 330)) #9
    nose.add_vertex((408, 305)) #10
    nose.add_vertex((405, 355)) #11
    nose.add_vertex((397, 390)) #12
    nose.add_vertex((454, 450)) #13
    nose.add_vertex((464, 490)) #14
    nose.add_vertex((536, 490)) #15
    nose.add_vertex((546, 450)) #16
    nose.add_vertex((603, 390)) #17
    nose.add_vertex((595, 355)) #18
    nose.filled = True
    nose.fill_color = SKIN_COLOR
    nose.color = SKIN_COLOR

    mouth = GPolygon()
    mouth.add_vertex((464, 498))
    mouth.add_vertex((536, 498))
    mouth.add_vertex((531, 535))
    mouth.add_vertex((469, 535))
    mouth.filled = True
    mouth.fill_color = SKIN_COLOR
    mouth.color = SKIN_COLOR

    l_eye = GPolygon()
    l_eye.add_vertex((530, 397))
    l_eye.add_vertex((580, 387))
    l_eye.add_vertex((578, 395))
    l_eye.add_vertex((532, 400))
    l_eye.filled = True
    l_eye.fill_color = SKIN_COLOR
    l_eye.color = SKIN_COLOR

    r_eye = GPolygon()
    r_eye.add_vertex((470, 397))
    r_eye.add_vertex((420, 387))
    r_eye.add_vertex((422, 395))
    r_eye.add_vertex((468, 400))
    r_eye.filled = True
    r_eye.fill_color = SKIN_COLOR
    r_eye.color = SKIN_COLOR

    l_face = GPolygon()
    l_face.add_vertex((590, 415))
    l_face.add_vertex((551, 455))
    l_face.add_vertex((541, 498))
    l_face.add_vertex((543, 515))
    l_face.add_vertex((550, 515))
    l_face.add_vertex((567, 455))
    l_face.filled = True
    l_face.fill_color = SKIN_COLOR
    l_face.color = SKIN_COLOR

    r_face = GPolygon()
    r_face.add_vertex((410, 415))
    r_face.add_vertex((449, 455))
    r_face.add_vertex((459, 498))
    r_face.add_vertex((457, 515))
    r_face.add_vertex((450, 515))
    r_face.add_vertex((433, 455))
    r_face.filled = True
    r_face.fill_color = SKIN_COLOR
    r_face.color = SKIN_COLOR

    window.add(background)
    window.add(outer_circle)
    window.add(inner_circle)
    window.add(head)
    window.add(ear1)
    window.add(ear2)
    window.add(ear3)
    window.add(chin1)
    window.add(chin2)
    window.add(forehead)
    window.add(nose)
    window.add(mouth)
    window.add(l_eye)
    window.add(r_eye)
    window.add(l_face)
    window.add(r_face)


if __name__ == '__main__':
    main()
