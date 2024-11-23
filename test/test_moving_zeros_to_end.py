import pytest
from src.moving_zeros_to_end import move_zeros

@pytest.mark.parametrize(
        "input, output",
        [
            ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
            ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9], [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            ([0, 0], [0, 0]),
            ([0], [0]),
            ([], [])
        ]
)

def test_move_zeros(input, output):
    assert move_zeros (input) == output