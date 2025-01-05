from MicroAPIgRESTion import *
from wifi_credentials import *

import machine
import time

# led0 simultaniously handling from route and toggle switch using interupt
led0 = machine.Pin(7, machine.Pin.OUT)
pin0 = Pin(0, Pin.IN, Pin.PULL_DOWN)

def handle_interrupt0(pin):
    led0.toggle()
    
# Set up interrupt to call handle_interrupt on a rising/falling edge
pin0.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=handle_interrupt0)

# Async HTTP handler function
@route('/0')
async def greet_handler0():
    led0.toggle()  # Change the state of the pin
    return '0'


# simultaneously running loop changing led1 state every 5 seconds
# while having route for changing led value at any time
led1 = machine.Pin(3, machine.Pin.OUT)

# Define an asynchronous loop function
async def constant_loop():
    while True:
        led1.toggle()
        await asyncio.sleep(5)

# Create a task for the constant loop before starting the main event loop
async def start_with_background_task():
    asyncio.create_task(constant_loop())  # Schedule the constant loop
    await main()  # Call the existing main() function from MicroAPIgRESTion

@GET('/1')
async def greet_handler1():
    led1.toggle()  # Change the state of the pin
    return '1'

# website serving acting as ui for led switches
@HTML('/index')
async def handler():
    return html_content('index.html')
