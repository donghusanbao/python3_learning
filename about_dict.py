if __name__ == '__main__':
    # copy
    list_one = [1, 2, 3]
    dict1 = {'a': 1, 'b': list_one}
    dict1.clear()
    print(list_one)  # list_one still exist
    print(dict1)  # dict1 is {}

    # reverse dict
    dict_one = {'a': 1, 'b': 2}
    dict_two = {y: x for x, y in dict_one.items()}
    print(dict_two)

    # get key from value
    dict_get = {'1': 's', '2': 'b'}
    key_get = list(dict_get.keys())[list(dict_get.values()).index('s')]
    print('key get is ', key_get)
