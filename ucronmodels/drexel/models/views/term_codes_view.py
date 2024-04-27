from typing import List

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class TermCodesView(BaseModel):
    """
    A view model for the term codes view.
    """

    term_code: int
    """The term code."""

    subject_codes: List[str]
    """The subject codes."""

    class Config:
        """
        Configuration class for `TermCodesView` model.
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
