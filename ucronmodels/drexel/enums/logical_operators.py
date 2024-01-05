from enum import Enum

import strawberry


@strawberry.enum
class LogicalOperator(Enum):
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
