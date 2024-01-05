from calendar import Day
from enum import IntEnum


class DaySymbol(IntEnum):
    """
    Enumeration for days of the week using symbols.
    """

    M = Day.MONDAY
    """
    Monday (0)
    """

    T = Day.TUESDAY
    """
    Tuesday (1)
    """

    W = Day.WEDNESDAY
    """
    Wednesday (2)
    """

    R = Day.THURSDAY
    """
    Thursday (3)
    """

    F = Day.FRIDAY
    """
    Friday (4)
    """
