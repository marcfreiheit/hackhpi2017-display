import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport # allow scrolling support
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def displayInfo():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=32, height=32, block_orientation=-90)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white")
        text(draw, (2, 2), "Hello", fill="white", font=proportional(LCD_FONT))
        text(draw, (2, 10), "World", fill="white", font=proportional(LCD_FONT))

    time.sleep(10)


displayInfo()

