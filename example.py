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
