#!/usr/bin/python3
"""
Solution to problem found at:
https://leetcode.com/problems/two-sum/
"""


class Solution:
    """
    A class that used to solve the problem.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Returns indices of the two numbers such that they add up to target.
        """
        index_dict = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in index_dict:
                return [index_dict[needed], index]
            index_dict[num] = index


if __name__ == "__main__":
    result = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    case = result.twoSum(nums, target)
    print(case)

    nums2 = [3, 2, 4]
    target2 = 6
    case2 = result.twoSum(nums2, target2)
    print(case2)

    nums3 = [3, 3]
    target3 = 6
    case3 = result.twoSum(nums3, target3)
    print(case3)
