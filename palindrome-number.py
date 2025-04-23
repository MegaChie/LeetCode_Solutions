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
        Returns a boolean indication if
        the number reads the same when reversed.
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_int = digit = 0
        copy = x

        while x > 0:
            digit = x % 10
            reversed_int = (reversed_int * 10) + digit
            x = x // 10

        if reversed_int == copy:
            return True

        return False


if __name__ == "__main__":
    case = 121
    case2 = -121
    case3 = 10
    case4 = 10101

    result = Solution()

    ret = result.isPalindrome(case4)
    print(ret)
