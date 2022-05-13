#父类A
class A(object):
    def __init__(self):
        self.num1 = 1
    def info_print1(self):
        print(self.num1)
#父类
class B(object):
    def __init__(self):
        self.num2 = 2
    def info_print2(self):
        print(self.num2)

#子类B 默认继承父类所有属性和方法
class C(A,B):
    pass
result = C()
result.info_print1()

