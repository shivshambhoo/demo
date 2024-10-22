import pytest
from calculator import add_numbers

def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-1, -1) == -2
    assert add_numbers(0, 0) == 0
    assert add_numbers(2.5, 3.5) == 6.0  # Ensure there are no hidden characters here

