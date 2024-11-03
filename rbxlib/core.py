import os

class RobloxError(Exception):
    """Custom exception for Roblox API errors."""
    pass

class RobloxUser:
    def __init__(self, path: str, createTime: str, _id: str, name: str,
                displayName: str, about: str, locale: str, premium: bool,
                idVerified: bool, socialNetworkProfiles: dict):
        self.path = path
        self.createTime = createTime
        self._id = _id
        self.name = name
        self.displayName = displayName
        self.about = about
        self.locale = locale
        self.premium = premium
        self.idVerified = idVerified
        self.socialNetworkProfiles = socialNetworkProfiles

def check_environment_variables(vars: list):
    """Check if required environment variables are set."""
    for var in vars:
        if os.getenv(var) is None:
            raise EnvironmentError(f"Environment variable '{var}' is not set.")

def initialize():
    """Check environment variables and perform any necessary setup."""
    required_vars = ["ROBLOX_CLIENT_ID", "ROBLOX_SECRET", "ROBLOX_API_KEY"]
    check_environment_variables(required_vars)