from typing import List

from ..database import CourseDB
from .section_client import SectionClient


class CourseClient(CourseDB):
    """
    This model extends the CourseDB model and contains a list of associated section client models.
    """

    sections: List[SectionClient]
    """The list of sections."""
