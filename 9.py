class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_size = len(x_str)
        if x_size == 1:
            return True
        mid = (x_size - 1) // 2
        mid_index = mid if len(x_str) % 2 == 1 else mid + 1
        for i in range(mid_index):
            if x_str[i] != x_str[x_size - 1 - i]:
                return False
        return True

    def isPalindrome_better(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if y == str(x):
                return True
            else:
                return False

    