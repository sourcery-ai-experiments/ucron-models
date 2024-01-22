from enum import StrEnum

import strawberry


@strawberry.enum
class LogicalOperator(StrEnum):
    """
    Enumeration for logical operators.
    """

    AND = "and"
    """
    Represents the logical 'AND' operator.
    """

    OR = "or"
    """
    Represents the logical 'OR' operator.
    """
