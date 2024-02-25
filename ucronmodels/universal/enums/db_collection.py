from enum import StrEnum


class DBCollection(StrEnum):
    """
    An enumeration of database collections.
    """

    INSTRUCTOR = "Instructor"
    """
    The collection for storing instructor-related data.
    """

    COURSE = "Course"
    """
    The collection for storing course-related data.
    """

    SECTION = "Section"
    """
    The collection for storing section-related data.
    """

    USER = "User"
    """
    The collection for storing user-related data.
    """
