from typing import List

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class CourseNumbersView(BaseModel):
    term_code: int
    """The term code."""

    subject_code: str
    """The subject code."""

    course_numbers: List[str]
    """The course numbers."""

    class Config:
        """
        Configuration class for `CourseNumbersView` model.
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
