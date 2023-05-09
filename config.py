# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "22193633"))
API_HASH = os.environ.get("API_HASH", "f88cf13c54322ecc6d06eedfddcf9d2c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6201709450:AAFHOaGeKYi6fs2tEQ0_JrUXbnCZpQaUWZ4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5960872422")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Baburphit")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kjfacts6:sbgl593KgNWLTSVc@cluster0.cv6vkc4.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5960872422")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001640254844")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "shortfly") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
