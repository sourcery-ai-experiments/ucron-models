# from calendar import Day
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from pydantic.alias_generators import to_camel

from ucronmodels.universal.enums import Day


class TimeRange(BaseModel):
    """
    Represents a time range with a start and end time.
    """

    start_time: str
    """
    The starting time of the range, represented as a string.
    """

    end_time: str
    """
    The ending time of the range, represented as a string.
    """

    class Config:
        """
        Configuration class for `TimeRange` model.
        """

        alias_generator = to_camel
        """
        A function that is used to generate aliases for model fields.
        """

        populate_by_name = True
        """
        Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias.
        """


class CourseSchedule(BaseModel):
    """
    Defines the schedule for a course including dates, time, days, and location.
    """

    start_date: Optional[datetime | str] = None
    """
    The start date of the course.
    """

    end_date: Optional[datetime | str] = None
    """
    The end date of the course.
    """

    time: TimeRange | str
    """
    The time range for the course.
    """

    days: List[Day]
    """
    The days when the course will be held.
    """

    building: str
    """
    The building where the course will be conducted.
    """

    room: str
    """
    The room number or name where the course will take place.
    """

    class Config:
        """
        Configuration class for `CourseSchedule` model.
        """

        alias_generator = to_camel
        """
        A function that is used to generate aliases for model fields.
        """

        populate_by_name = True
        """
        Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias.
        """

        use_enum_values = True
        """
        Indicates whether to use the enum values themselves instead of the enum instances.
        """
