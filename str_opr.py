def reverse(input_string):
    raw = input_string.split(' ')
    copied = raw[-1::-1]
    new = ' '.join(copied)
    return new


def some_sort(elem):
    return elem[0] + elem[1]


class SortElement(object):
    def __init__(self, elem_id=''):
        self.id = elem_id

    def __lt__(self, other):
        if self.id < other.id:
            return True
        else:
            return False


if __name__ == '__main__':
    # test function reverse
    input_str = 'I like cooking'
    output = reverse(input_str)

    # test function some_sort
    tuple_list = [(1, 5), (2, 3)]
    tuple_list.sort(key=some_sort)
    print('After sorted, tuple_list is : ', tuple_list)

    # test class SortElement
    raw_list = [SortElement(5), SortElement(3)]
    raw_list.sort()
    for element in raw_list:
        print(element.id)

    # test sort with lambda
    raw_list = ['abc', 'kfgv', 'cc']
    raw_list.sort(key=lambda elem: len(elem))
    raw_list = ['abc', 'kfgv', 'ccc']  # abc and ccc have the same length
    raw_list.sort(key=lambda elem: (len(elem), list(map(lambda e: -ord(e), elem))))
    # sort by length and then by reverse dict
    print(raw_list)

