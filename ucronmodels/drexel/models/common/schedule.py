from datetime import datetime, time
from typing import List, Optional

from pydantic import BaseModel, field_serializer
from pydantic.alias_generators import to_camel

from ucronmodels.universal.enums import DaySymbol


class TimeRange(BaseModel):
    """
    Represents a time range with a start and end time.
    """

    start_time: time | str
    """The starting time of the range."""

    end_time: time | str
    """The ending time of the range."""

    class Config:
        """
        Configuration class for `TimeRange` model.
        """

        alias_generator = to_camel
        """A function that is used to generate aliases for model fields."""

        populate_by_name = True
        """Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias."""


class CourseSchedule(BaseModel):
    """
    Defines the schedule for a course including dates, time, days, and location.
    """

    start_date: Optional[datetime | str] = None
    """The start date of the course."""

    end_date: Optional[datetime | str] = None
    """The end date of the course."""

    time: TimeRange | str
    """The time range for the course."""

    days: List[DaySymbol]
    """The days when the course will be held."""

    building: str
    """The building where the course will be conducted."""

    room: str
    """The room number or name where the course will take place."""

    @field_serializer("start_date", when_used="always")
    def serialize_start_date(start_date: Optional[datetime | str]) -> Optional[datetime | str]:
        """
        Field serializer for the `start_date` field.

        Args:
            start_date (Optional[datetime | str]): The start date of the course.

        Returns:
            Optional[datetime | str]: The serialized start date.
        """
        if isinstance(start_date, str):
            try:
                date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S%z")
                return date
            except ValueError:
                pass
        return start_date

    @field_serializer("end_date", when_used="always")
    def serialize_end_date(end_date: Optional[datetime | str]) -> Optional[datetime | str]:
        """
        Field serializer for the `end_date` field.

        Args:
            end_date (Optional[datetime | str]): The end date of the course.

        Returns:
            Optional[datetime | str]: The serialized start date.
        """
        if isinstance(end_date, str):
            try:
                date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S%z")
                return date
            except ValueError:
                pass
        return end_date

    class Config:
        """
        Configuration class for `CourseSchedule` model.
        """

        alias_generator = to_camel
        """A function that is used to generate aliases for model fields."""

        populate_by_name = True
        """Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias."""

        use_enum_values = True
        """Indicates whether to use the enum values themselves instead of the enum instances."""
