import displayio
import terminalio
from adafruit_display_text import label
from input_system import Input

bg_bitmap = displayio.Bitmap(240, 240, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = 0x00FF00  # green

inner_bitmap = displayio.Bitmap(160, 160, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # purple

text_area = label.Label(terminalio.FONT, text="Hello World!", color=0xFFFF00, scale=2)
text_area.anchor_point = (0.5, 0.5)
text_area.anchored_position = (120, 120)

def get_group():
    group = displayio.Group()

    group.append(displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette))

    group.append(displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=40, y=40))

    group.append(text_area)

    return group

def update(input):
    if input == Input.A:
        text_area.text = "A"
    elif input == Input.B:
        text_area.text = "B"
    elif input == Input.C:
        text_area.text = "C"
    elif input == Input.SPECIAL:
        text_area.text = "Special"