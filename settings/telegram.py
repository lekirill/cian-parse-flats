import os

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN') or 'testtestetest'
TG_API_BASE_URL = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/'
TG_NOTIFICATION_CHANNEL_NAME = os.getenv('TG_NOTIFICATION_CHANNEL_NAME') or '1234'
