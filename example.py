from MicroAPIgRESTion import *

@route('/hello', 'GET', 'name')
async def hello_handler(name):
    return f'Hello, {name}!'

@route('/hello', 'GET', 'first_name', 'last_name')
async def greet_handler(first_name, last_name):
    return f'Hello, {first_name} {last_name}!'

@route('/hello')
async def greet_handler():
    return 'Hello!'

asyncio.run(main())