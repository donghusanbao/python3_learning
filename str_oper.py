def reverse(input_string):
    raw = input_string.split(' ')
    copied = raw[-1::-1]
    new = ' '.join(copied)
    return new


if __name__ == '__main__':
    input_str = 'I like cooking'
    output = reverse(input_str)
