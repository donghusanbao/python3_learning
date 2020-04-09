class Solution:
    def longestPalindrome(self, s: str) -> str:
        repeat_num = 0
        map_rep = {}
        start = 0
        end = 0
        start_max = 0
        end_max = 0
        max_length = 0
        for i, v in enumerate(s):
            if v in map_rep:
                desired_repeat_num = i - map_rep[v] - 1
                if desired_repeat_num % 2 == 0:
                    desired_repeat_num += 1
                if desired_repeat_num == repeat_num:
                    repeat_num += 2
                    start = map_rep[v]
                    end = i
                    if repeat_num > max_length:
                        start_max = start
                        end_max = end
                        max_length = repeat_num
                else:
                    repeat_num = 0
                    start = 0
                    end = 0
            else:
                map_rep[v] = i
                repeat_num = 1
        return s[start_max: end_max + 1]


if __name__ == '__main__':
    s = Solution()
    result = s.longestPalindrome('bbb')
    print(result)