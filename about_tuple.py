if __name__ == '__main__':
    a = [1, 2, 3]
    tuple_one = (a, 2)
    print('tuple_one is ', tuple_one)
    a[0] = 2
    print('change element of list, tuple_one is ', tuple_one)
    a = 'sdd'
    print('change whole list, tuple_one is ', tuple_one)
