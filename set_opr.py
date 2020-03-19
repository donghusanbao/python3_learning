# empty set
set_zero = set()

# different instantiations
set_one = {'a', 'b', 'c'}
set_one_compare = set({'a', 'b', 'c'})  # equals to {'a', 'b', 'c'}
set_two = set('def')  # equals to {'d', 'e', 'f'}
set_three = set([1, 2, 3, 3])  # equals to {1, 2, 3} remove repeated elements
set_four = set((1, 2))  # equals to {1, 2}
set_four_compare = set({(1,2)})  # equals to {(1, 2)}
set_five = set({'a': 1, 'b': 2})  # equals to {'a', 'b'} only extract keys

# operations
one = {1, 2, 3}
two = {2, 3, 4}

if 1 in one:
    print('1 in one')

print(one & two)  # equals to 2, 3
print(one | two)  # equals to 1, 2, 3, 4
print(one - two)  # equals to 1
print(two - one)  # equals to 4
print(one ^ two)  # equals to 1, 4 |-&

# transfer between set and other types
test = {1, 2, 3}
list_trans = list(test)
tuple_trans = tuple(test)
str_trans = str(test)
