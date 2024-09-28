class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6861906489"
    sudo_users = ["6861906489"]
    GROUP_ID = "-1002337505439"
    TOKEN = "7624228426:AAEC_qtuQoQh1KDr7xhl6uDZqk3f_2jHMk4"
    mongo_url = "mongodb+srv://mybotwaifu123:<db_mybotwaifu123>@cluster0.48wu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    BOT_USERNAME = "make_your_waifu_bot"   
    api_id = "24331006"
    api_hash = "783a6c919b56b9dca14a16bc835fea26"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
