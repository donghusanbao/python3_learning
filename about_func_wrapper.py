from functools import wraps


class Wrapper(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        print('In wrapper')
        self._func(*args)


@Wrapper
def class_func(x, y):
    print('x = ', x, ' y = ', y)


def func_wrapper_logging(level):
    def func_wrapper_inner(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("%s is running" % func.__name__)
            elif level == "info":
                print("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return func_wrapper_inner


@func_wrapper_logging(level="warn")
def func(name):
    print("i am %s" % name)


def func_wrapper(f_be_wrapped):
    @wraps(f_be_wrapped)
    def new_func(name):
        print('print before f_be_wrapped')
        f_be_wrapped(name, ' in a func wrapper')
        print('print after f_be_wrapped')
    return new_func


@func_wrapper
def func_be_wrapped(name, pos):
    print(name, pos)


def func_as_return(name='sub_func1'):
    def sub_func1():
        print('This is sub func1')

    def sub_func2():
        print('This is sub func2')

    # pay attention to the return value, no ()
    if name == 'sub_func1':
        return sub_func1
    else:
        return sub_func2


def param_func():
    print('I am func as a param')


def func_as_param(func_name):
    print('Doing work before executing param_func')
    func_name()


def main():
    # test1: func can be used as a 'return'
    func1 = func_as_return()
    func2 = func_as_return('sub_func2')
    func1()
    func2()

    # test2: func can be used as a 'param', param_func can not add ()
    func_as_param(param_func)

    # test3: wrapper function
    func_be_wrapped('dongdong')

    # tes4: wrapper function with param (multi layer)
    func('liu')

    # test5: class wrapper
    class_func(2, 3)


if __name__ == '__main__':
    main()
