import pytest
from src.sum_of_array_singles import sum_arrays

@pytest.mark.parametrize(
        "input, expected",
        [
            ([4,5,7,5,4,8],15),
            ([9, 10, 19, 13, 19, 13],19),
            ([16, 0, 11, 4, 8, 16, 0, 11],12),
            ([5, 17, 18, 11, 13, 18, 11, 13],22),
            ([5, 10, 19, 13, 10, 13],24)
        ]
)

def test_sum_arrays(input, expected):
    assert sum_arrays(input) == expected