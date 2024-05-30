from MicroAPIgRESTion import *
from machine import Pin

@GET('/nips', 'email', 'nrOfNips')
async def nips_handler(email, nrOfNips):
    return f'{email}, {nrOfNips}'

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

@route('/hello', 'GET', 'name')
async def hello_handler(name):
    return f'Hello, {name}!'

@route('/hello', 'GET', 'first_name', 'last_name')
async def greet_handler(first_name, last_name):
    return f'Hello, {first_name} {last_name}!'

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

@GET('/index0', 'name')
async def handler(name):
    return html_content('index.html', params={'name': name})

@route('/hello')
async def greet_handler():
    return 'Hello!'

@route('/options', 'OPTIONS')
async def options_handler():
    return 'Do some options or smthn'

asyncio.run(main())