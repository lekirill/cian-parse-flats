import settings
from app.routes import route_list

from starlette.applications import Starlette

app = Starlette(debug=settings.DEBUG, routes=route_list)
