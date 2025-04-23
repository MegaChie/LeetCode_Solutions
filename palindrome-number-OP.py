#!/usr/bin/python3
"""
Solution to problem found at:
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    """
    A class that used to solve the problem.
    """
    def isPalindrome(self, x: int) -> bool:
        """
        Returns True if the number reads the same backward as forward.
        Note: This avoids overflow but is slower.
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    case = 121
    case2 = -121
    case3 = 10
    case4 = 10101

    result = Solution()

    ret = result.isPalindrome(case)
    print(ret)
    
    ret = result.isPalindrome(case2)
    print(ret)
    
    ret = result.isPalindrome(case3)
    print(ret)

    ret = result.isPalindrome(case4)
    print(ret)
