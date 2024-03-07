from typing import Any

from bson import ObjectId
from pydantic_core import core_schema


class PyObjectId(str):
    """
    Custom class for representing a Pydantic model field as a MongoDB ObjectId.

    This class inherits from `str` and provides methods for validating and serializing
    ObjectIds in Pydantic models.
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _handler: Any) -> core_schema.CoreSchema:
        """
        Returns the Pydantic core schema for this custom ObjectId field.

        Args:
            _source_type (Any): The source type of the field, unused in this implementation.
            _handler (Any): The handler for the field, unused in this implementation.

        Returns:
            core_schema.CoreSchema: The core schema for validating and serializing ObjectIds.
        """
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(cls.validate),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(lambda x: str(x)),
        )

    @classmethod
    def validate(cls, value: str) -> ObjectId:
        """
        Validates that the given string is a valid ObjectId.

        Args:
            value (str): The string to validate as an ObjectId.

        Returns:
            ObjectId: The validated ObjectId.

        Raises:
            ValueError: If the string is not a valid ObjectId.
        """
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)
