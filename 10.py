class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slices = p.split('*')
        print(slices)
        slices_l = len(slices)
        if slices_l == 1:

            # 忘记考虑s和p不等长的情况
            if len(s) != len(p):
                return False

            for i in range(len(s)):
                if s[i] != p[i]:
                    if p[i] != '.':
                        return False
            return True

        #忘记考虑p以*结尾，会多出来一个['']
        end_with = False
        if p[-1] == '*':
            slices = slices[:-1]
            # 忘记更新长度
            slices_l = len(slices)
            end_with = True

        last_index = 0
        s_repeat = ''
        s_match = False
        dot_match = False
        for t, slice_e in enumerate(slices):
            print(last_index)
            if s_match:
                if s[last_index] != slice_e[0]:
                    if len(slice_e) != 1:
                        return False
                    else:
                        continue
                else:
                    s_match = False
            if dot_match:
                print('dot match')
                not_dot = -1
                for zz in range(len(slice_e)):
                    if slice_e[zz] != '.':
                        not_dot = zz
                        break
                if not_dot == -1:
                    print('not dot is -1')
                    if t == (slices_l - 1) and (not end_with):
                        bound = last_index + len(slice_e) - 1
                        if bound > (len(s) - 1):
                            return False
                        return True
                    if t == (slices_l - 1) and end_with:
                        return True
                    if len(slice_e) == 1:
                        continue
                    else:
                        last_index = last_index + len(slice_e) - 1
                        continue
                for z in range(last_index, len(s)):
                    if s[z] == slice_e[not_dot]:
                        if z < (last_index + not_dot):
                            continue
                        last_index = z
                        dot_match = False
                        break
                if dot_match:
                    if len(slice_e) != 1:
                        return False
                    else:
                        continue
            for i in range(len(slice_e) - 1):
                if s[i + last_index] != slice_e[i]:
                    if slice_e[i] != '.':
                        return False
            last_index = len(slice_e) - 1 + last_index
            if last_index == len(s):
                if t == (slices_l - 1):
                    return True
                for tt in range(t + 1, slices_l):
                    if len(slices[tt]) > 1:
                        return False
                    if len(slices[tt]) == 1 and (not end_with):
                        return False
                return True

            if s[last_index] == slice_e[-1]:
                if t == (slices_l - 1) and not end_with:
                    break
                start_index = last_index
                for j in range(start_index + 1, len(s)):
                    if s[j] == slice_e[-1]:
                        last_index = j
                        continue
                    last_index += 1
                    break
            elif slice_e[-1] == '.':
                if t == (slices_l - 1):
                    if last_index == (len(s) - 1):
                        return True
                    else:
                        if end_with:
                            return True
                        return False
                dot_match = True
            else:
                s_match = True
        if last_index == (len(s) - 1):
            return True
        else:
            return False

    def match(self, s_in, p):
        p_list = []
        start = 0
        for i, v in enumerate(p):
            if v == '*':
                part = p[i - 1: i + 1]
                part_before = p[start: i - 1]
                if len(part_before) != 0:
                    p_list.append(part_before)
                p_list.append(part)
                start = i + 1
        print(p_list)
        s_index = 0
        dot_flag = False
        for r in p_list:
            if r.count('*') == 0:
                if r.count('.') == 0:
                    for j in range(s_index, len(s)):
                        if s[j] == r[0]:

                            return False
                if r.count('.') == len(r):
                    s_index += len(r)
                    continue
                for j in range(r):
                    if r[j] != '.'
            else:
                if r == '.*':
                    dot_flag = True
                else:
                    pass











if __name__ == '__main__':
    s = Solution()
    result = s.match('ab', '.*..c*')
