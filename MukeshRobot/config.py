class Config(object):
    LOGGER = True
    API_ID =20539290 
    API_HASH = "26e0c15a6803997a3e58d564be36f8f3"
    TOKEN = "6821828314:AAES-su9N9iQrQ4LtD5BWClzJX2jfdfxkns"  
    OWNER_ID=7448520005
    
    SUPPORT_CHAT = "-1002124344872" 
    START_IMG = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
    EVENT_LOGS =-1002124344872
    MONGO_DB_URI= "mongodb://mongo:SKfqQfOojkSyZmLRhxufNMjbyQPgWTFW@nozomi.proxy.rlwy.net:52328"
   
    DATABASE_URL = "postgresql://neondb_owner:npg_FueRAIz48ZaS@ep-solitary-haze-a8lylhhz-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "2ATSJ753CLE402MQ"
    )
    TIME_API_KEY = ""9LMMJQ30GM49

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
