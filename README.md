
<img src="https://github.com/user-attachments/assets/d58bb4b5-29bd-4bc1-984f-80bfcb1c5cda" alt="MICROAPIGRESTION" style="display:block; margin-left:auto; margin-right:auto;" />


# MicroAPIgRESTion

MicroAPIgRESTion is a lightweight, intuitive library tailored for building Async Restful APIs in MicroPython for use on microcontrollers. It streamlines the process of defining routes and handlers for various HTTP methods and query parameters. Initially crafted for the Raspberry Pi Pico W due to its lightweight nature, MicroAPIgRESTion can also serve webpages.

# Example
```python
from MicroAPIgRESTion import *

# Get request at http://device-ip/hello
@route('/hello')
async def greet_handler():
    return 'Hello!' # will return 'Hello!'

# connect to network with DHCP
connect_wifi('YOUR-SSID', 'YOUR-PASS')

# start server listening on all predefined handlers
asyncio.run(main())

```

# Features
- Route handling simplified with decorators
- Webserver
- Support for all HTTP methods, with explicit support for `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`
- Automatic parsing of query parameters
- WiFi connection management
- Method & Query parameters specific route handlers

# Usage
- [Getting Started](#getting-started)
- [Routing](#routing)
- [Webpage Serving](#webpage-serving)
- [Handling other http methods](#handling-other-http-methods)
- [Starting the server](#starting-the-server)
    - [Network setup](#network-setup)
    - [Actually starting the server](#actually-starting-the-server)
- [A more comprehensive example](#a-more-comprehensive-example)

## Getting Started
The library is the MicroAPIgRESTion.py file, so
```python
from MicroAPIgRESTion import *
```
## Routing
You can define a simple route handler as follows:

```python
@route('/hello')
async def greet_handler():
    return 'Hello!'
```
Whatever the handler function returns will be the response of the request.

The `@route` decorator accepts three attributes: `url`, `method`, and `queryParams`. 

For example:

```python
@route('/hello', 'GET', 'first_name', 'last_name')
async def greet_handler(first_name, last_name):
    return f'Hello, {first_name} {last_name}!'
```

In this example, `/hello` is the `url`, `GET` is the `method`, and `first_name` & `last_name` are the `queryParams`. The `queryParams` need to also be included as parameters for the handler function.

You can also use the `@GET`, `@POST`, `@PUT`, `@DELETE`, `@PATCH` decorators for routing:

```python
@GET('/nips', 'email', 'nrOfNips')
async def nips_handler(email, nrOfNips):
    return f'{email}, {nrOfNips}'
```
## Webpage serving
Webpages can be served, while passing query parameters like so:
```python
@GET('/index', 'name')
async def index_handler(name):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Hello, {name}`s World!</title>
</head>
<body>
    <h1 id="greeting">Loading...</h1>

    <script>
        document.getElementById('greeting').textContent = 'Hello, {name}`s World!';
    </script>
</body>
</html>
"""
```
Or using a separate html file by returning the html_content function and passing as arguments the relative or absolute path of the html file and the query parameters like so:
```python
@HTML('/index0', 'name')
async def handler(name):
    return html_content('index.html', params={'name': name})
```
or
```python
@GET('/index0', 'name')
async def handler(name):
    return html_content('index.html', params={'name': name})
```
*note: this is optional as all files on the device can be accessed at http://device-ip/fileName.ext*
<br>
<br>
**When using the html_content function:**
 - Using css and js is following the usual way by linking the css file and the script file inside the html file like so:
```html
<head>
    <title>Hello, {name}`s World!</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script src="script.js"></script>
</head>
```
*notes for noobs: html, css, js files should be saved on the micropython device*
 - query parameters can be used by using {param} inside any of the html, css, js files like so:
```html
<title>Hello, {name}`s World!</title>
```
And now {name} from the title will have the value of the name query parameter.
## Handling other http methods
Other http methods can be handled by using `@route`.

For example:

```python
@route('/options', 'OPTIONS')
async def options_handler():
    #Do some options or smthn
    return 'Did some options!'
```
This will handle requests made with the method `OPTIONS` at `http://(device-ip)/options`.
`(device-ip)` is a placeholder for the actual ip of the device which is being output in serial when the device connects to WI-Fi.

## Starting the server

- ## Network setup
Prefered way is by saving a file named config.py containing
```python
# config.py
SSID = "SSID" # Your wifi SSID
PASS = "PASS" # Your wifi PASSWORD
```
And importing the network credentials in your main.py
```python
from config import SSID, PASS
```
After that the `connect_wifi()` function can be used to either
```python
# Connect to network with DHCP
connect_wifi(SSID, PASS)
```
or
```python
# Connect to network with static IP
connect_wifi(SSID, PASS, ip="192.168.1.100")
```
*note: The ip of the device is being output in serial when the device connects to WI-Fi when using `connect_wifi()`.*

Another prefered way is by doing your own thing like
```python

SSID = "YOUR-SSID"
PASS = "YOUR-PASS"

# Initialize the WLAN interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to the WiFi network
if not wlan.isconnected():
    print('Connecting to WiFi...')
    wlan.connect(SSID, PASS)
    while not wlan.isconnected():
        pass

# Print the network configuration, containing device ip
print('Connected to WiFi:', wlan.ifconfig())
```
*note: can be useful for custom network setups &/or creating your own network*

- ## Actually starting the server

After route handlers have been defined & a network connection has been established, running 
```python
asyncio.run(main())
```
will start the Async Rest Api, being able to handle requests at routes defined previously, and get requests at http://device-ip/fileName.ext

# A more comprehensive example

## *[Found on example branch](https://github.com/Lemon2311/MicroAPIgRESTion/tree/example)*

```python
# import lib
from MicroAPIgRESTion import *
# importing Pin for use in future handler
from machine import Pin
from config import SSID, PASS

# basic example
@GET('/nips', 'email', 'nrOfNips')
async def nips_handler(email, nrOfNips):
    return f'{email}, {nrOfNips}'

# using device pins
@POST('/initializeDigitalPin', 'pin', 'mode')
async def digitalPin_init_handler(pin, mode):
    
    pin = int(pin)
    
    if mode == 'input':
        Pin(pin, Pin.IN)
    elif mode == 'output':
        Pin(pin, Pin.OUT)
    else:
        return "Invalid"
    
    return f"Digital pin nr.{pin} initialized as {mode}"

@POST('/digitalOutput', 'pin', 'state')
async def digitalPin_out_handler(pin, state):
    
    pin = int(pin)
    
    if state == 'high':
        Pin(pin).value(1)
    elif state == 'low':
        Pin(pin).value(0)
    else:
        return "Invalid"
    
    return f"Pin nr.{pin} set to {state}"

@HTML('/')
async def index_handler():
    return html_content('index.html')

@GET('/index0')
async def index0_handler():
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Hello, name`s World!</title>
</head>
<body>
    <h1 id="greeting">Loading...</h1>

    <script>
        document.getElementById('greeting').textContent = 'Hello, name`s World!';
    </script>
</body>
</html>
"""

# different handlers based on query parameters
@route('/hello', 'GET', 'name')
async def hello_handler(name):
    return f'Hello, {name}!'

@route('/hello')
async def greet_handler():
    return 'Hello!'

# other http methods handlingthon
@route('/options', 'OPTIONS')
async def options_handler():
    #Do some options or smthn
    return 'Did some options!'


# Example usage with DHCP
connect_wifi(SSID, PASS)

# Running server
asyncio.run(main())
```
## Contributions are welcome!</h2>

