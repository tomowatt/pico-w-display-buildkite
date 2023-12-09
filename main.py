import network
import socket
from time import sleep
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_P4
import machine

### WIFI Settings
ssid = 'SSID HERE'
password = 'PASSWORD HERE'

### Display Settings
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)


### Create Colour Pens
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)

# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

# set up
clear()

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        display.set_pen(WHITE)
        display.text('Waiting for connection...', 10, 10, 240, 4)
        display.update()
        sleep(1)
    ip = wlan.ifconfig()[0]
    return ip

clear()

try:
    ip = connect()
    sleep(1)
except KeyboardInterrupt:
    machine.reset()

clear()

display.set_pen(WHITE)
display.text(f'Connected on {ip}', 10, 10, 240, 4)
display.update()
sleep(5)

clear()

while True:
    if button_a.read():                                   # if a button press is detected then...
        clear()                                           # clear to black
        display.set_pen(WHITE)                            # change the pen colour
        display.text("Button A pressed", 10, 10, 240, 4)  # display some text on the screen
        display.update()                                  # update the display
        sleep(1)                                     # pause for a sec
        clear()                                           # clear to black again
    elif button_b.read():
        clear()
        display.set_pen(CYAN)
        display.text("Button B pressed", 10, 10, 240, 4)
        display.update()
        sleep(1)
        clear()
    elif button_x.read():
        clear()
        display.set_pen(MAGENTA)
        display.text("Button X pressed", 10, 10, 240, 4)
        display.update()
        sleep(1)
        clear()
    elif button_y.read():
        clear()
        display.set_pen(YELLOW)
        display.text("Button Y pressed", 10, 10, 240, 4)
        display.update()
        sleep(1)
        clear()
    else:
        display.set_pen(GREEN)
        display.text("Press any button!", 10, 10, 240, 4)
        display.update()
    sleep(0.1)  # this number is how frequently the Pico checks for button presses
