from dataclasses import dataclass


MIN_MAGIC_SQUARE_ORDER = 3
ODD_ORDER_DIVISOR = 2
ODD_ORDER_REMAINDER = 1
BLANK_NAME_ERROR = "name must not be blank"


@dataclass(frozen=True, slots=True)
class User:
    """Represents a MagicSquare user.

    Attributes:
        name: User display name.
    """

    name: str

    def __post_init__(self) -> None:
        """Normalize and validate user data after initialization.

        Raises:
            ValueError: If the user name is blank.
        """
        normalized_name = self.name.strip()

        if not normalized_name:
            raise ValueError(BLANK_NAME_ERROR)

        object.__setattr__(self, "name", normalized_name)

    def can_create_magic_square(self, order: int) -> bool:
        """Check whether the user can create a magic square of the given order.

        Args:
            order: Requested magic square order.

        Returns:
            True when the order is a supported odd magic square order.
        """
        return (
            order >= MIN_MAGIC_SQUARE_ORDER
            and order % ODD_ORDER_DIVISOR == ODD_ORDER_REMAINDER
        )
