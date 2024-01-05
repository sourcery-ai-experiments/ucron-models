from typing import List, Optional

from ucronmodels.universal.models import MongoDBModel

from .course_section import CourseSection
from .credits import Credits
from .prerequisites import Prerequisites


class Course(MongoDBModel):
    """
    A model representing a unique course identified by its subject code, course number, and term code.
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

    term_code: int
    """
    The code that represents the term the course is offered in.
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

    sections: List["CourseSection"] = []
    """
    A list of section offered for a course, if any.
    """

    prerequisites: Optional[Prerequisites]
    """
    Prerequisite courses for this course, if any.
    """

    restrictions: Optional[str] = None
    """
    Enrollment restrictions for the course.
    """
