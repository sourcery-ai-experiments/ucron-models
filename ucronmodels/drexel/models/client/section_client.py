from typing import List

from ..database import InstructorDB, SectionDB


class SectionClient(SectionDB):
    """
    This model extends the SectionDB model and contains a list of instructor models.
    """

    instructors: List[InstructorDB]
    """The list of instructors teaching the course section."""
