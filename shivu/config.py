class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6861906489"
    sudo_users = ["6861906489"]
    GROUP_ID = "-1002337505439"
    TOKEN = "6600186454:AAFLZH3zYUM3V1q_a7RkQ6nnGlHiz5hRxoU"
    mongo_url = "mongodb+srv://Epic2:w85NP8dEHmQxA5s7@cluster0.tttvsf9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://envs.sh/SqR.jpg"]
    UPDATE_CHAT = "FLEX_BOTS_NEWS"
    BOT_USERNAME = "Grabbing_Your_Waifu_Bot"
    CHARA_CHANNEL_ID = "-1002009998662"
    api_id = "24331006"
    api_hash = "f6cadf28523943f525e706e6ace8a250"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
