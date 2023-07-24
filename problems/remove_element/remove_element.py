import copy
import pytest
from typing import List


class TestSolution:
    example1 = ([3, 2, 2, 3], 3, 2)
    example2 = ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
    examples = [example1, example2]

    @pytest.mark.parametrize(
        "nums, val, expected",
        copy.deepcopy(examples),
        ids=["example1", "example2"],
    )
    def test_remove_element(self, nums: List[int], val: int, expected: int) -> int:
        """
        Time:
        Space:
        """
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        assert k == expected
