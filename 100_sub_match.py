import re


def sub_match(str_main, str_sub):
    j = 0
    k = 0
    max_index = len(str_main) - 1
    for i, value in enumerate(str_main):
        if value == str_sub[j]:
            if j == len(str_sub) - 1:
                k += 1
                break
            else:
                j += 1
                k += 1
        else:
            if str_sub[j] == '?':
                if j == (len(str_sub) - 1):
                    k += 1
                    break
                if (i < max_index) and (str_sub[j + 1] == str_main[i + 1]):
                    k += 2
                    j += 2
                    if j == (len(str_sub)):
                        break
                    i += 1
                elif (i < max_index - 1) and str_sub[j + 1] == str_main[i + 2]:
                    k += 3
                    j += 2
                    if j == (len(str_sub)):
                        break
                    i += 2
                elif (i < max_index - 2) and str_sub[j + 1] == str_main[i + 3]:
                    k += 4
                    j += 2
                    if j == (len(str_sub)):
                        break
                    i += 3
            else:
                j = 0
                k = 0
    return k


def re_test():
    ret = re.findall(r"(-?\d+\.\d*)|(-?\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
    result_one = [one for one, two in ret]
    result_two = [two for one, two in ret]
    print(result_one)
    print(result_two)
    ret = re.findall(r"(-?\d+)|(-?\d+\.\d*)", "1-2*(60+(-40.35/5)-(-4*3))")
    result_one = [one for one, two in ret]
    result_two = [two for one, two in ret]
    print(result_one)
    print(result_two)
    ret = re.findall(r"(-?\d+|-?\d+\.\d*)", "1-2*(60+(-40.35/5)-(-4*3))")
    print(ret)


if __name__ == '__main__':
    str_main = 'aabcddefg'
    str_sub = 'b?e'
    k = sub_match(str_main, str_sub)
    re_test()


