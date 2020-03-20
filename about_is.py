import math
# the id of the same number is the same
a = 1000
b = 1000
if a is b:
    print('int: a is b')  # result is true

a = 1000.0
b = 1000.0
if a is b:
    print('float: a is b')  # result is true

a = 1000.0 + 4j
b = 1000.0 + 4j
if a is b:
    print('complex: a is b')  # result is true

a = True
b = True
if a is b:
    print('bool: a is b')  # result is true

# list (dict is the same)
a = 1000
b = 1000
a_list = [a, 2, 3]
b_list = [b, 2, 3]
if a_list is b_list:
    print("list: a_list is b_list")  # result is false
if a_list[0] is b_list[0]:
    print('list: a is b')

a_list = [1000, 2, 3]
b_list = [1000, 3, 4]
if a_list is b_list:
    print("list: a_list is b_list (no variable)")  # result is false
if a_list[0] is b_list[0]:
    print('list: a is b (not variable a and b)')

# tuple
a = 1000
b = 1000
a_tuple = (a, 10, 100)
b_tuple = (b, 10, 100)
if a_tuple is b_tuple:
    print("tuple: a_tuple is b_tuple ")  # result is false
if a_tuple[0] is b_tuple[0]:
    print('tuple: a is b')
a_tuple = (1000, 10, 100)
b_tuple = (1000, 10, 100)
if a_tuple is b_tuple:
    print("tuple: a_tuple is b_tuple (no variable)")  # result is false
if a_tuple[0] is b_tuple[0]:
    print('tuple: a is b (no variable)')

