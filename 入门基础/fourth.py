a=1
b=a
print(b)
print(id(a))
print(id(b))
#...
a=2
print(b)
# ...
aa = [10,20]
bb=aa
print(id(aa))
print(id(bb))
#..
aa.append(30)
print(id(aa))
print(id(bb))
print(bb)
#...
def test1(a):
    print(a)
    print(id(a))
    a+=a
    print(id(a))
b=100
test1(b)
c=[100,200]
test1(c)