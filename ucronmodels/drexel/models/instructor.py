from ucronmodels.universal.models import MongoDBModel


class Instructor(MongoDBModel):
    """
    A Pydantic model representing a course instructor.
    """

    name: str
    """
    The full name of the instructor.
    """

    @property
    def first_name(self) -> str:
        """
        Extracts the first name from the full name.

        Returns:
            str: The first name of the instructor.
        """
        name_parts = self.name.split()
        return name_parts[0]

    @property
    def last_name(self) -> str:
        """
        Extracts the last name from the full name.

        Returns:
            str: The last name of the instructor, or an empty string if only one part is present.
        """
        name_parts = self.name.split()
        return name_parts[-1] if len(name_parts) > 1 else ""

    university: str
    """
    The name of the university where the instructor works.
    """

    college: str
    """
    The name of the college within the university where the instructor is affiliated.
    """
