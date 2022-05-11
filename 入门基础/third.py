nameList=['Tom','Tim','Sam']

print(nameList.pop(1))

dict2 = {'name':'Tom', 'age':20, 'gender':'男'}
print(dict2.get('name'))
print(dict2.get('id',110))
print(dict2.get('id'))

print(dict2.keys())

print(dict2.values())

print(dict2.items())

print(dict2)

s1={10,20,30,10}
print(s1)

# s1.remove([10,20])
s1.remove(10)
print(s1)

list = ['a','b','c','d','e']
for i in enumerate(list):
    print(i)

list3=[]
i=0
while i <10:
    list.append(i)
    i+=1
print(list3)

for i in range(10):
    print(i)

list1 = ['name','age','gender']
list2 = ['Tom',20,'man','nv']
dict1 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict1)

print('**********')

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
count2= {}
for key,value in counts.items():
    if value >= 200:
        count2[key]=value
print(f'count2值是{count2}')

print('**********')


count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)

def add_num(a,b):
    result = a+b
    print(result)
# print(result)
print(add_num(1,2))

print(help(len))


def add2(a,b):
    """
    sum func
    :param a:
    :param b:
    :return:
    """
    return a+b

def testBB():
    return print("B")
def testAA():
    testBB()
    return print("A")
testAA()


a = 100
print(a)
def runA():
    print(a)
runA()
def runB():
    a = 200
    print(a)
runB()
print(a)
def runC():
    global a
    a = 300
    print(a)
runC()
print(a)


def user(*args):
    print(args)

user()

def user2(**kwargs):
    print(kwargs)
user2(name='Tom',age=18,id=10)


dict1 = {'name':'Tom', 'age':18}
a,b = dict1
print(dict1[a])
print(b)