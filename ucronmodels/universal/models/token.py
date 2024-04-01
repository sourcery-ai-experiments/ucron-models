from typing import List

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class Token(BaseModel):
    """
    Represents an authentication token.
    """

    access_token: str
    """The token that can be used to access resources."""

    token_type: str
    """The type of the token, typically Bearer."""


class TokenData(BaseModel):
    """
    Stores data associated with a token, including the username and scopes.
    """

    username: str
    """The username of the token holder."""

    scopes: List[str]
    """A list of scopes or permissions granted by the token."""
