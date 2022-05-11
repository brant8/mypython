fn2 = lambda: 100
print(fn2)
print(fn2())

fn1 = lambda *args: args
print(fn1({'name':'tim'}))

fn2 = lambda **kwargs: kwargs
print(fn2(name='python',age=20))

fn3 = lambda *kwargs: kwargs
print(fn3([10,20,30]))

fn41 = lambda a,b: a if a> b else b #与三目运算合用
print(fn41(100,50))

students = [
    {'name':'Tom','age':20},
    {'name':'Tim','age':21},
    {'name':'Sam','age':23}
]
students.sort(key=lambda x:x['age'], reverse=True)
print(students)

def sum1(a,b,f):
    return f(a)+f(b)

print(sum1(3,-5,abs))

list12 = [1,2,3,4,5]
def func(x):
    return x**2
result = map(func,list12)
print(result)
print(list(result))

import functools
def func(a,b):
    return a+b
result = functools.reduce(func,list12)
print(result)

def func(x):
    return x % 2 == 0
result = filter(func,list12)
print(result)
print(list(result))
