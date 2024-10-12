# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22542407"))
API_HASH = getenv("API_HASH", "e162d195c0ab0f1a45f4329bc02e6b4e")
BOT_TOKEN = getenv("BOT_TOKEN", "7564201003:AAGEaICEKcB1JlH3vUwCdJ1G51jDkB8Q4No")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7524828572").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "1002230302878")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002230302878"))
