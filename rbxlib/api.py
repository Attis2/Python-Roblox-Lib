import requests
from .core import RobloxError, RobloxUser, RobloxGroup, RobloxRole

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

    def get_user(self, user_id: int | str,
                toObj: bool = False) -> RobloxUser | dict:
        """Get user data by ID."""
        endpoint = f"cloud/v2/users/{user_id}"
        user_data = self.make_request(endpoint)
        if not toObj:
            return user_data
        user = RobloxUser(
                path=user_data['path'],
                createTime=user_data['createTime'],
                _id=user_data['id'],
                name=user_data['name'],
                displayName=user_data['displayName'],
                about=user_data['about'],
                locale=user_data['locale'],
                premium=user_data['premium'],
                idVerified=user_data['idVerified'],
                socialNetworkProfiles=None
            )
        try:
            user.socialNetworkProfiles = user_data['socialNetworkProfiles']
        except KeyError:
            pass
        return user

    def get_group(self, group_id: int | str,
                toObj: bool = False, ownerAsObj: bool = False) -> RobloxGroup | dict:
        """Get group info by ID."""
        endpoint = f"cloud/v2/groups/{group_id}"
        user_data = self.make_request(endpoint)
        if not toObj:
            return user_data
        return RobloxGroup(
            path=user_data['path'],
            createTime=user_data['createTime'],
            updateTime=user_data['updateTime'],
            _id=user_data['id'],
            displayName=user_data['displayName'],
            description=user_data['description'],
            owner=self.get_user(user_data['owner'][6:], ownerAsObj),
            memberCount=user_data['memberCount'],
            publicEntryAllowed=user_data['publicEntryAllowed'],
            locked=user_data['locked'],
            verified=user_data['verified']
        )
    
    def get_asset(self, asset_id: int | str) -> dict:
        """Get asset info by ID."""
        endpoint = f"assets/v1/assets/{asset_id}"
        return self.make_request(endpoint)

    def get_roles(self, group_id: int | str) -> list[RobloxRole] | dict:
        """Get every role info by group ID."""
        pass

    def get_user_role(self):
        pass