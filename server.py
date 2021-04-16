import asyncio
import logging
import uvicorn

import settings
from app import app, clients


def run_server():
    @app.on_event("startup")
    async def startup():
        await clients.setup(app)
        pass

    @app.on_event("shutdown")
    async def shutdown():
        await clients.shutdown(app)
        pass

    if settings.DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT, debug=settings.DEBUG)


if __name__ == '__main__':
    run_server()
