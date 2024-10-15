# MicroAPIgRESTion

MicroAPIgRESTion is a lightweight, intuitive library tailored for building Async Restful APIs in MicroPython for use on microcontrollers. It streamlines the process of defining routes and handlers for various HTTP methods and query parameters. Initially crafted for the Raspberry Pi Pico W due to its lightweight nature.

# Features
- Route definition simplified with decorators
- Support for all HTTP methods, with explicit support for `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`
- Automatic parsing of query parameters
- WiFi connection management
- Method & Query parameters specific route handlers

# Usage
- [Network setup](#network-setup)
- [Routing](#routing)
- [Webpage Serving](#webpage-serving)
- [Handling other http methods](#handling-other-http-methods)
- [Starting the server](#starting-the-server)
- [A more comprehensive example](#a-more-comprehensive-example)

## Network setup
To get started, save `MicroAPIgRESTion.py` onto the device and insert your wifi credential into the file `config.py`, following the pattern below, then save it on the device.
```
config.py
```
```python
SSID = "SSID" # Your wifi SSID
PASS = "PASS" # Your wifi PASSWORD
```
The ip of the device is being output in serial when the device connects to WI-Fi.
## Importing the library
Then begin using by importing the library:

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
*note: this is optional as all files on the device can be accessed at http://your-ip/fileName.ext*
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
After route handlers have been defined, running 
```python
asyncio.run(main())
```
will start the Async Rest Api, being able to handle requests at routes defined previously.

## A more comprehensive example
```
example.py
```
```python
# import lib
from MicroAPIgRESTion import *
# importing Pin for use in future handler
from machine import Pin

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

# Running server
asyncio.run(main())
```
## Contributions are welcome!</h2>

