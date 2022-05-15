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

class Dog(object):
    __tooth = 10		#__xx为私有属性
    @classmethod		#定义类方法
    def get_tooth(cls): #
        return cls.__tooth

wangcai = Dog()
wangcai.get_tooth()