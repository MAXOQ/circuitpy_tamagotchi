from adafruit_st7789 import ST7789
import displayio
import busio
import board
from fourwire import FourWire
import debug_display
import battery_display

display = None
splash = None

active_screen = 0

screens = [
    {"name": "debug" ,"group": debug_display.get_group(), "update": debug_display.update}
]

always_loads = [
    {"name": "battery", "group": battery_display.get_group(), "update": battery_display.update}
]

def init():
    global display, splash

    displayio.release_displays()
    spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
    display_bus = FourWire(
        spi,
        command=board.GP16,
        chip_select=board.GP17,
        reset=None,
        baudrate=24_000_000,
    )

    display = ST7789(display_bus, width=240, height=240, rowstart=80)

    splash = displayio.Group()
    display.root_group = splash

    for screen in range(len(screens)):
        screens[screen]["group"].hidden = not screen == active_screen
        splash.append(screens[screen]["group"])
    for always_load in always_loads:
        splash.append(always_load["group"])

def update(input):
    screens[active_screen]["update"](input)
    for always_load in always_loads:
        always_load["update"](input)