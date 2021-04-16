import asyncio

from .db import DBClient
from .rest import RestClient
from .scheduler import Scheduler
from .tg_bot import TelegramNotifier

import settings


async def setup(app):
    loop = asyncio.get_event_loop()
    app.db = DBClient(settings.DB, loop=loop)
    app.rest = RestClient(app, loop)
    app.scheduler = Scheduler(app, loop=loop)
    app.tg = TelegramNotifier(app)
    await app.db.setup()
    await app.scheduler.setup()


async def shutdown(app):
    await app.db.close()
    await app.scheduler.shutdown()


