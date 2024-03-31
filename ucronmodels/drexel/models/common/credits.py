from typing import Any

from pydantic import BaseModel


class Credits(BaseModel):
    """
    Number of possible credits for a Course or Course Section.
    """

    minimum: float
    """Minimum possible credits for a Course."""

    maximum: float
    """Maximum possible credits for a Course."""

    def __add__(self, other: Any) -> "Credits":
        """
        Adds the credits from another Credits instance to this instance.

        Args:
            other (Any): The other Credits instance to add.

        Returns:
            Credits: A new Credits instance with the summed minimum and maximum credits.

        Raises:
            NotImplemented: If `other` is not an instance of Credits.
        """
        if not isinstance(other, Credits):
            return NotImplemented
        return Credits(minimum=self.minimum + other.minimum, maximum=self.maximum + other.maximum)
