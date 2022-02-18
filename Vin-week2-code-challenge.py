import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.3
# create a color as a tuple value
ac_orange = 0xfc4600
# pixels.fill(ac_orange)
tiffany_blue = 0x0abab5
# pixels.fill(tiffany_blue)
barbie_pink = 0xe0218a
# pixels.fill(barbie_pink)
# time.sleep(10)

pixels.fill(0)

# declare a digitial input
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)

button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)

# A variable to track the LED led state
led_state = True

while True:
    # gather all input values from sensors
    button_a_read = button_a.value
    button_b_read = button_b.value

    # execute first
    if button_a_read and button_b_read:
        pixels.fill(ac_orange)
        print('A')
    elif button_a_read == True:
        pixels.fill(tiffany_blue)
        print('B')
    elif button_b_read == True:
        pixels.fill(barbie_pink)
        print('C')
    else:
        led_state = False
        pixels.fill(0)
        print('D')
        time.sleep(0.1)
