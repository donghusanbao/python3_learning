class Student(object):
    name = 1

    def count(self):
        self.name += 1
        print(self.name)


class Classname:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')


'''
类可以调用静态方法、类方法，不能调用普通方法
对象三个都可以调用
'''
Classname.fun()
Classname.a()
C = Classname()
C.fun()
C.a()
C.b()

student = Student()
student.count()
print(student.name)
print(Student.name)
