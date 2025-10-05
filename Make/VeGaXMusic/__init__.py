from VeGaXMusic.core.bot import KIMBot
from VeGaXMusic.core.dir import dirr
from pyromod import listen
from VeGaXMusic.core.userbot import Userbot
from VeGaXMusic.misc import dbb, heroku, sudo
from .logging import LOGGER

dirr()

dbb()

heroku()

sudo()

app = KIMBot()

userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
