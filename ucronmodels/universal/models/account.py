from typing import Optional

from .mongodb_model import MongoDBModel
from .pyobjectid import PyObjectId


class Account(MongoDBModel):
    """
    Represents an account linked to a user, containing authentication and authorization details.
    """

    user_id: PyObjectId
    """The unique identifier of the user this account is associated with."""

    type: str
    """The type of account, describing the authentication strategy."""

    provider: str
    """The name of the provider for third-party authentication."""

    provider_account_id: str
    """The unique identifier for the user given by the provider."""

    refresh_token: Optional[str]
    """A token that can be used to obtain a new access token when the current one expires."""

    access_token: Optional[str]
    """The token that grants access to the provider's resources."""

    expires_at: Optional[int]
    """The timestamp (in seconds) when the access token expires."""

    token_type: Optional[str]
    """The type of token issued."""

    scope: Optional[str]
    """The scope of access granted by the access token."""

    id_token: Optional[str]
    """A JWT that contains the user's profile information."""

    session_state: Optional[str]
    """An opaque value used by the provider to maintain session state."""
