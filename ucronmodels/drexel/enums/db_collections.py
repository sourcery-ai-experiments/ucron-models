from enum import StrEnum


class DBCollection(StrEnum):
    """
    An enumeration of database collections.
    """

    INSTRUCTORS = "Instructors"
    """
    The collection for storing instructor-related data.
    """

    BASE_COURSES = "BaseCourses"
    """
    The collection for storing base-course-related data.
    """

    COURSES = "Courses"
    """
    The collection for storing course-related data.
    """
