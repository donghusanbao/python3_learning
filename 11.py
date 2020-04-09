class Solution:
    def maxArea(self, height):
        max_v = 0
        n = len(height)
        index_list = range(len(height))
        new_list = sorted(index_list, key=lambda k: height[k])
        for i in range(n - 1):
            v = height[new_list[i]]
            a1 = abs(max(new_list[i + 1:]) - new_list[i])
            a2 = abs(min(new_list[i + 1:]) - new_list[i])
            v = v * max(a1, a2)
            if max_v < v:
                max_v = v
        return max_v


if __name__ == '__main__':
    s = Solution()
    result = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(result)