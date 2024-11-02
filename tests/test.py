import os
from dotenv import load_dotenv
from rbxlib.api import RobloxAPI

load_dotenv()
client_id = os.getenv("ROBLOX_CLIENT_ID")
client_secret = os.getenv("ROBLOX_SECRET")
api_key = os.getenv("ROBLOX_API_KEY")

roblox_api = RobloxAPI(client_id, client_secret, api_key)

# Test here
try:
    print(roblox_api.get_asset(12268509034))
except:
    pass