import board
import digitalio

a_button_output = None
a_button_input = None
b_button_output = None
b_button_input = None
c_button_output = None
c_button_input = None

a_pressed = False
b_pressed = False
c_pressed = False
special_pressed = False

def init():
    global a_button_output, a_button_input
    global b_button_output, b_button_input
    global c_button_output, c_button_input

    a_button_output = digitalio.DigitalInOut(board.GP2)
    a_button_output.direction = digitalio.Direction.OUTPUT
    a_button_output.value = False

    a_button_input = digitalio.DigitalInOut(board.GP3)
    a_button_input.direction = digitalio.Direction.INPUT
    a_button_input.pull = digitalio.Pull.UP

    b_button_output = digitalio.DigitalInOut(board.GP6)
    b_button_output.direction = digitalio.Direction.OUTPUT
    b_button_output.value = False

    b_button_input = digitalio.DigitalInOut(board.GP7)
    b_button_input.direction = digitalio.Direction.INPUT
    b_button_input.pull = digitalio.Pull.UP

    c_button_output = digitalio.DigitalInOut(board.GP4)
    c_button_output.direction = digitalio.Direction.OUTPUT
    c_button_output.value = False

    c_button_input = digitalio.DigitalInOut(board.GP5)
    c_button_input.direction = digitalio.Direction.INPUT
    c_button_input.pull = digitalio.Pull.UP

class Input:
    NONE = 0
    A = 1
    B = 2
    C = 3
    SPECIAL = 4

def get_input():
    global a_pressed, b_pressed, c_pressed, special_pressed
    a = not a_button_input.value
    b = not b_button_input.value
    c = not c_button_input.value
    if a and c:
        if not special_pressed:
            a_pressed = True
            c_pressed = True
            special_pressed = True
            return Input.SPECIAL
    else:
        special_pressed = False

    if a:
        if not a_pressed:
            a_pressed = True
            return Input.A
    else:
        a_pressed = False

    if b:
        if not b_pressed:
            b_pressed = True
            return Input.B
    else:
        b_pressed = False

    if c:
        if not c_pressed:
            c_pressed = True
            return Input.C
    else:
        c_pressed = False
    return Input.NONE