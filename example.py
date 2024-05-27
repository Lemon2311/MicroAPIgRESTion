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