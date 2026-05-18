import pytest

from entity.user import User


def test_user_is_created_with_trimmed_name() -> None:
    """Test that a user name is normalized when the user is created."""
    # Arrange
    raw_name = "  Alice  "

    # Act
    user = User(name=raw_name)

    # Assert
    assert user.name == "Alice"


def test_user_rejects_blank_name() -> None:
    """Test that a blank user name is rejected."""
    # Arrange
    raw_name = "   "

    # Act & Assert
    with pytest.raises(ValueError, match="name must not be blank"):
        User(name=raw_name)


def test_user_can_create_odd_magic_square() -> None:
    """Test that a user can create a supported odd-order magic square."""
    # Arrange
    user = User(name="Alice")

    # Act
    result = user.can_create_magic_square(order=3)

    # Assert
    assert result is True


def test_user_cannot_create_magic_square_with_invalid_order() -> None:
    """Test that a user cannot create a magic square below the minimum order."""
    # Arrange
    user = User(name="Alice")

    # Act
    result = user.can_create_magic_square(order=2)

    # Assert
    assert result is False
