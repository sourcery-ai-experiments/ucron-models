from typing import Optional

from pydantic import BaseModel

from .credits import Credits


class CourseRequirement(BaseModel):
    """
    Represents a course requirement for another dependant course.
    """

    title: Optional[str] = None
    """The title of the course. This field only used when subject code and course number are not available."""

    subject_code: Optional[str] = None
    """The subject code of the course, such as "CS" for Computer Science."""

    course_number: Optional[str] = None
    """The course number, which is a unique identifier for the course within its subject code."""

    minimum_grade: Optional[str] = None
    """The minimum grade required to statisfy this course requirement."""

    credits: Optional[Credits] = None
    """Number of possible credits for a course requirement."""
