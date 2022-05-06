num=10
if num>5:
    print("条件成立执行代码1")
    print("条件成立执行代码2")
    if num<20:
        print("条件成立执行代码1")


# print(type(float(2)))

import random

print(random.randint(1,99))

i=0
while i<3:
    print("条件成立执行代码1")
    i+=1


i=1
while i<=9:
    j=1
    while j<=i:
        print(f'{i}*{j} = {i*j}', end="\t")
        j+=1
    print("")
    i+=1


a="hello" \
  " world"

print("helloworld".find('wode'))
print("helloworld".index('wo'))
print("helloworld".split('wo'))

print('...'.join(['a','b','c']))