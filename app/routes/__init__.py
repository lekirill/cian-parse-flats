from starlette.routing import Route, Mount

from app.api.healthcheck import ping
from app.api.v1 import new_offers

route_list = [
    Route('/ping', ping.ping),

    # Mount('/v1', name='v1', routes=[
    #     Route('/fetch_new_offers', new_offers.get_new_offers, methods=['POST', ]),
    # ]),
]

