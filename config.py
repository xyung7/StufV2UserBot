# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_VER = "0.1.0@master"
BRANCH = "master"
LOG_CHAT = int(getenv("LOG_CHAT") or 0)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_USERNAME = getenv("SPOTIFY_USERNAME", "")
MONGO_DB = getenv("MONGO_DB", "")
ALIVE_IMG = getenv("ALIVE_IMG", "")
DB_URL = getenv("DATABASE_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1Z2Z2c2ZWdPaFVlcW8zNzRsSTh6aktIMTlrUEVNcTNBdFNuRw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "stufgrup")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1N0dWZVQi9TdHVmdjJVc2VyYm90").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
