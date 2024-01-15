from typing import Any, Optional

from pydantic import BaseModel, field_validator
from pydantic.alias_generators import to_camel

from .prerequisites import Prerequisites


class PrerequisitesContainer(BaseModel):
    """
    A model that will be used to transport prerequisites information for a course.
    """

    subject_code: str
    """
    The subject code of the course, such as "CS" for Computer Science.
    """

    course_number: str
    """
    The course number, which is a unique identifier for the course within its subject code.
    """

    prerequisites: Optional[Prerequisites]
    """
    Prerequisite courses for this course, if any.
    """

    @field_validator("prerequisites", mode="before")
    @classmethod
    def prerequisitesValidator(cls, v: Any) -> Optional[Prerequisites]:
        """
        Allows the Prerequisites model to use custom deserialization logic.
        """
        return Prerequisites.from_dict(v)

    class Config:
        """
        Configuration class for `MongoDBModel` model.
        """

        alias_generator = to_camel
        """
        A function that is used to generate aliases for model fields.
        """

        populate_by_name = True
        """
        Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias.
        """
