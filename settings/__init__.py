from .db import *
from .telegram import *
from .cian import *

DEBUG = os.getenv('DEBUG') or True
SERVICE_HOST = os.getenv('SERVICE_HOST') or '0.0.0.0'
SERVICE_PORT = os.getenv('SERVICE_PORT') or 8080


