from pydantic import BaseModel


class Credits(BaseModel):
    """
    Number of possible credits for a Course or Course Section.
    """

    minimum: float
    """
    Minimum possible credits for a Course.
    """

    maximum: float
    """
    Maximum possible credits for a Course.
    """
