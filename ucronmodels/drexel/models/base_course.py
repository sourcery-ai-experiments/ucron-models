from ucronmodels.universal.models import MongoDBModel


class BaseCourse(MongoDBModel):
    """
    A base model representing a unique course identified by its subject code, and course number.
    This base model is term agnostic.
    """

    subject_code: str
    """
    The subject code of the course, such as "CS" for Computer Science.
    """

    course_number: str
    """
    The course number, which is a unique identifier for the course within its subject code.
    """
