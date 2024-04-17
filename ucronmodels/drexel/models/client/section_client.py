from typing import List
from ucronmodels.drexel.models.database import SectionDB, InstructorDB


class SectionClient(SectionDB):
    """
    This model extends the SectionDB model and contains a list of instructor models.
    """

    instructors: List[InstructorDB]
    """The list of instructors teaching the course section."""