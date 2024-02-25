from enum import StrEnum


class DBViews(StrEnum):
    """
    An enumeration of database views.
    """

    DISTINCT_SUBJECT_CODES = "DistinctSubjectCodes"
    """
    The view for distinct subject codes on the Courses collection.
    """
