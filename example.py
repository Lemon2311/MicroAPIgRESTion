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

@route('/car')
async def car_handler(**query_params):
    series = query_params.get('series', 'Anonymous')
    model = query_params.get('model', 'Unknown')
    return f'{model},{series}'

@route('/pin')
async def car_handler(**query_params):
    value = query_params.get('value', '0V')
    return f'{value}'

asyncio.run(main())