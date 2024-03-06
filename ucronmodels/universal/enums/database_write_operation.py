from enum import StrEnum


class DatabaseWriteOperation(StrEnum):
    """
    Defines the types of write operations that can be performed on a database.
    """

    INSERT = "INSERT"
    """
    INSERT: Represents an insert operation.
    """

    UPDATE = "UPDATE"
    """
    UPDATE: Represents an update operation.
    """

    DELETE = "DELETE"
    """
    DELETE: Represents a delete operation.
    """

    INVALID = "INVALID"
    """
    INVALID: Represents an invalid operation.
    """
