from AbhiXmusic.core.bot import Anony
from AbhiXmusic.core.dir import dirr
from AbhiXmusic.core.git import git
from AbhiXmusic.core.userbot import Userbot
from AbhiXmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
