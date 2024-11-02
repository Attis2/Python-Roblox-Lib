import os

class RobloxError(Exception):
    """Custom exception for Roblox API errors."""
    pass

def check_environment_variables(vars: list):
    """Check if required environment variables are set."""
    for var in vars:
        if os.getenv(var) is None:
            raise EnvironmentError(f"Environment variable '{var}' is not set.")

def initialize():
    """Check environment variables and perform any necessary setup."""
    required_vars = ["ROBLOX_CLIENT_ID", "ROBLOX_SECRET", "ROBLOX_API_KEY"]
    check_environment_variables(required_vars)