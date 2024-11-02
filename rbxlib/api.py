import requests
from .core import RobloxError

class RobloxAPI:
    BASE_URL = "https://apis.roblox.com"

    def __init__(self, _id: str = None, _secret: str = None, _key: str = None) -> None:
        """
        Initializes the RobloxAPI instance.

        Parameters:
        _id (str): Client ID for authentication (optional).
        _secret (str): Client Secret for authentication (optional, but required if _key is None).
        _key (str): API Key for access (optional, but required if _secret is None).
        _cookies (str): Cookies for session management (optional).
        
        Raises:
        ValueError: If both _secret and _key are None.
        """
        if _secret is None and _key is None:
            raise ValueError("Cannot work without a Client Secret nor an API Key.")
        self._id = _id
        self._secret = _secret
        self._key = _key

    def make_request(self, endpoint: str, params = None):
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            "x-api-key": f"{self._key}"
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise RobloxError(f"Error: {response.status_code} - {response.text}")
        return response.json()

    def get_user(self, user_id: int | str):
        """Get user data by ID."""
        endpoint = f"cloud/v2/users/{user_id}"
        return self.make_request(endpoint)
    
    def get_group(self, group_id: int | str):
        """Get group info by ID."""
        endpoint = f"cloud/v2/groups/{group_id}"
        return self.make_request(endpoint)
    
    def get_asset(self, asset_id: int | str):
        """Get asset info by ID."""
        endpoint = f"cloud/v2/.../{asset_id}"
        return self.make_request(endpoint)