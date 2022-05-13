# f = open('../pics/test.txt','w')
# f.write('aaa')
# f.close()

f2 = open('../pics/test.txt')
content = f2.readlines()
print(content) #['aaa\n', 'bbb\n', 'ccc\n', 'ddd']


f3 = open('../pics/test.txt','r+')
# 1.改变读取数据开始位置
# f3.seek(2,0)
# 2.把文件指针放结尾（无法读取数据）
f3.seek(0,2)
con = f3.read()
print(con)
f3.close()

# 1.获取要复制的文件
old_name = input("输入要备份的名字： ")
print(old_name)
print(type(old_name))
# 2.提取后缀 test.txt 找到名字中的点，名字和后缀分离
index = old_name.rfind('.')
print(index)
# 2.2 有效文件才备份
if index> 0:
    postfix = old_name[index:] #后面省略
# 3.切片分离
print(old_name[0:index])
print(old_name[index:])
new_name = old_name[0:index] + '[备份]' + old_name[index:] #postfix
# 4.通过二进制打开文件和二进制写入
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')
# 5.若并不确定文件大小，循环写入
while True:
    con = old_f.read(1024)
    if len(con)==0:
        break
    new_f.write(con)
# 6.关闭文件
old_f.close()
new_f.close()

import os
