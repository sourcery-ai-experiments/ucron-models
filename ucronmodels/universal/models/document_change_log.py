from typing import Optional

from pydantic import BaseModel

from ..enums import DatabaseWriteOperation, DBCollection
from .pyobjectid import PyObjectId


class DocumentChangeLog(BaseModel):
    """
    Reflects the changes made to a document in the database.
    """

    id: Optional[PyObjectId]
    """
    The unique identifier for the document.
    """

    collection: DBCollection
    """
    The database collection.
    """

    operation: DatabaseWriteOperation
    """
    The type of write operation performed on the document.
    """

    def __str__(self) -> str:
        id_str = f" for document with ID {self.id}" if self.id else ""
        extra_attrs = ", ".join([f"{key}: {value}" for key, value in self.model_extra.items()])
        extra_str = f", with attributes {extra_attrs}" if self.model_extra else ""
        return f"{self.operation} in collection '{self.collection}'{id_str}{extra_str}."

    class Config:
        """
        Configuration class for `DocumentChangeLog` model.
        """

        extra = "allow"
        """
        Whether to ignore, allow, or forbid extra attributes during model initialization.
        """

        use_enum_values = True
        """
        Indicates whether to use the enum values themselves instead of the enum instances.
        """
