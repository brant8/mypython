其他兴趣：[【黑客技术】手把手教你如何攻击一个网站](https://ykbkw.top/post/86.html)

# Python学习

1. Python解释器作用：运行文件
   1. 解释器种类：CPython - C语言开发，广泛应用； IPython - 基于CPython，以及其他解释器。
   2. PyCharm中可以在Settings的ProjectXXX更改解释器版本。
   3. 单行注释使用井号"#"。多行注释使用`""" 注释 """`或者`''' 注释 ''`

2. Python中的输出函数：`print()`, 如print(520)。
   1. 可输出内容：数字，字符串，含有运算符的表达式
   2. 将内容输出目的地：显示器，文件
   3. 可换行，可不换行 
   4. | 格式符号  | 转换  |  例子   '%'作为连接符|
      |---|---|---|
      | <Strong>%s</Strong> | 字符串  |  print('今年%d岁' % 8) |
      | <Strong>%d</Strong> |  有符号的十进制整数(正负符号)，%06d表示正数显示位数，不足以0不全，超出当前位数原样输出 | print('我叫%s' % 'tom')，  print('我的学号是%03d' % stu_id) |
      | <Strong>%f</Strong>  | 浮点数(默认6个小数点，保留小数点多少位'%.xf')  |  print('我的体重是%.2f 斤' % weight) |
      |  %c | 字符  |   |
      |  %u |  无符号十进制整数 |  |
      |  %o | 八进制整数  |   |   |   |
      |  %x |  十六进制整数 小写ox |   |  
      |  %X | 十六进制整数 大写OX  |   |  
      |  %e | 科学计数法 小写e  |   |   
      |  %E | 科学计数法 大写E  |   |  
      |  %g |  %f和%e的简写 |   |   
      |  %G |  %f和%E的简写 |   |  
      |   |   | print('我的名字是%s学号是%03d' % (name,stu_id))  | 
   5. 字符串%s(也可以当作%d和%f)：`print('我的名字是%s,今年%s岁了' % (name,age))`
   6. 语法`f'{表达式}'`：如 `print(f'我的名字是{name},今年{age}岁了')`。注意：f格式化字符串是Python3.6版本以上才有。

3. 变量：就是一个存储数据的时候当前数据所在内存地址的名字。
   1. 不能数字开头
   2. 严格区分大小写
   3. 不能使用内置关键字

4. 数据类型 - 检测数据类型 `type(数据)`
   1. 数值：int、float
   2. 布尔型：True、False（在条件if语句时使用True/False）
   3. `str`（字符串）
   4. `list`（列表）:`c = [10, 20, 30]`
   5. `tuple`（元组）:`d = (10,20,30)`
   6. `set`（集合）:`e = {10,20,30}`
   7. `dict`（字典,键值对）：`f = { 'name':'TOM', 'age':18}`

5. 转义字符： `\n`换行、`\t`制表符，tab键(4个空格)。 
   1. `print('hello',end="\n")`，默认结尾是`end="\n"`作为结束符号
   2. 自定义结束符号`print('hello',end="..")`

6. 输入。`input("提示信息")`
   1. 当程序执行到input，等待用户输入，输入完成之后才继续向下执行。
   2. input会把接收到的任意哦那个胡输入的数据都当作字符串`str`处理。

7. 数据类型转换
   1. |  函数 |  说明 |   | 
      |---|---|---|
      | `int(x[,base])`  |  将x转换为一个正数 | 如： int(num) | 
      | `float(x)`  | 将x转换为一个浮点数(默认一个小数点)  |  float('123') | 
      |  `complex(real [,imag])` | 创建一个复数，real为实部，imag为虚部  |   | 
      |  `str(x)` |  将对象x转换为字符串 |   | 
      | `repr(x)`  | 将对象x转换为表达式字符串  |   | 
      | `eval(str)`  |  用来计算在字符串中的有效Python表达式，并返回一个对象 |  str1='1.1' ， str2=[1,2] ， eval(str1)转换成对应的原本类型浮点数 | 
      | `tuple(s)`  | 将序列s转换为一个元组(小/圆括号)  | list=[1,2] tuple(list)  | 
      |  `list(s)` | 将序列s转换为一个列表(中/方括号)  |   | 
      | `chr(x)`  | 将一个正数转换为一个Unicode字符  |   | 
      |  `ord(x)` |  将一个字符转换为它的ASCII整数值 |   | 
      |  `hex(x)` |  将一个正数转换为一个十六进制字符串 |   | 
      |  `ord(x)` | 将一个正数转换为一个八进制字符串  |   | 
      |  `bin(x)` |  将一个正数转换为一个二进制字符串 |   | 

8. 运算符
   1. 算术运算符：
      1. 加减乘除，
      2. 整除 `//` 比如 `9//4 = 2` `9//2 = 4`
      3. 取余 `%` 比如 `9%4 = 1`
      4. 指数 `**` 比如 `2**4 = 16`即 `2*2*2*2`
   2. 赋值运算符
      1. 多变量赋值 `num1,float1,str1 = 10, 0.5, 'abc'`
   3. 复合赋值运算符
      1. |  运算符 |  说明 | 实例  | 
         |---|---|---|
         | += | 加法赋值运算 | c+= 等价于 c=c+a|
         | -= | 减法赋值 | c-=a 等价于c=c-a |
         | *= | 乘法赋值 | c*=a 等价于c=c*a |
         | /= | 除法赋值 | c/=a 等价于c=c/a|
         | //= | 整除赋值 |c//=a等价于 c=c//a |
         | %= | 取余 | c&=a 等价于c=c%a|
         | **= | 幂赋值 | c**=a 等价于c=c**a |
      2. 例子： c=10  c*=1+2 -> c=30 -> c= c * (1+2)   
   4. 比较运算符: ==、 !=、 >、 < 、>= 、 <=、
   5. 逻辑运算符：and | or | not
      1. 数组之间的逻辑运算：
         1. `and`只要有一个数字为0，则结果为0，否则结果为最后一个非0数字。
         2. `or`只有所有值为0结果才为0，否则结果为第一个非0数字。

9. 条件语句if 语法如下（4个空格的tab）
   ```python
   if True:
       print("条件成立执行代码1")
       print("条件成立执行代码2")
   else:
       print("条件不成立执行代码3")
   
   if "条件1":
       print("条件成立执行代码1")
   elif "条件2":
       print("条件成立执行代码2")
   else:
       print("条件不成立执行代码3")
   
   # 化简
   if (age>=18) and (age<=60):
   # 可以化简为：
   if 18 <= age <= 60:
   
   #嵌套
   if "条件1":
       print("条件成立执行代码1") 
       if "条件2":
           print("条件成立执行代码2")  
   ```

10. random随机
    1. 使用时需要使用`import 模块名`如 `import random`
    2. 使用random模块中的随机整数功能
       1. `random.randint(开始，结束)`：包含开始和结束

11. 三目运算符：简化if - else用的
    1. `条件成立执行的表达式 if 条件 else 条件不成立执行的表达式`

12. while循环 
    1. break： 终止此循环
    2. continue： 退出当前一次循环，继续执行下一次循环。
    3. while循环嵌套
    ```python
    while condition:
        print("条件成立执行代码1")
    # 如
    i=0 #若有循环计数器，必须要有初始值。一般i取0
    while i<3:
        print("条件成立执行代码1")
        i+=1
    #while嵌套
    while condition1:
        while condition2:
            print("条件成立执行代码2")
        print("条件成立执行代码1")
    #例子， 九九乘法表
    i=1
    while i<=9:
        j=1
        while j<=i:
            print(f'{i}*{j} = {i*j}', end="\t")
            j+=1
        print("")
        i+=1
    ```

13. for循环
    ```python
     for 临时变量 in 序列:
         print("条件成立执行代码1")
     #序列可以是字符串，可以是元组等
    ```

14. 循环与else配合使用：表示当循环<strong>正常结束</strong>之后要执行的代码,`break`非正常结束，`continue`正常结束。
    ```python
    #while与else
    i=1
    while i<=5:
        print("原谅我呀！")
        i+=1
        #break		 # 若while True时，使用break才会退出循环
        			# break用于提前结束循环
    else:
        print("原谅我了哈") #执行完while后才执行else
    
    #for与else
    str1="hello world"
    for i in str1:
        print(i)
        # break		#若此行添加一行break/return，则不会执行下面的else，结束该循环
    else:
        print("正常结束else")
    ```

15. 字符串：单引号、双引号、三引号`'''Tom'''`或`"""Tom"""`
    1. 三引号可以直接换行，并且输出效果与三引号换行效果一致
    2. 单引号换行(回车)后会自动添加反斜杠`\`
    3. 单引号中有单个单引号，可以使用转义符如：`'I\'m Tom'`
    4. 格式化输出
       ```python
        name='tom'
        print('我的名字%s' % name)
        print(f'我的名字{name}')
       ```
    5. 下标：字符数据从0开始按顺序分配一个编号（索引值），如`str1[0]`
    6. 切片：指对操作的对象截取其中的一部分操作。字符串、列表、元组都支持切片操作
       1. 不包含结束位置下标对应的数据，正负整数均可。
       2. 步长是选取<strong>间隔</strong>，正负整数均可，默认步长为1.
       ```python
       #语法： 序列[开始位置下标：结束位置下标：步长]  
       
       name = "012345678"
       print(name[2:5:1]) #234
       print(name[2:5]) #234
       print(name[:5]) #01234, 不写结束，默认从0开始
       print(name[2:]) #2345678, 不写结束，表示选取到最后
       print(name[:]) #012345678, 不写开始和结束，表示从头选取到最后
       #负数从右向左，如-1为8，-2为7
       print(name[::-1]) #876543210, 开始结束不写，且为-1表示全选且倒叙
       print(name[-4:-1]) #fedcba, 开始结束不写，且为-1表示全选且倒叙
       print(name[-4:-1:1]) #567
       print(name[-4:-1:1]) #空值不能选取，选取方向与步长方向相反
       print(name[-1:-4:1]) #876
       ```
    7. 查找`find()`：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则返回-1。
       1. `rfind()`查找方向从右侧开始。下标0还是从左开始数。
       2. 语法：`字符串序列.find(子串，开始位置下标，结束位置下标)`，开始和结束位置可以省略，表示在整个字符串序列中查找
       3. 下标从0开始，如`print("helloworld".find('wo'))`返回5.
       4. 不存在，如`print("helloworld".find('wode'))`返回-1.
    8. 查找`index()`：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则报异常。
       1. `rindex()`查找方向从右侧开始。
       2. 语法：`字符串序列.find(子串，开始位置下标，结束位置下标)`
    9. 次数`count()`:返回某个子串在字符串出现的次数
    10. 修改字符串`replace()`:返回新的字符串
        1. `字符串序列.replace(旧子串，新子串，替换次数)`，可以省略替换次数，则表示全部替换
        2. replace函数有返回值即新数据，返回值式修改后的字符串，原字符串无变化。
        3. **说明字符串式不可变数据类型**
    11. 分割字符串`split()`：返回一个列表
        1. `字符串序列.split(分割字符,num)` 表示分割字符出现的次数，即将来返回数据个数为num+1个
        2. 如 `print("helloworld".split('wo'))` 结果`['hello', 'rld']`
        3. 丢失分割字符
    12. `join()`：合并列表里面的字符串数据为一个大字符串
        1. `字符或子串.join(多字符串组成的序列)`
        2. 如`print('...'.join(['a','b','c']))`结果`a...b...c`
    13. 其他字符串方法，如`str.capitalize()`转换第一个字母为大写，`str.title()`每个字母都大写，`str.upper()`以及`str.lower()`
    14. `lstrip()`删除字符串左侧空白字符，`rstrip()`删除字符串右侧空白字符，`strip`删除两侧的空白字符
    15. `ljust()`返回一个源字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串。
        1. `字符串序列.ljust(长度，填充字符)`
        2. `rjust()`以及`center()`
    16. 判断是否以指定子串开头或结尾，如果设置开始和结束下表，则在指定范围内检查
        1. `startswith()`:'字符串序列.startswith(子串，开始位置下标，结束位置下标)'
        2. `endswith()`: 
    17. `isalpha()`：如果字符串至少有一个字符并且所有字符都是字母，则返回True
    18. `isdigit()`：如果字符串只包含数字则返回True。
    19. `isalnum()`：如果字符串至少有一个字符并且所有字符都是字母或数字或组合，则返回True
    20. `isspace()`：如果字符串中只包含空白则返回True

16. 列表 `[数据1,数据2,数据3,..]`：可以存不同数据类型，但一般不推荐
    1. 查找列表：
       1. 下方式标：从0开始 如`list[0]`,`list[1]`
       2. 函数方式：
          1. `index()`：返回指定数据所在下标，`列表序列.index(数据，开始位置下标，结束位置下标)`
          2. `count()`：同级指定数据在当前列表中出现的次数`列表数据.count('子串')`
          3. `len(序列)`：访问列表长度，即列表中数据的个数，公共方法，元组列表等都可使用。

    2. 判断是否存在
       1. `in`：判断指定数据在某个列表序列，如果在返回True
          1. 如 `print('Lily' in ['Tom','Lily','Rose'])`
       2. `not in`：判断指定数据不在某个列表序列，如果不在返回True

    3. 追加，列表结尾追加数据。`列表序列.append(数据)`  

    4. `extend()` 列表结尾追加数据，如果数据是一个列表，则这个序列的数据逐一添加到列表。  
       ```python
        name_list=['Tom','Lily','Rose']
        name_list.extend('Jack')
        print(name_list)
       # 结果：['Tom', 'Lily', 'Rose', 'J', 'a', 'c', 'k']
       name_list2=['Tom','Lily','Rose']
       name_list2.extend(['zs','ls'])
       print(name_list2)
       # ['Tom', 'Lily', 'Rose', 'zs', 'ls'] 
       ```

    5. `insert()`：指定位置新增数据

       1. `列表序列.insert(位置下标，数据)`

    6. 删除指定数据: `del(目标)`或`del 目标`

       1. 可以删除指定元素`del(list[2])`

    7. `pop()`删除指定列表下标的数据，如`['Tom','Sam','Jack'].pop(1)`

       1. 如果不指定下标，默认删除最后一个数据，
       2. 无论按照下标还是删除最后1个，pop函数都会返回这个被删除的数据。

    8. `remove()`：删除数据，如`['Tom','Sam','Jack'].remove('Sam')`

    9. `clear()`：清空列表，`列表.clear()`

    10. 修改列表的操作，修改指定下标：`nameList[1]='aaa'`

    11. `reverse()`：逆序，`列表.reverse()`

    12. `sort()`排序：升序和降序，默认升序排序

        1. `列表序列.sort(key=None, reverse=False)`
        2. `reverse=True`降序，`reverse=False`升序（默认）

    13. `copy()`：复制，如`列表.copy()

    14. 列表的循环遍历：while

        ```pyth
        nameList=['Tom','Lily','Rose']
        i=0
        while i<len(nameList):
        	print(nameList[i])
        	i+=1
        ```

    15. for循环

        ```py
        nameList=['Tom','Lily','Rose']
        for i in nameList:
        	print(i)
        ```

    16. 列表嵌套：`[ [列表1],[列表2],[列表3]，..]`

17. Tuple 元组 `(数据1,数据2,数据3)`：一个元组可以存储多个数据，**元组内的数据是不能修改的**。只支持查找。

    1. 多个数据元组 `(10,20,30)`

    2. 单个数据元组`(10,)`，若单个数据元组内没有逗号，则该数据是什么类型，此参数即什么类型。

    3. 按下标查找数据：`tuple1[0]`

    4. `index()`查找某个数据，如果存在返回下标，否则报错。

       ```pyt
       tuple1 = ('aa','bb','cc','bb')
       print(tuple1.index('aa'))	# 0
       ```

    5. `count()`：数据出现的次数，`tuple1('aa')`

    6. `len()`：长度

    7. 如果元组里面有列表，列表里面的数据可以修改。

       ```pyt
       tuple1=('a','b',['cc','dd'])
       tuple1[2][0] = 'Tom'
       ```

18. 字典：数据以键值对形式出现，字典数据和数据顺序没有关系，即字典不支持下标。

    1. `dict = {'name':'Tom', 'age':20}`

    2. 增加：`字典序列[key] = 值`：`dict['gender']='男'`。如果key不存在，则新增，如果key存在，则修改。

    3. 删除：`del dict['age']`或者`del(dict['age'])`

    4. 清空：`clear()`

    5. 查找：`key`值查找， `字典序列['key']`，若key值不存在报错

    6. 查找：`get()`查找 `字典序列.get(key,默认值)`

       ```python
       dict2 = {'name':'Tom', 'age':20, 'gender':'男'}
       print(dict2.get('name'))
       print(dict2.get('id',110))  #如果id不存在，则返回100；如果省略第二个参数，且key不存在，则返回None
       ```

    7. 查找：`keys()`，返回字典中所有的key返回可迭代对象

       ```python
       print(dict2.keys())
       # dict_keys(['name', 'age', 'gender'])
       ```

    8. 查找：`values()`，返回字典中所有key对应值的可迭代对象

       ```python
       print(dict2.values())
       # dict_values(['Tom', 20, '男'])
       ```

    9. 查找：`items()`，返回键值对，以元组形式输出可迭代对象，元组数据1为key，元素数据2为value

       ```python
       print(dict2.items())
       # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])
       ```

    10. 字典循环遍历key 

       ```python
       for key in dict2.keys():
       	print(key)
       ```

    11. 字典循环遍历value

        ```python
        for value in dict2.values():
            print(value)
        ```

    12. 字典循环遍历元素(元组)

        ```python
        for item in dict2.items():
            print(item)
        ```

    13. 字典循环遍历键值对

        1. ```python
           for key,value in dict2.items():
               print(f'{key} = {value}')
           ```

19. 集合使用`{}`或`set()`，若要创建空集合只能使用`set()`，因为`{}`用雷创建空字典。集合是可变类型。

    1. 集合数据特点：去重复

    2. 集合没有顺序

       ```python
       s1={10,20,50,30}
       s2=set('abcdegg')
       ```

    3. 增加单一数据`add()`，若追加的数据是当前集合已有数据的话，不进行任何操作

       ```python
       s1.add(100) #若追加s1.add([10,20])会报错
       ```

    4. `update()`追加的是序列，若追加单一数据，则会报错

       ```python
       s1.update([30,50,70,90])  # s1.update(10) 会报错
       ```

    5. `remove()`删除集合中的指定数据，如果数据不存在则报错（删除单个数据）

    6. `discard()`删除集合中的指定数据，如果数据不存在也不会报错

    7. `pop`随机删除集合中的某个数据，并返回这个数据

    8. 查找数据`in` 和`not in`，如`print(10 in s1)`

20. 运算符

    1. 序列，指的是一种包含多项数据的数据结构，序列包含的多个数据项（也叫成员）按顺序排列，可通过索引来访问成员。 Python 的常见序列类型包括字符串、列表和元组
    
    | 运算符  | 描述  | 支持的容器类型  |  
    |---|---|---|
    |  + |  合并 |  字符串、列表、元组 |  
    |  * |  复制 |   |  字符串、列表、元组  | 
    | in  |  元素是否存在 |   字符串、列表、元组、字典 |  
    |  not in |  元素是否不存在 |  字符串、列表、元组、字典 |

21. 公共方法


|  函数 | 描述  |  
|---|---|
| len()  | 计算容器中元素个数  |  
|  del或del() | 删除 （可根据下标删除） | 
|  max() |  返回容器中元素最大值 | 
|  min() | 返回容器中元素最小值  | 
|  range(start,end,step) |  生成start到end的数组（不包含end），步长为step（可省略，默认值1）的可迭代对象，共for循环使用 | 
| enumerate()  | 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中  | 


1. `enumerate(可便利对象, start = 0)`，start参数用来设置遍历数据的下标起始值，默认为0.

   ```python
   list = ['a','b','c','d','e']
   for i in enumerate(list):
       print(i)
   # 输出: enumerate返回结果是元组，元组第一个数据是原迭代对象的数据对应下标，元组第二个数据是元迭代对象的数据
   #(0, 'a')
   #(1, 'b')
   #(2, 'c')
   #..
   ```

22. 容器类型转换

    1. 将某个序列转换为元组tuple

       ```python
       list1 = [10,20,30,40,20,50]
       s1 = {100,300,400,500}
       t1 = ('a','b','c','d','e')
       print(tuple(list1))
       print(tuple(s1))
       ```

    2. 将某个序列转换为列表list

       ```python
       print(list(s1))
       print(list(t1))
       ```

    3. 将某个序列转换集合set，注意： 转成集合后若有相同内容则被去除

       ```python
       print(set(list1))
       print(set(t1))
       ```

23. 推导式：用一个表达式创建一个有规律的列表或空值一个有规律的列表。没有规律可以创建规律！

    1. 例如给空数组`list[]`添加数字0-9，可使用while循环和`list.append`添加，以及for循环的`list.append`

    2. 推导式：

       ```python
       list1=[i for i in range(10)]  # 第一个i为返回值
       
       # 创建偶数
       list2 =[]
       for i in range(10):
       	if i%2 ==0:
               list2.append(i)
       #带有if的列表推导式
       list1=[i for i in range(10) if i% 2 == 0]
       
       #创建列表如：[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
       #多个for循环实现列表推导式
       list1=[(i,j) for i in range(1,3) for j in range(3)]
       ```



24. 字典推导式：快速合并列表为字典或提取字典中目标数据

    1. 案例：创建一个字典：字典key是1-5数字，value是这个数字的次方。

       ```python
       dict1 = {i:i**2 for in range(1,5)}
       print(dict1)	#{1:1,2:4,3:9,4:16}
       # **合并两个列表为一个字典**
       list1 = ['name','age','gender']
       list2 = ['Tom',20,'man']
       dict1 = {list1[i]: list2[i] for i in range(len(list1))}
       print(dict1)
       # 如果两个列表数据个数相同， len统计任何一个列表长度都可以
       # 如果两个列表数个个数不同，len统计多的个数会报错，只能统计个数少的不会报错len(list2)
       # **提取字典中目标数据**
       consts = {'MBP':268, 'HP':125, 'DELL':201}
       ```

    2. 案例需求：提取上述电脑数量大于200的字典数据

       ```python
       counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
       count1 = {key: value for key, value in counts.items() if value >= 200}
       print(count1) # {'MBP': 268, 'DELL': 201}
       #普通方法
       count2= {}
       for key,value in counts.items():
           if value >= 200:
               count2[key]=value
       print(f'count2值是{count2}')
       ```

25. 函数：将一段具有独立功能的代码块，整合到一个整体并命名。实现代码重用。函数先定义再调用。

    1. 参数

       ```python
       # def 函数名(参数)：
       #  	  代码1
       #     代码2
       #     ...
       def add_num(a,b):
           result = a+b
       ```

    2. 函数返回值`return`

       ```python
       # def 函数名()：
       #  	  return 值
       ```

    3. 函数的说明文档:`help(函数名)`，查看函数的说明文档，只能放在第一行

       ```python
       # def 函数名()：
       #  	 """说明文档的位置"""
       #	代码
       ```

    4. 函数嵌套调用

       1. ```python
          def testB():
              return print("B")
          def testA():
              testB()
              return print("A")
          testA()
          ```

    5. 函数有作用域：

       1. 局部变量，函数体内部临时保存数据

       2. 全局变量

          1. 在函数体内修改全局变量的值，普通方法修改无法达成
          2. 在函数体内修改全局变量使用`global XX`

       3. ```python
          a = 100
          print(a)
          def testA():
              print(a)
          def testB():
              a=200 #新的局部变量
              print(a)
          print(a)
          def testC():
              global a #全局变量
              a=300
              print(a)
          print(a)    
          ```

    6. 位置参数：调用函数时根据函数定义的参数位置来传递参数，必须按照顺序写入参数

    7. 关键字参数，通过`键=值`形式加以指定，可以不用按照顺序，如`user('Tim',age=20,gender='girl')`；若有参数不想写关键字，则必须写在前面，按照位置参数来写。

    8. 缺省参数：即默认参数，为参数提供默认值，如`user(name,age,gender='boy')`指定了默认性别，可省略参数gender。

    9. 不定长参数：可变参数，不确定调用的时候会传递多少个参数（不传参也可以）。此时用包裹`packing`位置参数或者包裹关键字参数。

       1. 包裹位置传递：

          1. ```python
             def user(*args): 
                 print(args)
             user('Tom',21,'man')   
             user('Tom','student')
             ```

          2. 传进的所有参数都会被args变量手机，它会根据传进参数的位置合并为一个元组tuple。args是元组类型，这就是包裹位置传递。

       2. 包裹关键字传递：`def user(**kwargs): print(kwargs)`

          1. ```python
             def user(**kwargs):
                 print(kwargs)
             user(name='Tom',age=18,id=10)
             # {'name': 'Tom', 'age': 18, 'id': 10}
             ```

          2. 无论是包裹位置传递还是关键字传递，都是一个组包的过程。

    10. 拆包：元组

        1. ```python
           def return_num():
               return 100,200
           num1,num2 = return_num()
           print(num1)
           print(num2)
           ```

    11. 拆包：字典

        1. ```python
           dict1 = {'name':'Tom', 'age':18}
           a,b = dict1
           print(dict1[a]) # Tom
           print(b)		# age	
           ```

    12. 交换变量

        1. 方法一：借助第三个临时变量来交换两个数据变量

        2. 方法二：

           1. ```python
              a,b=1,2
              a,b=b,a
              print(a)
              print(b)
              ```

26. 引用：**在python中，值是靠引用来传递的**。可以用`id()`来判断两个变量是否为同一个值的引用，将id值理解为那块内存的地址表示。

    1. int类型为不可变类型

       ```python
       a=1
       b=a
       print(b)	# 1
       print(id(a))  # 1945375604976
       print(id(b))  # 1945375604976
       
       a=2
       print(b) 	# 1  不可变类型
       ```

    2. 列表为可变类型

       ```python
       aa = [10,20]
       bb=aa
       print(id(aa)) # 1726621398656
       print(id(bb)) # 1726621398656
       
       aa.append(30)
       print(id(aa)) # 1726621398656
       print(bb) # [10, 20, 30]
       ```

    3. 引用当实参传入

       ```python
       # int不可变
       def test1(a):
           print(a)
           print(id(a))  # int不一样:2231664384464 	列表一样：2363173135360
           a+=a
           print(id(a))  # int不一样:2231664381264	列表一样：2363173135360
       
       b=100
       test1(b)
       # 列表[100,200]   2363173135360
       
       ```

27. 可变和不可变类型：数据能够直接进行修改，如果能直接修改那么可变，否则就是不可变。

    1. ```markdown
       | 可变类型  | 不可变类型  |  
       |---|---|
       |  列表、字典、集合 | 整型、浮点型、字符串、元组  | 
       ```

28. 在函数中进行判断语句后使用`return`，当执行`return`后表示**退出当前函数**。

29. 递归的特点：函数内部自己调用自己；必须有出口。

    ```python
    #例如：3以内的数字累加和
    def sum_number(num):
        #2. 出口
        if num == 1:			 
            return 1			# -> 返回上次函数调用的地方 即sum_numbers(num-1)
        #1. 当前数字 + 当前数字减1的累加和
        return num + sum_numbers(num-1)  # -> 最后一次调用的地方时sum_numbers(3)的主体函数的输入
    ```

    1. 为了避免内存溢出和性能影响设置了最大递归深度为998, 当调用栈超过998层就会报错
    2. `return`返回的时上一次函数调用的地方 [图示](pics/digui.JPG)

30. lambda表达式： 如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化。

    1. 语法： `labmda 参数列表 ： 表达式(须有返回值)`

    2. labmda表达式的参数可有可无，函数的参数在lambda表达式中完全适用。

    3. lambda表达式能接收任何数量的参数但只能返回一个表达式的值。

       ```python
       #1 函数
       def fn1():
           return 100
       result = fn1()
       #2 lambda 匿名函数
       fn2 = lambda: 100
       print(fn2)  # 输出的是lambda的内存地址<function <lambda> at 0x000001CE5FD43F40>
       print(fn2())  # 输出100
       ```

    4. 关于labmda的参数有无写法

       ```python
       #无参数
       fn1 = lambda: 100
       #一个参数
       fn1 = lambda a:a
       print(fn1('hello world'))
       #默认参数
       fn1 = lambda a,b,c=100: a+b+c  #默认值c为100
       print(fn1(10,20))
       #可变参数(不定长参数)
       fn1 = lambda *args: args
       print(fn1(10,20,30))		# 输出元组 (10,20,30)
       #可变参数 **kwargs
       fn1 = lambda **kwargs: kwargs
       print(fn1(name='python',age=20))	#返回字典dict
       ```

    5. 带判断的lambda

       ```python
       #简单的判断
       fn1 = lambda a,b: a if a> b else b #与三目运算合用
       print(fn1(100,50))
       #列表数据按字典key的值排序
       students = [
           {'name':'Tom','age':20},
           {'name':'Tim','age':21},
           {'name':'Sam','age':23}
       ]
       #按name值升序排序
       students.sort(key=lambda x: x['name'])
       print(students)
       #按name值降序排列
       students.sort(key=lambda x: x['name'], reverse=True)
       print(students)
       ```

31. 高阶函数：把函数作为参数传入

    1. 内置高阶函数

       1. `abs(值)`：绝对值
       2. `round(值)`：四舍五入
       3. `map(函数func, 列表list)`：将传入的函数变量func作用到每个元素中，并将结果组成新的列表Python2 / 迭代器Python3返回。
       4. `reduce(函数func, 列表list)`：func必须有两个参数，每次func计算的结果继续和序列的下一个元素做积累计算。
       5. `filter(函数func, 列表list)`：用于过滤序列，过滤不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用`list()`来转换。

    2. 高阶函数：`f`是第三个参数，用来接收将来传入的函数

       ```python
       #高阶介绍
       def sum1(a,b,f):
           return f(a)+f(b)
       print(sum1(3,-5,abs))
       # map例子
       list12 = [1,2,3,4,5]
       def func(x):
           return x**2
       result = map(func,list12)
       print(result)		# <map object at 0x0000022B9B733A60>
       print(list(result))	# [1, 4, 9, 16, 25]
       #reduce
       import functools
       def func(a,b):
           return a+b
       result = functools.reduce(func,list12)
       print(result)	# 15
       #filter过滤
       def func(x):
           return x % 2 == 0
       result = filter(func,list12)
       print(result)		# <filter object at 0x0000019B5D597CD0>
       print(list(result))	# [2, 4]
       ```

32. 文件操作

    1. `open(name, mode)`：打开一个已经存在的文件，或者创建一个新文件

       1. name：要打开的目标文件名的字符串（可以包含文件所在的具体路径）。

       2. mode：设置打开文件的模式（访问模式），只读、写入、追加等。

          ```python
          f = open('../pics/test.txt','w') # f为文件对象
          f.write('aaa')
          f.close()
          ```

          | 模式  | 描述  |
          |---|---|
          | r  | 以**只读方式打开**文件。文件的指针将会放在文件的开头，这是默认模式，如果文件不存在，报错。 |
          | rb  |  以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式 |
          | r+  |  打开一个文件用于读写。文件指针将会放在文件的开头。 |
          | rb+  |  以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
          | w  | 打开一个文件只用于**写入**。如果文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
          | wb  | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从头开始编辑，即原有内容会被删除。如果该文件不存在，则创建新文件。  |
          | w+  |  打开一个文件用于读写。如果该文件已存在则打开文件，并从头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
          | wb+  |  以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
          | a  | 打开一个文件用于**追加**。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容会被写入到已有内容之后，如果该文件不存在，创建新文件进行写入。 |
          | ab | 以二进制格式打开一个文件用于追加。如果文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容会被写入到已有内容之后。如果文件不存在，创建新文件进行写入。 |
          | a+ | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时回事追加模式。如果文件不存在，创建新文件用于读写。文件指针后面没有数据，所以无法读取。 |
          | ab+ | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |
          
       3. 访问模式可以省略，默认模式为`r`.

       4. 注意w+、a+、r+指针，等读取数据有影响。

    2. `read()`：如`文件对象.read(num)`表示从文件中读取的数据长度（单位是字节），如果没有传入num，则表示读取文件中所有的数据。注意：换行符`\n`页占2个字节数。

    3. `readlines()`：按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。

       ```python
       f2 = open('../pics/test.txt')
       content = f2.readlines()
       print(content) #['aaa\n', 'bbb\n', 'ccc\n', 'ddd']
       ```

    4. `readline()`：一次读取一行内容。第一次调用读取第一行，第二次读取调用第二行。

    5. `write()`：写文件

    6. `seek()`：用来移动文件指针

       1. `文件对象.seek(偏移量，起始位置)`：0代表文件开头、1代表当前位置、2代表文件结尾。

       2. ```python
          f3 = open('../pics/test.txt','r+')
          # 1.改变读取数据开始位置,向后偏移2个单位
          f3.seek(2,0)
          # 2.把文件指针放结尾（无法读取数据）
          f3.seek(0,2)
          con = f3.read()
          print(con)
          f3.close()
          ```

    7. 文件备份案例

       1. ```python
          # 1.获取要复制的文件
          old_name = input("输入要备份的名字： ")
          print(old_name)
          print(type(old_name))
          # 2.提取后缀 test.txt 找到名字中的点，名字和后缀分离
          index = old_name.rfind('.')
          print(index)
          # 3.切片分离
          print(old_name[0:index])
          print(old_name[index:])
          new_name = old_name[0:index] + '[备份]' + old_name[index:]
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
          ```

    8. 在Python中文件和文件夹的操作要借助`os模块`里面的功能

       1. 导入os模块：`import os`
       2. `os.rename(旧名，新名)`重命名，适用于文件和文件夹
       3. `os.remove(文件名)`删除
       4. 获取当前目录`os.getcwd()`
       5. 创建文件夹`os.mkdir(名)`
       6. 删除文件夹`os.rmdir(名)`
       7. 改变默认目录`os.chddir`
       8. 获取某个文件夹下所有文件，返回一个**列表**`listdir()`，默认当前文件夹

33. 面向对象

    1. 类名语法：遵循大驼峰命名习惯

    2. ```python
       class 类名():
           代码..
       对象名 = 类名()    
       # 比如
       class Washer():
           def wash(self):
               print("wash machine")
               print(self) # 2.2 <__main__.Washer object at 0x0000023111887E80>
       haier = Washer()   #1.海尔对象传入Washer里的wash的self     
       print(haier) # 2.1 <__main__.Washer object at 0x0000023111887E80>
       ```

    3. `self`：指的是调用该函数的对象

    4. 属性：既可以在类外添加和获取，也可以在类里面添加和获取

       1. 类外设置属性：`对象名.属性名 = 值`
       2. 类里设置属性：`self.属性名`

    5. 魔法方法：`__xx__()`格式的函数叫做魔法方法，指的是具有特殊功能的函数。

    6. `__init__()`：初始化对象

       ```python
       class Washer():
           #定义__init__，添加实例属性
           def __init__(self): # __init__()创建一个对象时默认被调用，不需要手动调用    
               self.width=500
               self.height = 800
           def print_info(self):
               print(f'洗衣机的宽度{self.width}，高度时{self.height}')
           #带参数初始化值
           def __init__(self,width,height):    
               self.width = width
               self.height = height
       haier1 = Washer(20,30)        
       ```

    7. `__str__()`：默认打印内存地址，与java的`toString`类似。如果定义了`__str__(self)`方法，就会打印从这个方法中`return`的数据。

    8. `__del__()`：当删除对象时，python解释器也会默认调用`__del__()`方法。

    9. 烤地瓜案例：

       ```python
       class Potato():
           def __init__(self): #设置属性初始状态
               self.cook_time = 0
               self.cook_static = '生的'
               self.condiments = []
           def cook(self,time):
               self.cook_time += time
               if 0 <= self.cook_time <3:
                   self.cook_static = '生的'
               elif 3<=self.cook_time<5:
                   self.cook_static='半生不熟'
               elif 5<= self.cook_time < 8:
                   self.cook_static = '输了'
               elif 8 <= self.cook_time:
                   self.cook_static = '焦了'
           def add_condiments(self,condiment):
               """添加调料"""
               self.condiments.append(condiment)
           def __str__(self):
               return f'这个地瓜烤了{self.cook_time}秒，现在是{self.cook_static},添加有{self.condiments}种调料'
       
       digua = Potato()
       digua.cook(2)
       digua.add_condiments('盐')
       print(digua)
       digua.add_condiments('辣椒面')
       digua.cook(2)
       print(digua)
       ```

34. 继承两个版本

    1. 经典类：不由任意内置类型派生出的类，称之为经典类

       1. ```python
          class 类名：
          	代码...	
          ```

    2. 新式类：Python3.0解释器默认使用

       1. ```python
          class 类名(object)： # object为基类
          	代码..
          ```

    3. 所有类默认继承object类，object类时顶级类或基类了其他子类叫做派生类。

       1. ```python
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
          ```

    4. 单继承：一个父类继承给子类

    5. 多继承：一个类同时继承了多个父类。一个类多个父类的时候，默认使用第一个父类的同名属性和方法。

    6. 子类重写父类同名方法和属性：若子类父类有相同方法和属性，则使用子类自身同名的属性和方法。

    7. `__mro__()`：打印类的继承顺序。如`C.__mro__()`

    8. 子类调用父类同名的属性和方法：

       1. ```python
          class Prentice(School, Master):
          	def __ini__(self):
                  self.kongfu = '[独创煎饼果子]'
              def make_cake(self):
                  #如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
                  self.__init__()	# 如果不加自己的初始化，kongfu属性值是上次调用init内的kongfu属性值
                  print(f'运用{self.kongfu}制作煎饼果子')
              # 调用父类同名方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化    
              def make_master_cake(self):
                  Master.__init__(self) # 想要调用父类的同名方法和属性，属性在init初始化位置，所以要再次调用init
                  Master.make_cake(self) # 把父类同名属性和方法再次封装
              def make_school_cake(self):
                  School.__init__(self)
                  School.make_cake(self)
          ...
          ```

    9. 多层继承

    10. `super()`调用父类方法：使用`super()`可以自动查找父类

        1. ```python
           # 普通调用父类方法和属性
           def make_old_cake(self): 
               Master.__init__(self)
               Master.make_cake(self)
               School.__init__(self)
               School.make_cake(self)
           # 使用super方法    
           # 1. 带参数super(当前类名,self).函数()  若父类页调用爷爷类，则父类爷爷类都会调用
           super(Prentice,self).__init__()	
           super(Prentice,self).make_cake()
           # 2. 没有参数
           super().__init__()
           super().make_cake()
           ```

    11. 私有权限：为实例属性和方法设置私有权限，子类无法使用。定义私有语法，使用前缀`__XX`。

    12. 获取和修改私有属性值：定义函数名`get_xx`获取私有属性，定义`set_xx·修改私有属性。

        1. ```python
           def get_money(self):
               return self.__money
           def set_money(self):
               self.__money = 500
           ```

        2. 






























