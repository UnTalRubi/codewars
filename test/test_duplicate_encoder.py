import pytest
from src.duplicate_encoder import encode

@pytest.mark.parametrize(
        "input, expected",
        [
            ("din","((("),
            ("recede","()()()"),
            ("(( @","))(("),
            ("Success",")())())")
        ]
)

def test_duplicate(input, expected):
    assert encode (input) == expected