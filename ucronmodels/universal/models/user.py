from typing import List, Optional

from pydantic import BaseModel, EmailStr, validator

from .account import Account
from .mongodb_model import MongoDBModel


class UserDB(MongoDBModel):
    """
    Represents a user in the database.
    """

    name: Optional[str]
    """The name of the user."""

    email: Optional[str]
    """The email of the user."""

    image: Optional[str]
    """A URL to the user's profile image."""

    hashed_password: Optional[str]
    """The hashed password of the user."""

    scopes: list[str]
    """A list of scopes or permissions assigned to the user."""

    accounts: List[Account]
    """A list of Account objects associated with the user."""


class User(MongoDBModel):
    """
    Client user model.
    """

    name: Optional[str]
    """The name of the user."""

    email: Optional[str]
    """The email of the user."""

    image: Optional[str]
    """A URL to the user's profile image."""

    scopes: list[str]
    """A list of scopes or permissions assigned to the user."""

    accounts: List[Account]
    """A list of Account objects associated with the user."""


class CreateUserRequest(BaseModel):
    """
    Defines the request schema for creating a new user, including validations for the password.
    """

    email: EmailStr
    """The email address of the new user."""

    password: str
    """The password for the new user"""

    @validator("password")
    @classmethod
    def password_strength(cls, value: str) -> str:
        """
        Validates the password strength based on length, digit inclusion, case sensitivity, and special character inclusion.

        Args:
            value (str): The password to validate.

        Returns:
            str: The validated password.

        Raises:
            ValueError: If the password does not meet the required criteria.
        """
        if not len(value) >= 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char in "!@#$%^&*()-_=+[]{}};:,.<>?/|\\" for char in value):
            raise ValueError("Password must contain at least one special character")
        return value
