class Solution(object):
    def zero_one_packet_0(self, weight, value, cap):
        packet_map = [[0 for j in range(cap + 1)] for i in range(len(weight))]
        for j in range(cap + 1):
            if weight[0] <= j:
                packet_map[0][j] = value[0]
            else:
                packet_map[0][j] = 0
        for i in range(1, len(weight)):
            for j in range(cap + 1):
                if weight[i] <= j:
                    packet_map[i][j] = max(packet_map[i - 1][j], packet_map[i - 1][j - weight[i]] + value[i])
                else:
                    packet_map[i][j] = packet_map[i - 1][j]
        weight_index = len(weight) - 1
        cap_index = cap
        output_list = []
        for i in reversed(range(weight_index + 1)):
            if i == 0:
                if packet_map[i][cap_index] != 0:
                    output_list.append(i)
                break
            if packet_map[i][cap_index] == packet_map[i - 1][cap_index]:
                continue
            else:
                output_list.append(i)
                cap_index = cap_index - weight[i]
        print(output_list)
        return packet_map[len(weight) - 1][cap]

    def zero_one_packet_1(self, weight, value, cap):
        first_value_list = [0] * (cap + 1)
        for i in range(len(weight)):
            second_value_list = []
            for j in range(cap + 1):
                if weight[i] <= j:
                    second_value_list.append(max(first_value_list[j], first_value_list[j - weight[i]] + value[i]))
                else:
                    second_value_list.append(first_value_list[j])
            first_value_list = second_value_list
        return first_value_list[-1]

    def zero_one_packet_2(self, weight, value, cap):
        first_value_list = [0] * (cap + 1)
        second_value_list = [0] * (cap + 1)
        for i in range(len(weight)):
            for j in range(cap + 1):
                if weight[i] <= j:
                    second_value_list[j] = max(first_value_list[j], first_value_list[j - weight[i]] + value[i])
                else:
                    second_value_list[j] = first_value_list[j]
            first_value_list, second_value_list = second_value_list, first_value_list
        return first_value_list[-1]

    def zero_one_packet_3(self, weight, value, cap):
        first_value_list = [0] * (cap + 1)
        for i in range(len(weight)):
            for j in reversed(range(cap + 1)):
                if weight[i] <= j:
                    first_value_list[j] = max(first_value_list[j], first_value_list[j - weight[i]] + value[i])
                else:
                    first_value_list[j] = first_value_list[j]
        return first_value_list[-1]

    def complete_packet_0(self, weight, value, cap):
        packet_map = [[0 for j in range(cap + 1)] for i in range(len(weight))]
        for j in range(cap + 1):
            if weight[0] <= j:
                packet_map[0][j] = packet_map[0][j - weight[0]] + value[0]
            else:
                packet_map[0][j] = 0
        for i in range(1, len(weight)):
            for j in range(cap + 1):
                if weight[i] <= j:
                    packet_map[i][j] = max(packet_map[i - 1][j], packet_map[i][j - weight[i]] + value[i])
                else:
                    packet_map[i][j] = packet_map[i - 1][j]
        print(packet_map)
        cap_index = cap
        weight_index = len(weight) - 1
        output_list = []
        while cap_index > 0 and weight_index >= 0:
            if weight_index == 0:
                number = cap_index // weight[0]
                output_list.extend([0] * number)
                break
            if packet_map[weight_index][cap_index] == packet_map[weight_index - 1][cap_index]:
                weight_index -= 1
            else:
                cap_index -= weight[weight_index]
                output_list.append(weight_index)
        print(output_list)
        return packet_map[len(weight) - 1][cap]

    def complete_packet_1(self, weight, value, cap):
        value_list = [0] * (cap + 1)
        for i in range(len(weight)):
            for j in range(cap + 1):
                if weight[i] <= j:
                    value_list[j] = max(value_list[j], value_list[j - weight[i]] + value[i])
        return value_list[-1]

    def multi_packet_0(selfs, weight, value, count, cap):
        packet_map = [[0 for j in range(cap + 1)] for i in range(len(weight))]
        g_map = [[1 for j in range(cap + 1)] for i in range(len(weight))]
        for j in range(cap + 1):
            if weight[0] <= j:
                for c in range(1, count[0] + 1):
                    if (j - c * weight[0]) >= 0:
                        packet_map[0][j] = c * value[0]
        print(packet_map)
        for i in range(1, len(weight)):
            for j in range(cap + 1):
                packet_map[i][j] = packet_map[i - 1][j]
                g_map[i][j] = g_map[i - 1][j]
                if weight[i] <= j:
                    for c in range(1, count[i] + 1):
                        if (j - c * weight[i]) >= 0:
                            new_v = packet_map[i - 1][j - c * weight[i]] + c * value[i]
                            if new_v == packet_map[i][j]:
                                g_map[i][j] += g_map[i - 1][j - c * weight[i]]
                            elif new_v > packet_map[i][j]:
                                packet_map[i][j] = new_v
                                g_map[i][j] = g_map[i - 1][j - c * weight[i]]
        print(packet_map)
        print(g_map)
        output_list = []
        cap_index = cap
        weight_index = len(weight) - 1
        while (cap_index > 0) and (weight_index >= 0):
            if weight_index == 0:
                number = cap_index // weight[0]
                output_list.extend([0] * number)
                break
            if packet_map[weight_index][cap_index] == packet_map[weight_index - 1][cap_index]:
                weight_index -= 1
            else:
                for c in range(1, count[weight_index] + 1):
                    c_i = packet_map[weight_index - 1][cap_index - c * weight[weight_index]] + c * value[weight_index]
                    if c_i == packet_map[weight_index][cap_index]:
                        output_list.extend([weight_index] * c)
                        cap_index = cap_index - c * weight[weight_index]
                        weight_index -= 1
                        break
        print(output_list)
        return packet_map[len(weight) - 1][cap]

    def multi_packet_1(self, weight, value, count, cap):
        first_value = [0] * (cap + 1)
        g_value = [1] * (cap + 1)
        for i in range(len(weight)):
            for j in reversed(range(cap + 1)):
                if weight[i] <= j:
                    for c in range(1, count[i] + 1):
                        if (j - c * weight[i]) >= 0:
                            new_v = first_value[j - c * weight[i]] + c * value[i]
                            if new_v == first_value[j]:
                                g_value[j] += g_value[j - c * weight[i]]
                            elif new_v > first_value[j]:
                                first_value[j] = new_v
                                g_value[j] = g_value[j - c * weight[i]]
        print(g_value)
        return first_value[-1]


if __name__ == '__main__':
    s = Solution()
    weight = [3, 4]
    value = [4, 8]
    count = [2, 1]
    cap = 12
    result = s.multi_packet_0(weight, value, count, cap)
    print(result)
