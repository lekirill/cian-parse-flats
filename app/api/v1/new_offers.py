from starlette.requests import Request
from starlette.responses import JSONResponse

from app.cian_data_processing import fetch_new_offers


async def get_new_offers(request: Request):
    await fetch_new_offers(request.app)
    return JSONResponse({'msg': 'start fetch offers'},
                        status_code=200
                        )
