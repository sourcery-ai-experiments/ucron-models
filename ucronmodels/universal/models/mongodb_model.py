from typing import Optional

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel

from .pyobjectid import PyObjectId


class MongoDBModel(BaseModel):
    """
    Base model for MongoDB documents, providing common configurations and fields.
    """

    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    """
    The unique identifier for the model, mapped to the MongoDB '_id' field.
    """

    class Config:
        """
        Configuration class for `MongoDBModel` model.
        """

        arbitrary_types_allowed = True
        """
        Whether arbitrary types are allowed for field types.
        """

        alias_generator = to_camel
        """
        A function that is used to generate aliases for model fields.
        """

        populate_by_name = True
        """
        Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias.
        """
