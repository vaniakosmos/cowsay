"""
Set up logging and get env vars.

.env must be somewhere in project. File example:
    APP_NAME=app-name-on-heroku
    BOT_TOKEN=bot-token-obtained-from-bot-father
    PORT=5000
"""
import os
import logging
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


DEBUG = True

logging.getLogger('telegram').setLevel(logging.WARNING)
logging.basicConfig(format='%(asctime)s ~ %(levelname)-10s %(name)-25s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    level=logging.DEBUG if DEBUG else logging.INFO)
logging.addLevelName(logging.DEBUG, '🐛 DEBUG')
logging.addLevelName(logging.INFO, '📑 INFO')
logging.addLevelName(logging.WARNING, '🔥 WARNING')
logging.addLevelName(logging.ERROR, '🚨 ERROR')

APP_NAME = os.environ.get('APP_NAME', '5000')
PORT = int(os.environ.get('PORT', '5000'))
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5000')
