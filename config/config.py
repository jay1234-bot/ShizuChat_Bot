from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "22498794"
# -------------------------------------------------------------
API_HASH = "478083c48d2a9681d487f60531312856"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7759422732"))
BOT_ID = int(getenv("BOT_ID", "8113054986"))
SUPPORT_GRP = "MBV_CHATS"
UPDATE_CHNL = "MBV_NETWORK"
OWNER_USERNAME = "censored_politicsss"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002379178269"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7759422732").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Badhacker98/ShizuChat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
