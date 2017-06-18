import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport # allow scrolling support
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def displayInfo(height):
    # get now
    now = datetime.datetime.now()

    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=32, height=32, block_orientation=-90)

    with canvas(device) as draw:
        text(draw, (2, 0), now.strftime("%d.%m"), fill="white", font=proportional(SINCLAIR_FONT))
        text(draw, (3, 8), now.strftime("%Y"), fill="white", font=proportional(SINCLAIR_FONT))
        text(draw, (2, 18), str(height) + "m", fill="white", font=proportional(SINCLAIR_FONT))
        # draw.line()

    luma.led_matrix.device.time.sleep(10)

def googleTest():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=32, height=32, block_orientation=-90)

    with canvas(device) as draw:
        text(draw, (2, 12), "COKE", fill="white", font=proportional(SINCLAIR_FONT))

def calibrate ():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=32, height=32, block_orientation=-90)

    with canvas(device) as draw:
        draw.rectangle((4, 4, 7, 11), outline="white", fill="white")
        draw.rectangle((4, 20, 11, 27), outline="white", fill="white")
        draw.rectangle((20, 20, 27, 27), outline="white", fill="white")
        draw.rectangle((8, 16, 15, 19), outline="white", fill="white")
        draw.rectangle((12, 12, 23, 15), outline="white", fill="white")
        draw.rectangle((24, 8, 27, 27), outline="white", fill="white")
        draw.rectangle((16, 4, 23, 7), outline="white", fill="white")
        draw.rectangle((16, 8, 19, 11), outline="white", fill="white")

