import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8938666563:AAHEbZmsnls2WqvZ8xb-WANu2nLx2Z8NfxE")
    API_ID = int(os.environ.get("API_ID", "39792511"))
    API_HASH = os.environ.get("API_HASH", "45c445ee134ca8645e7f34ba795849df")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1003897378101")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
