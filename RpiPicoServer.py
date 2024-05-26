import uasyncio as asyncio
import network
from machine import Pin

led = Pin("LED", Pin.OUT)

# Connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi:', wlan.ifconfig())

# Handle incoming HTTP requests
async def handle_request(reader, writer):
    print('Received request from:', writer.get_extra_info('peername'))
    led.toggle() 

    # Read the entire request
    while True:
        line = await reader.readline()
        line = line.decode().strip()
        if line == '':
            break
        print('Received header:', line)

    # Send the response
    response = b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!\r\n'
    await writer.awrite(response)
    await writer.aclose()

# Start the async REST API server
async def main():
    # Connect to WiFi
    connect_wifi("SSID", "PASS")
    
    # Start server
    server = await asyncio.start_server(handle_request, '0.0.0.0', 80)

    print('Server listening on IP: 0.0.0.0')
    print('Server listening on port: 80')

    async with server:
        await server.wait_closed()

# Run the event loop
asyncio.run(main())
