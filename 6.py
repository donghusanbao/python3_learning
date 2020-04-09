class Solution:
    def convert(self, s: str, numRows: int) -> str:
        one_z = numRows * 2 - 2
        s_size = len(s)
        z_number = s_size // one_z
        remains = s_size % one_z
        return_str = [''] * len(s)
        if (len(s) <= numRows) or (numRows == 1):
            return s
        for i in range(z_number):
            return_str[i] = s[i * one_z]
        if remains >= 1:
            i += 1
            return_str[i] = s[i * one_z]
        sum_v = 0
        for j in range(1, numRows - 1):
            for k in range(z_number):
                return_str[i + 2 * k + 1 + sum_v] = s[one_z * k + j]
                return_str[i + 2 * k + 2 + sum_v] = s[one_z * k + 2 * (numRows - 1) - j]
            sum_v += 2 * z_number
            if remains >= j + 1:
                sum_v += 1
                return_str[i + sum_v] = s[one_z * z_number + j]
            if remains >= (2 * (numRows - 1) - j + 1):
                sum_v += 1
                return_str[i + sum_v] = s[one_z * z_number + 2 * (numRows - 1) - j]
        for z in range(z_number):
            return_str[i + sum_v + z + 1] = s[one_z * z + (numRows - 1)]
        if remains >= numRows:
            return_str[i + sum_v + z_number + 1] = s[one_z * z_number + numRows - 1]
        return ''.join(return_str)


if __name__ == '__main__':
    s = Solution2()
    # result = s.convert('LEETCODEISHIRING', 3)
    result = s.reverse(234)
    print(result)
