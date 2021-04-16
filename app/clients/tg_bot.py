import settings
import logging

logger = logging.getLogger(__name__)


class TelegramNotifier:

    def __init__(self, app):
        self.app = app
        self.tg_base_url = settings.TG_API_BASE_URL

    async def send_message(self, msg):
        response, status, content_type = await self.app.rest.request(
            'POST',
            url=self.tg_base_url + 'sendMessage',
            params={
                'chat_id': settings.TG_NOTIFICATION_CHANNEL_NAME,
                'text': msg,
                'parse_mode': 'HTML'
            }
        )
        logger.info(f"""status: {status}
        content_type: {content_type}
        response: {response}
        """)
