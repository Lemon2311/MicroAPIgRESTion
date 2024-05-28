# MicroAPIgRESTion

MicroAPIgRESTion is a lightweight, intuitive library tailored for building Async Restful APIs in MicroPython for use on microcontrollers. It streamlines the process of defining routes and handlers for various HTTP methods and query parameters. Initially crafted for the Raspberry Pi Pico W due to its lightweight nature.

## Features

- Route definition simplified with decorators
- Support for all HTTP methods, with explicit support for `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`
- Automatic parsing of query parameters
- WiFi connection management

## Usage

To get started, save `MicroAPIgRESTion.py` onto the device and create a `WIFI_CREDENTIALS.py` file following the pattern/structure from `WIFI_CREDENTIALS(example).py`, then save it on the device.
```
WIFI_CREDENTIALS.py
```
```python
SSID = "SSID"
PASS = "PASS"
```
Begin by importing the library:

```python
from MicroAPIgRESTion import *

```

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
Other http methods can be handled by using `@route`:

For example:

```python
@route('/options', 'OPTIONS')
async def options_handler():
    return 'Do some options or smthn'
```
This will handle requests made with the method `OPTIONS` at `http://(device-ip)/options`.
`(device-ip)` is a placeholder for the actual ip of the device which is being output in serial when the device connects to WI-Fi.

After route handlers have been defined, running 

```python
asyncio.run(main())
```
will start the Async Rest Api, being able to handle requests at routes defined previously.

A more comprehensive example of use would be:
```
example.py
```
```python
from MicroAPIgRESTion import *

@GET('/nips', 'email', 'nrOfNips')
async def nips_handler(email, nrOfNips):
    return f'{email}, {nrOfNips}'

@GET('/car', 'series', 'model')
async def car_handler(series, model):
    return f'{model}, {series}'

@POST('/pin', 'value')
async def pin_handler(value):
    return f'Pin set to {value}V'

@route('/hello', 'GET', 'name')
async def hello_handler(name):
    return f'Hello, {name}!'

@route('/hello', 'GET', 'first_name', 'last_name')
async def greet_handler(first_name, last_name):
    return f'Hello, {first_name} {last_name}!'

@route('/hello')
async def greet_handler():
    return 'Hello!'

@route('/options', 'OPTIONS')
async def options_handler():
    return 'Do some options or smthn'

asyncio.run(main())
```
## Contributions are welcome!</h2>

