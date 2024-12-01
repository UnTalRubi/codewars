import pytest
from src.n_smallest import first_n_smallest

@pytest.mark.parametrize(
        "input1, input2, output",
        [
            (([1,2,3,4,5],3), [1,2,3]),
            (([5,4,3,2,1],3), [3,2,1]),
            (([1,2,3,1,2],3), [1,2,1]),
            (([1,2,3,-4,0],3), [1,-4,0]),
            (([1,2,3,4,5],0), []),
            (([1,2,3,4,5],5), [1,2,3,4,5]),
            (([1,2,3,4,2],4), [1,2,3,2]),
            (([2,1,2,3,4,2],2), [2,1]),
            (([2,1,2,3,4,2],3), [2,1,2]),
            (([2,1,2,3,4,2],4), [2,1,2,2]),
        ]
)

def test_n_smallest(input1, input2, output):
    assert first_n_smallest (input1, input2) == output


