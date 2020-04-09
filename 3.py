class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        max = 0
        if len(s) <= 1:
            return 1
        for i in range(1, len(s)):
            for k in range(j, i):
                if s[k] == s[i]:
                    v = i - k
                    if v > max:
                        max = v
                        print('max is ', max, ' start from ', k, ' end at ', i)
                    j = k + 1
                    break
                elif k == i - 1:
                    v = i - j + 1
                    if v > max:
                        max = v
                        print('max is ', max, ' start from ', j, ' end at ', i)
        return max

    def lengthOfLongestSubstring_best(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLongestSubstring('')
    print(result)