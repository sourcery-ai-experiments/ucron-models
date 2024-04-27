from typing import List

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class CollegesView(BaseModel):
    """
    A view model for the colleges view.
    """

    college: str
    """The college."""

    departements: List[str]
    """The departments within the college."""

    subject_codes: List[str]
    """The subjects offered by the college."""

    class Config:
        """
        Configuration class for `CollegesView` model.
        """

        arbitrary_types_allowed = True
        """
        Whether arbitrary types are allowed for field types.
        """

        alias_generator = to_camel
        """
        A function that is used to generate aliases for model fields.
        """

        populate_by_name = True
        """
        Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias.
        """
