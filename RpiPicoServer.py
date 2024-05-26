import uasyncio as asyncio
import network
from machine import Pin
from WIFI_CREDENTIALS import SSID,PASS

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

# Dictionary to store URL handlers
url_handlers = {}

# Decorator to register URL handlers
def route(url):
    def decorator(func):
        url_handlers[url] = func
        return func
    return decorator

# Dispatch incoming HTTP requests to the appropriate handler
async def dispatch_request(reader, writer):
    print('Received request from:', writer.get_extra_info('peername'))

    # Read the first line of the request
    line = await reader.readline()
    line = line.decode().strip()
    method, url, version = line.split()

    # Read the entire request
    while True:
        line = await reader.readline()
        line = line.decode().strip()
        if line == '':
            break
        print('Received header:', line)

    # Call the appropriate handler function
    if url in url_handlers:
        await url_handlers[url](reader, writer)
    else:
        # Send a 404 response if no handler is found
        response = b'HTTP/1.0 404 Not Found\r\n\r\n'
        await writer.awrite(response)
        await writer.aclose()

# Start the async REST API server
async def main():
    # Connect to WiFi
    connect_wifi(SSID, PASS)
    
    # Start server
    server = await asyncio.start_server(dispatch_request, '0.0.0.0', 80)

    print('Server listening on IP: 0.0.0.0')
    print('Server listening on port: 80')

    async with server:
        await server.wait_closed()

# Example usage:
@route('/hello')
async def hello_handler(reader, writer):
    response = b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!\r\n'
    await writer.awrite(response)
    await writer.aclose()

# Example usage:
@route('/dennis')
async def dennis_handler(reader, writer):
    response = b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\nDennis\r\n'
    await writer.awrite(response)
    await writer.aclose()
    
# Run the event loop
asyncio.run(main())