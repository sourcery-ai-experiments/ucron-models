from enum import IntEnum


class CourseDuration(IntEnum):
    """
    An enumeration of course duration options.
    """

    ANY = 0
    """Any course."""

    FULL_TERM = 1
    """A full term course."""

    ACCELERATED = 2
    """An accelerated course."""
