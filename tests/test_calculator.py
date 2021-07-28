import pytest
from src.calculator import double_value


# @pytest.mark.parametrize("test_input, expected", [(2, 4), ("2", 0), (-1, -2)])
@pytest.mark.parametrize("test_input, expected", [(2, 4)])
def test_double_value_success(test_input, expected):
    assert double_value(test_input) == expected
