from starlette.responses import JSONResponse


async def ping(request):
    return JSONResponse({'message': 'pong'},
                        status_code=200)
