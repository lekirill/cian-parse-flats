import asyncio
import json
import logging

import settings

from app.cian_data_processing.preparation import prepare_data, prepare_string_to_send
from app.cian_data_processing.db_interaction import insert_to_database, extract_data_to_notify

logger = logging.getLogger(__name__)


async def fetch_new_offers(app):
    resp, status, content_type = await app.rest.request(
        'POST',
        url=settings.CIAN_URL_TO_REQUEST,
        data=json.dumps(settings.CIAN_PAYLOAD),
    )
    if status == 200 and isinstance(resp, dict):
        loop = asyncio.get_event_loop()
        data_to_insert = await loop.run_in_executor(None, prepare_data, resp)
        await insert_to_database(app, data_to_insert)


async def send_notification(app):
    data_to_send = await extract_data_to_notify(app)
    if data_to_send:
        msg = prepare_string_to_send(data_to_send)
        await app.tg.send_message(msg)
    else:
        logger.info('no offers to send')


