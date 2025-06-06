from os import environ, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", '7007221986:AAHX004OXGlHO00UcJzsa9GQywMfZkwLa4A')
API_ID = int(environ.get("API_ID", 20583781))
API_HASH = environ.get("API_HASH", "6f6593a285f3949c9b2ae6906b62360c")
SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "8019277081").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", -1002241911142))
GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", -1002241911142))
MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
MONGO_URL = environ.get("MONGO_URL", None)
ARQ_API_URL = environ.get("ARQ_API_URL", None)
ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
RSS_DELAY = int(environ.get("RSS_DELAY", None))
UPSTREAM_REPO = environ.get(
    "UPSTREAM_REPO", "https://github.com/rozari0/NezukoBot.git"
)
