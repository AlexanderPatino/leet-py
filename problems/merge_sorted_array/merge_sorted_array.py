import copy
import pytest
from typing import List


class TestSolution:
    example1 = ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    example2 = ([1], 1, [], 0, [1])
    example3 = ([0], 0, [1], 1, [1])
    examples = [example1, example2, example3]

    @pytest.mark.parametrize(
        "nums1, m, nums2, n, expected",
        copy.deepcopy(examples),
        ids=["example1", "example2", "example3"],
    )
    def test_merge1(
        self, nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]
    ) -> None:
        """
        Time: O((m+n)log(m+n))
        Space: O(1)
        """
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()
        assert nums1 == expected

    @pytest.mark.parametrize(
        "nums1, m, nums2, n, expected",
        copy.deepcopy(examples),
        ids=["example1", "example2", "example3"],
    )
    def test_merge2(
        self, nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]
    ) -> None:
        """
        Time: O(m+n)
        Space: O(1)
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        assert nums1 == expected
