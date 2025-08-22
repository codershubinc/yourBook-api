from typing import TypedDict


class User_Config_Schema(TypedDict):
    name: str
    email: str
    avatar_uri: str
    user_type: str
    createdAt: str
    updatedAt: str
