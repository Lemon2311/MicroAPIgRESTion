from MicroAPIgRESTion import *

# Example usage:
@route('/hello')
async def hello_handler(**query_params):
    name = query_params.get('name', 'Anonymous')
    id = query_params.get('id', 'Unknown')
    return f'Hello, {name}! Your ID is {id}.'

@route('/nips')
async def nips_handler(**query_params):
    email = query_params.get('email', 'Anonymous')
    nrOfNips = query_params.get('nrOfNips', 'Unknown')
    return f'{email},{nrOfNips}'

# @route can be used for any method and if the method is not specified it will default to GET
@route('/pin','OPTIONS')
async def car_handler(**query_params):
    return 'Do some options or smthn'

# this is basically route('/pin','GET')
@GET('/pin')
async def car_handler(**query_params):
    value = query_params.get('value', '0V')
    return f'{value}'

@POST('/pin')
async def car_handler(**query_params):
    return 'Pin posting like settig a pin state'

asyncio.run(main())