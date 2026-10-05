import board
import analogio
import terminalio
from adafruit_display_text import label
import time
import displayio


battery_label = label.Label(terminalio.FONT, text="", color=0x000000, scale=2, x=8, y=14)

# GP29 reads VSYS through a divide-by-3 resistor divider on the board.
# On battery, VSYS is the battery voltage minus a small drop across the board's diode.
vsys_pin = analogio.AnalogIn(board.VOLTAGE_MONITOR)
DIODE_DROP = 0.25  # volts between the battery and VSYS; tweak if % looks off vs a multimeter

# Approximate LiPo voltage -> percent curve
LIPO_CURVE = (
    (4.20, 100), (4.10, 90), (4.00, 80), (3.90, 65), (3.80, 50),
    (3.75, 40), (3.70, 30), (3.65, 20), (3.60, 10), (3.50, 5), (3.30, 0),
)


def read_vsys():
    total = 0
    for _ in range(16):
        total += vsys_pin.value
    return total / 16 * vsys_pin.reference_voltage / 65535 * 3


def battery_percent(volts):
    if volts >= LIPO_CURVE[0][0]:
        return 100
    for (v_hi, p_hi), (v_lo, p_lo) in zip(LIPO_CURVE, LIPO_CURVE[1:]):
        if volts >= v_lo:
            return int(p_lo + (volts - v_lo) / (v_hi - v_lo) * (p_hi - p_lo))
    return 0


def update_battery():
    vsys = read_vsys()
    if vsys > 4.4:  # only USB can push VSYS this high
        battery_label.text = "Charging"
    else:
        battery_volts = vsys + DIODE_DROP
        if battery_percent(battery_volts) < 20:
            battery_label.text = "Low battery"
        else:
            battery_label.text = ""

last_battery_check = 0

def update(_input):
    global last_battery_check
    if time.monotonic() - last_battery_check > 5:
        update_battery()
        last_battery_check = time.monotonic()

def get_group():
    group = displayio.Group()
    group.append(battery_label)
    return group
