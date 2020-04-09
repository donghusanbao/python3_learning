class Solution:
    def reverse(self, x: int) -> int:
        if 10 > x > -10:
            return x
        int_str = str(x)
        reverse_str = ''
        if x < 0:
            reverse_str = ''.join(list(reversed(int_str[1:])))
            reverse_str = '-' + reverse_str
        else:
            reverse_str = ''.join(list(reversed(int_str)))
        result = int(reverse_str)
        if (-2 ** 31) <= result <= (2 ** 31 -1):
            return result
        else:
            return 0

    def reverse_best(self, x: int) -> int:
        if 10 > x > -10:
            return x
        result = ''
        if x > 0:
            result = str(x)[::-1]
            result = int(result)
        else:
            result = str(x)[:0:-1]
            result = - int(result)
        if (-2**31) <= result <= (2**31 -1):
            return result
        else:
            return 0

    def reverse_better(self, x):
        y, res = abs(x), 0
        boundary = (1 << 31) - 1 if x > 0 else (1<<31)
        print(boundary)
        while y != 0:
            res = res * 10 + y % 10
            if res > boundary:
                return 0
            y //= 10
        return res if x > 0 else -res


if __name__ == '__main__':
    s = Solution()
    s.reverse_better(222)


