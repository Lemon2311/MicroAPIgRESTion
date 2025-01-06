import RUN
from RUN import *
from MicroAPIgRESTion import *
from wifi_credentials import *


#Defineing routes for changing device files so that connecting device via usb isn`t required anymore
@GET('/file','filename')
async def code_return_handler(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


@POST('/file','filename','value')
async def code_set_handler(filename,value):
    with open(filename, 'w') as file:
        content = file.write(value)
    return content


# Wi-Fi connection
connect_wifi(SSID, PASS, ip="192.168.1.111")

# Run the asyncio event loop serving routes on all files defined in main.py and in RUN.py
# and running the device loop and Interupt for the toggle switch via function imported from RUN.py
asyncio.run(start_with_background_task())
