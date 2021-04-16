import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.cian_data_processing import fetch_new_offers, send_notification


class Scheduler:

    def __init__(self, app, loop):
        self.app = app
        self.scheduler = AsyncIOScheduler({
            'event_loop': loop,
            'apscheduler.timezone': 'UTC',
        })

    async def setup(self):
        self.scheduler.add_job(fetch_new_offers, 'interval', minutes=2, kwargs={'app': self.app})
        await asyncio.sleep(15)
        self.scheduler.add_job(send_notification, 'interval', minutes=2, kwargs={'app': self.app})
        self.scheduler.start()

    async def shutdown(self):
        await self.scheduler.shutdown()
