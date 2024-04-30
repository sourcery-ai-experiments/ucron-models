from datetime import datetime
from typing import Optional, Self, Sequence

from pydantic import model_validator
from pydantic.alias_generators import to_camel

from ucronmodels import MongoDBModel, PyObjectId

from ..common import CourseSchedule, Credits


class SectionDB(MongoDBModel):
    """
    A database model representing a specific section or class of a course.
    """

    subject_code: str
    """The subject code of the course, such as "CS" for Computer Science."""

    course_number: str
    """The course number, which is a unique identifier for the course within its subject code."""

    section: str
    """The section identifier for the course, e.g., "001" or "A01"."""

    term_code: int
    """The code that represents the term the course is offered in."""

    crn: int
    """The Course Reference Number (CRN) associated with this course section."""

    credits: Optional["Credits"] = None
    """Number of possible credits for a Course Section."""

    instruction_type: str
    """The type of instruction for the course section, such as "Lecture" or "Lab"."""

    instruction_method: str
    """The method of instruction for the course section, such as "In-Person" or "Online"."""

    instructors: Sequence[PyObjectId]
    """The list of instructors teaching the course section."""

    campus: Optional[str] = None
    """Campus where the course is being taught."""

    max_enroll: Optional[int] = None
    """The maximum number of students that can enroll in the course section."""

    enroll: Optional[int] = None
    """The current number of students enrolled in the course section."""

    comments: Optional[str] = None
    """Additional comments regarding the course section."""

    schedule: CourseSchedule
    """The schedule related information about the course section."""

    course_duration_in_weeks: int = 0
    """The duration of the course in weeks."""

    class_duration: int = 0
    """The duration of the class in minutes."""

    @model_validator(mode="after")
    def validate_course_duration(self) -> Self:
        if isinstance(self.schedule.start_date, datetime) and isinstance(
            self.schedule.end_date, datetime
        ):
            self.course_duration_in_weeks = (
                self.schedule.end_date - self.schedule.start_date
            ).days // 7
        return self  # type: ignore

    @model_validator(mode="after")
    def validate_class_duration(self) -> Self:
        self.class_duration = self.schedule.time.end_time - self.schedule.time.start_time
        return self  # type: ignore

    def __hash__(self) -> int:
        """
        Compute a hash based on the Course Reference Number (CRN).

        Returns:
            int: The computed hash value.
        """
        return hash(self.crn)

    class Config:
        """
        Configuration class for `CourseSection` model.
        """

        arbitrary_types_allowed = True
        """Whether arbitrary types are allowed for field types."""

        alias_generator = to_camel
        """A function that is used to generate aliases for model fields."""

        populate_by_name = True
        """Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias."""
