import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ['AUTH_USERS'].split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """**Hey! Dear!**

💡 I am TG Media Search Bot

<code>Here you can search files in inline mode. Just press follwing buttons and start searching </code>

👲 Bot By: @MaxxBots

"""

SHARE_BUTTON_TEXT = ' 𝐶ℎ𝑒𝑐𝑘𝑜𝑢𝑡 𝑇ℎ𝑖𝑠 {username} 𝐵𝑜𝑡 . 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝐹𝑖𝑙𝑒𝑠 𝑆𝑒𝑎𝑟𝑐ℎ 🔍 𝐵𝑜𝑡 😊. '
