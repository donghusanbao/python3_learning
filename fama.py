class Solution(object):
    def total_compose(self, weight, count):
        cap = sum([weight[i] * count[i] for i in range(len(weight))])
        result_list = [True] + [False] * cap
        for i in range(len(weight)):
            for cap_index in reversed(range(cap + 1)):
                for c in range(0, count[i] + 1):
                    if c * weight[i] <= cap_index:
                        if result_list[cap_index - c * weight[i]]:
                            result_list[cap_index] = True
                            break
        print(result_list)
        return result_list.count(True) - 1


if __name__ == '__main__':
    weight = [1, 2, 3, 5, 10, 20]
    count = [0, 2, 1, 0, 0, 0]
    s = Solution()
    result = s.total_compose(weight, count)
    print(result)