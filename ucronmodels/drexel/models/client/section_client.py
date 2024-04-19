from typing import Sequence

from ..database import InstructorDB, SectionDB


class SectionClient(SectionDB):
    """
    This model extends the SectionDB model and contains a list of instructor models.
    """

    instructors: Sequence[InstructorDB]
    """The list of instructors teaching the course section."""
