from typing import Any, Optional

from pydantic import field_validator

from ucronmodels.universal.models import MongoDBModel

from ..common import Credits, Prerequisites


class CourseDB(MongoDBModel):
    """
    A database model representing a unique course identified by its subject code and course number.
    """

    subject_code: str
    """
    The subject code of the course, such as "CS" for Computer Science.
    """

    course_number: str
    """
    The course number, which is a unique identifier for the course within its subject code.
    """

    course_title: Optional[str] = None
    """
    The title of the course.
    """

    description: Optional[str] = None
    """
    The course description.
    """

    credits: Optional["Credits"] = None
    """
    Number of possible credits for a Course.
    """

    college: Optional[str] = None
    """
    The college in which the Course is offered.
    """

    department: Optional[str] = None
    """
    The department, within the college, responsible for the Course.
    """

    restrictions: Optional[str] = None
    """
    Enrollment restrictions for the course.
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
        if isinstance(v, Prerequisites):
            return v
        return Prerequisites.from_dict(v) if v is not None else None
