class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 0

    def add(self):
        self.c = self.a + self.b

aa = A()
bb = getattr(aa, 'add')
bb()
print(aa.c)

