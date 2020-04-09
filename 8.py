import re
class Solution:
    def myAtoi(self, str_input: str) -> int:
        str_input = str_input.strip()
        if len(str_input) == 0:
            return 0
        if len(str_input) == 1:
            if str_input.isdigit():
                return int(str_input)
            else:
                return 0
        first_digit = -1
        last_digit = -1
        flag = 0
        if str_input[0] in ['+', '-'] or str_input[0].isdigit():
            flag = '+' if str_input[0] not in ['+', '-'] else str_input[0]
            first_digit = 1 if str_input[0] in ['+', '-'] else 0
            if not str_input[first_digit].isdigit():
                return 0
            for j in range(first_digit, len(str_input)):
                if str_input[j].isdigit():
                    continue
                else:
                    last_digit = j - 1
                    break
        else:
            return 0
        if first_digit == -1:
            return 0
        if last_digit == -1:
            last_digit = len(str_input) - 1
        result = int(str_input[first_digit: last_digit + 1])
        if flag == '-':
            result = - result
        boundary = (1<<31) - 1 if flag == '+' else (1<<31)
        if abs(result) > boundary:
            return boundary if result > 0 else -boundary
        return result

    def myAtoi_best(self, str_in: str) -> int:
        result = re.findall('^[\+\-]?\d+', str_in.lstrip())
        result = int(*result)
        return min(max(result, -(1<<31)), (1<<31) - 1)

    def test(self):
        list_one = []
        print(str(*list_one))


if __name__ == '__main__':
    s = Solution()
    #result = s.myAtoi_best("words and 987")
    #print(result)
    s.test()