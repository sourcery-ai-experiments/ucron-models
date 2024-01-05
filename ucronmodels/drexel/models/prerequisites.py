from typing import List

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel

from ..enums import LogicalOperator
from .course_requirement import CourseRequirement


class Prerequisites(BaseModel):
    """
    Represents the requirements needed for a course.
    """

    prerequisites: List[CourseRequirement | type["Prerequisites"]] = []
    """
    A list of required courses requirements or nested prerequisites.
    """

    logical_operator: LogicalOperator = Field(default=LogicalOperator.AND, validate_default=True)
    """
    The logical operator (e.g., AND, OR) used to combine the prerequisites.
    """

    class Config:
        """
        Configuration settings for the PreRequisites model.
        """

        use_enum_values = True
        """
        Indicates whether to use the enum values themselves instead of the enum instances.
        """

        validate_assignment = True
        """
        Determines if assignments to fields should be validated.
        """

        alias_generator = to_camel
        """
        A function that is used to generate aliases for model fields.
        """

        populate_by_name = True
        """
        Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias.
        """
