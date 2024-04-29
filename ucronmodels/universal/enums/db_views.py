from enum import StrEnum


class DBViews(StrEnum):
    """
    An enumeration of database views.
    """

    DISTINCT_SUBJECT_CODES = "DistinctSubjectCodes"
    """The view for distinct subject codes on the Courses collection."""

    COURSE_CLIENT = "CourseClient"
    """The view for CourseClient."""

    SECTION_CLIENT = "SectionClient"
    """The view for SectionClient."""

    TERM_CODES = "TermCodes"
    """The view for term codes and subject codes grouped by term codes."""

    COLLEGES = "Colleges"
    """The view for colleges and departments grouped by colleges."""

    COURSE_NUMBERS = "CourseNumbers"
    """The view for course numbers grouped by term codes and subject codes."""

    CAMPUS = "Campus"
    """The view for all distinct campuses."""
