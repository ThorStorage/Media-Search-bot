# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'

# Bot settings
MAX_RESULTS = 10
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """**Hey! Dear!**

💡 I am TG Media Search Bot

<code>Here you can search files in inline mode. Just press follwing buttons and start searching </code>

👲 Bot By: @MaxxBots

"""

SHARE_BUTTON_TEXT = ' 𝐶ℎ𝑒𝑐𝑘𝑜𝑢𝑡 𝑇ℎ𝑖𝑠 {username} 𝐵𝑜𝑡 . 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝐹𝑖𝑙𝑒𝑠 𝑆𝑒𝑎𝑟𝑐ℎ 🔍 𝐵𝑜𝑡 😊. '
