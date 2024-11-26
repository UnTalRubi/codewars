import pytest
from src.unique_in_order import unique_in_order

@pytest.mark.parametrize(
        "input, expected",
        [
            ("",[]),
            ([],[]),
            ((),[]),
            ("A",["A"]),
            (["A"],["A"]),
            (("A",),["A"]),
            ("AA",["A"]),
            ("AAAABBBCCDAABBB",["A", "B", "C", "D", "A", "B"]),
            ("ABBCcA",["A", "B", "C", "c", "A"]),
            ([1, 2, 3, 3, -1],[1, 2, 3, -1]),
            (["a", "b", "b", "a"],["a", "b", "a"])
        ]
)

def test_unique_in_order(input, expected):
    assert unique_in_order(input) == expected