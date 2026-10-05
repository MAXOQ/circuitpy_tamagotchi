import board
import digitalio
import input_system
import display_manager

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

display_manager.init()

input_system.init()

while True:
    display_manager.update(input_system.get_input())