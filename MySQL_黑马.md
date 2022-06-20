# MySQL 8.0.26

1. ### 服务

   1. 安装的时候注意 Windows Service Name名称。默认开机启动。
   2. 启动与关闭方式一：在系统的Service里面找到对应的MySQL服务，进行启动和关闭。
   3. 启动和关闭方式二：命令行。`net start mysql80` 和  `net stop mysql80`。（mysql80为安装时的服务名称）
   4. 客户端连接方式一：命令行（需要配置环境变量）。`mysql [-h 127.0.0.1] [-P 3306] -u root -p`
      1. `MySQL\MySQL Server 8.0\bin`
   5. 客户端连接方式一：MySql命令窗口直接进入。

2. ### MySql数据库

   1. 关系型数据库 RDBMS：建立在关系模型基础上，由多张相互连接的二维表组成的数据库。
      1. 基于表存储的数据库为关系型数据库。

3. ### SQL

   1. 通用语法：可以单行或多行书写，以分号结尾。

   2. 不区分大小写，关键字建议使用大写。

   3. 注释：

      1. 单行注释： `--注释内容` 或 `#注释内容`
      2. 多行注释：`/*注释内容*/`

   4. SQL分类

      | 分类 | 全称                       | 说明                                                   |
      | ---- | -------------------------- | ------------------------------------------------------ |
      | DDL  | Data Definition Language   | 数据定义语言，用来定义数据库对象（数据库，表，字段）   |
      | DML  | Data Manipulation Language | 数据操作语言，用来对数据库表中的数据进行增删改         |
      | DQL  | Data Query Language        | 数据查询语言，用来查询数据库中表的记录                 |
      | DCL  | Data Control Language      | 数据控制语言，用来创建数据库用户、控制数据库的访问权限 |

4. ### DDL 库&表结构操作

   1. DDL 数据库操作( `[..]`可选 )：

      1. 查询：查询所有数据库 `show databases;`  查询当前数据库 `select database();`
      2. 创建：`create database [if not exists] 数据库名 [default charset 字符集] [collate 排序规则];`
      3. 删除：`drop database [if exists] 数据库名;`
      4. 使用：`use 数据库名;`

   2. DDL 表操作 **查询**：

      1. 查询当前数据库所有表：`show tables;`
      2. 查询表结构：`desc 表名;`
      3. 查询指定表的建表语句：`show create table 表名;`

   3. DDL 表操作 **创建**：

      ```sql
      create table 表名(
      	字段1 字段1类型[comment 字段1注释],
          字段2 字段2类型[comment 字段2注释], #如 name varchar(50) comment '姓名',
          ...
      )[comment 表注释];
      ```

   4. DDL 表操作 **数据类型**：数值类型、字符串类型、日期时间类型。

      1. ![数值](https://github.com/brant8/mypython/blob/master/pics/mysql_int.png)
      2. DECIMAL：大小取决于精度和标度，比如 `123.45`，精度表示5，标度表示2。
      3. 具体使用：
         1. 比如 ：`age TINYINT UNSIGNED`表示无符号取值范围（即只能取正数）
         2. 比如：`score double(4,1)`表示100以内的数，只有1个小数，如95.9。
      4. ![字符串](https://github.com/brant8/mypython/blob/master/pics/mysql_char.png)
      5. `char`性能好，`varchar()`性能差。
         1. `char(10)`表示最大10个字符，不足10个空格自动补齐。
         2. `varchar(10)`表示最大10个字符，若不足10个按多少有多少来算（需要去计算长度才知道占多少）。
         3. 具体使用：如username使用varchar，gender使用char。
      6. ![字符串](https://github.com/brant8/mypython/blob/master/pics/mysql_time.png)

   5. 举例：

      ```sql
      create table employment(
      	id int comment '编号',  --编号纯数字
          workno varchar(10) comment '工号', --字符串类型，长度不超过10位
          name varchar(10) comment '姓名', --字符串类型，长度不超过10位
          gender char(1) comment '性别', --男/女，存储一个汉字
          age tinyint unsigned comment '年龄', --正常人年龄，不可能存储负数
          idcard char(10) comment '身份证号', --二代身份证号均为18位
          entrydate date comment '入职时间'--取值年月日即可
      ) comment ‘员工表';
      ```

   6. DDL 表操作 **修改**

      1. 添加字段：`alter table 表名 add 字段名 类型(长度) [comment ‘注释’] [约束];`
      2. 修改数据类型：`alter table 表名 modify 字段名 新数据类型(长度);`
      3. 修改字段名和字段类型：`alter table 表名 change 旧字段名 新字段名 类型(长度) [comment "注释"] [约束]；`
      4. 删除字段：`alter table 表名 drop 字段名;`
      5. 修改表名：`alter table 表名 rename to 新名`

   7. DDL 表操作 **删除**

      1. 删除表：`drop table [if exists] 表名;`
      2. 删除指定表，并重新创建该表：`truncate table 表名;`

5. ### DML 数据操作

   1. DML **添加**数据
      1. 给指定字段添加数据：`insert into 表名(字段1，字段2,...) values(值1,值2,...);`
      2. 给全部字段添加数据：`insert into 表名 values(值1,值2,...);`
      3. 批量添加数据：`insert into 表名(字段1,字段2,...) values(值1,值2,...), (值1,值2,...);`
      4. 批量添加数据：`insert into 表名 values(值1,值2,...),(值1,值2,...);`
      5. *注意事项：插入数据时，字符串和日期型数据应该包含在引号中，且插入数据大小应在字段规定范围内*。
   2. DML **修改**数据
      1. 更新数据：`update 表名 set 字段名1 = 值1, 字段名2 = 值2,...[where 条件];`
      2. *注意事项：如果没有条件，表示修改表中所有数据*
   3. DML **删除**数据
      1. 删除命令：`delete from 表名 [where 条件]`
      2. *注意事项：如果没有条件，则会删除整张表的所有数据，删除语句不能删除某个字段的值（可以使用update）*

6. ### DQL 查询数据

   1. DQL语法 **编写顺序**：

      1. `SELECT 字段列表 FROM 表名列表 WHERE 条件列表 GROUP BY 分组字段列表 HAVING 分组后条件列表 ORDER BY 排序字段列表 LIMIT 分页参数`

   2. DQL **执行顺序**：

      1. `from` - `where` - `group by` - `select` - `order by` - `limit` ：使用表别名、字段别名时需要注意先后顺序

      1. *分组通常与聚合函数配合，如count、max、min、avg、sum*

   3. DQL **基本**查询

      1. 查询多个字段：`select 字段1, 字段2,字段3, ... from 表名;`
      2. 查询所有字段：`select * from 表名;` 一般工作不推荐写`*`
      3. 设置别名：`select 字段1 [as '别名1']， 字段2 [as '别名2'] ... from 表名;` 其中`as`可以省略。
      4. 去除重复记录：`select distinct 字段列表 from 表名;`

   4. QDL **条件**查询

      1. 语法：`select 字段列表 from 表名 where 条件列表;`

      2. 条件

         | 比较运算符       | 功能                                                         | 逻辑运算符  | 功能                         |
         | ---------------- | ------------------------------------------------------------ | ----------- | ---------------------------- |
         | >                | 大于                                                         | AND 或 &&   | 并且（多条件同时成立）       |
         | >=               | 大于等于                                                     | OR 或 \|\|  | 或者（多个条件任意一个成立） |
         | <                | 小于                                                         | NOT 或 !    | 非，不是                     |
         | <=               | 小于等于                                                     | IS NOT NULL | 不是null的                   |
         | <> 或 !=         | 不等于                                                       |             |                              |
         | BETWEEN...AND... | 在某个范围之内（含最小、最大值）<br>若最小值和最大值顺序颠倒则查询不到。 |             |                              |
         | IN(...)          | 在in之后的列表中的值，多选一                                 |             |                              |
         | LIKE 占位符      | 模糊匹配（`'_'`匹配单个字符，`'%'`匹配人一个字符）           |             |                              |
         | IS NULL          | 是NULL                                                       |             |                              |

   5. DQL **聚合**函数 Aggregation Function

      1. 将一列数据作为一个整体，进行纵向计算。**注意：null值不参与所有聚合函数运算**。
      2. 常见聚合函数：count统计数量、max、min、avg、sum。
      3. 语法：`select 聚合函数(字段列表) from 表名;`

   6. DQL **分组**查询

      1. 语法：`select 字段列表 from 表名 [where 条件] group by 分组字段名 [having 分组后过滤条件]`
      2. where与having分别
         1. 执行时机不同：where是分组之前进行过滤，不满足where条件，不参与分组；而having是分组后对结果进行过滤。
         2. 判断条件不同：where不能对聚合函数进行判断，而having可以。
         3. 执行顺序：where **>** 聚合函数 **>** having
         4. *分组之后，查询的字段一般为聚合函数和分组字段，查询其他字段无任何意义。*
      3. 例子：`select gender, count(*) from emp group by gender`根据男女分别统计数量
      4. 例子：查询年龄小于45的员工，并根据工作地址分组，获取员工数量大于等于3的工作地址
      5. `select workaddress, count(*) from emp where age < 45 group by workaddress having count(*) >=3;`
      6. 讲解：先输出根据workaddress和count(*)选出工作地址&人数分组，**分组完后在结果中**筛选人数大于3的。

   7. DQL **排序**查询

      1. 语法：`select 字段列表 from 表名 order by 字段1 排序方式1, 字段2 排序方式2;`
      2. 排序方式：`asc`升序（默认值）， `desc`降序

   8. DQL **分页**查询

      1. 语法：`select 字段列表 from 表名 limit 起始索引,查询记录数;`
      2. **起始索引从0开始，起始索引 = （查询页码 - 1）* 每页显示记录数**
      3. 分页查询是数据库的方言，不同的数据库有不同的实现，MySQL中是LIMIT。
      4. 如果查询的是第一页数据，起始索引可以省略，直接简写为`limit 10` 

7. ### DCL 用户控制管理

   1. DCL 管理用户

      1. 查询用户：`use mysql;` `select * from user;`
      2. 创建用户：`create user '用户名'@'主机名' indentified by '密码';` 主机名表示允许在哪里访问。
         1. 任意主机访问：`'用户名'@'%'`
      3. 修改用户密码：`alert user '用户名'@'主机名' identified with mysql_native_password by '新密码';`
      4. 删除用户：`drop user '用户名'@'主机名';`

   2. DCL 常用权限控制

      1. | 权限                | 说明     | 权限   | 说明               |
         | ------------------- | -------- | ------ | ------------------ |
         | ALL, ALL PRIVILEGES | 所有权限 | DELETE | 删除数据           |
         | SELECT              | 查询数据 | ALTER  | 修改表             |
         | INSERT              | 插入数据 | DROP   | 删除数据库/表/视图 |
         | UPDATE              | 修改数据 | CREATE | 创建数据库/表      |

      2. **查询**权限：`show grants for '用户名'@'主机名';`

      3. **授予**权限：`grant 权限列表 on 数据库.表名 to '用户名'@'主机名';`

         1. 比如：`grant all on itcast.* to 'heima'@'%';`

      4. **撤销**权限：`revoke 权限列表 on 数据库名.表名 from '用户名'@'主机名';`

      5. *注意：多个权限之间使用逗号分割；授权是，数据库名和表名可以使用`*`进行通配，代表所有。*

8. ### 函数

   1. 函数是指一段可以直接被另一端程序调用的程序或代码。

   2. 使用场景：数据报表等信息直接调用函数快速返回。

   3. 字符串函数

      1. | 常用函数                     | 功能                                                         |
         | ---------------------------- | ------------------------------------------------------------ |
         | CONCAT（S1，S2，..Sn）       | 字符串拼接，将S1，S2，S3等拼接成一个字符串                   |
         | LOWER（STR）                 | 将字符串str全部转为小写                                      |
         | UPPER（STR）                 | 将字符串str全部转为大写                                      |
         | LPAD（str, n, pad）          | 左填充，用字符串pad对str的左边进行填充，达到n个字符串长度。<br>当填充长度小于字符串长度，直接截取n个字符串。 |
         | RPAD（str, n, pad）          | 右填充，用字符串pad对str的右边进行填充，达到n个字符串长度    |
         | TRIM（str）                  | 去掉字符串头部和尾部的空格                                   |
         | SUBSTRING（str, start, len） | 返回从字符串str从start位置起的len个长度的字符串。起始索引值为1。 |

      2. ```sql
         #比如
         select rpad('abcdefg',8,'-');
         select trim('&nbsp; hello world ');
         #案例：员工工号统一5位数，不足5位数的全部在前面补0. 如00001
         update emp set workno = lpad(workno, 5, '0');  -数据库数据直接变更，影响数据。
         ```

   4. 数值函数

      1. | 常用函数      | 功能                               |
         | ------------- | ---------------------------------- |
         | CEIL（X）     | 向上取整                           |
         | FLOOR（X）    | 向下取整                           |
         | MOD（x, y）   | 返回x/y的模（余数）                |
         | RAND（）      | 返回0~1内的随机数                  |
         | ROUND（x, y） | 求参数x的四舍五入的值，保留y位小数 |

      2. 比如：`select mod(3,4);`结果是3。`select mod(5,4);`结果是1。

   5. 日期函数

      1. | 常用函数   | 功能               | 常用函数                             | 功能                                              |
         | ---------- | ------------------ | ------------------------------------ | ------------------------------------------------- |
         | CURDATE()  | 返回当前日期       | MONTH（date）                        | 获取指定date的月份                                |
         | CURTIME()  | 返回当前时间       | DAY（date）                          | 获取指定date的日期                                |
         | NOW()      | 返回当前日期和时间 | DATE_ADD（date, INTERVAL expr type） | 返回一个日期/时间值加上一个时间间隔expr后的时间值 |
         | YEAR(date) | 获取指定date的年份 | DATEDIFF（date1, date2）             | 返回起始时间date1和结束时间date2之间的天数        |

      2. 比如：`select date_add(now(), INTERVAL 70 DAY);`显示当前时间70天后的时间，若为负数则往前70天。type：MONTH，YEAR，DAY

   6. 流程函数

      1. | 常用函数                                                     | 功能                                                         |
         | ------------------------------------------------------------ | ------------------------------------------------------------ |
         | `IF(value, t, f)`                                            | 如果value为true，则返回t，否则返回f                          |
         | `IFNULL(value1, value2)`                                     | 如果value1不为空，返回value1，否则返回value2                 |
         | `CASE WHEN [val1] THEN [res1] ... ELSE [default] END`        | 如果val1为true，返回res1，...否则返回default默认值（范围取值时常使用） |
         | `CASE [expr] WHEN [VAL1] THEN [res1] ... ELSE [default] END` | 如果expr的值等于val1，返回res1，...否则返回default默认值     |

      2. ```sql
         select if(false, 'OK', 'Error');
         select ifnull('','Default'); #返回空字符串
         select ifnull(null,'Default'); #返回default
         # 查询emp员工地址，北京/上海显示一线城市，其他二线城市
         select
         	name,
         	(case workaddress when '北京' then '一线城市' when '上海' then '一线城市' else '二线城市' end) as '工作地址'
         from emp;
         ```

9. ### 约束 Constraint

   1. 作用域表中字段上的规则，用于限制存储在表中的数据。

   2. 保证数据库中数据的正确、有效性和完整性。

   3. | 约束                     | 描述                                                     | 关键字         |
      | ------------------------ | -------------------------------------------------------- | -------------- |
      | 非空约束                 | 限制该字段的数据不能为null                               | NOT NULL       |
      | 唯一约束                 | 保证该字段的所有数据都是唯一、不重复的                   | UNIQUE         |
      | 主键约束                 | 主键时一行数据的唯一表示，要求非空且唯一                 | PRIMARY KEY    |
      | 默认约束                 | 保存数据时，如果未指定该字段的值，则采用默认值           | DEFAULT        |
      | 检查约束(8.0.16版本之后) | 保证字段值满足一条件                                     | CHECK          |
      | 外键约束                 | 用来让两张表的数据之间建立连接，保证数据的一致性和完整性 | FOREIGN KEY    |
      | 自动增长                 | 仅限在primary key中，且在oracle中使用另外一种自增。      | AUTO_INCREMENT |

   4. ```sql
      create table  user_2(
        id int primary key auto_increment comment '主键id',
        name varchar(10) not null unique comment '姓名',
        age int check ( age > 0 && age <= 120 ) comment '年龄',
        status char(1) default '1' comment '状态',
        gender char(1) comment '性别'
      );
      #插入数据例子
      insert into user_2(name, age, status, gender) values ('Tom1',19,'1','男'),('Tom2',23,'1','男');
      ```

   5. *注意：若插入数据失败后显示null，再插入下一条数据时，自增ID会跳过一个数。原因时因为即使插入数据失败，插入数据时会向数据库申请主键，即使失败。其他报错情况不会主键自增*

10. ### 外键约束

    1. 用来让两张表的数据之间建立连接，从而保证数据的一致性和完整性。

    2. **子表**：带有外键id的。

    3. **父表/主表**：外键id为主键id的。

    4. **添加**外键：

       1. 创建：`create table 表名( 字段名 数据类型， ...  [constraint] [外键名称] FOREIGN KEY (外键字段名) REFERENCES 主表(主表列明) );`
       2. 修改：`alter table 表名 add constraint 外键名称 foreign key (外键字段名) references 主键(主表列明);`
       3. 比如 `alter table emp add constraint fk_emp_dept_id foreign key (dept_id) references dept(id);`

    5. **删除**外键：`alter table 表名 drop foreign key 外键名称;` (子表的外键字段)

    6. **删除/更新行为**

       | 行为        | 说明                                                         |
       | ----------- | ------------------------------------------------------------ |
       | NO ACTION   | 在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新。（与RESTRICT一致） |
       | RESTRICT    | 在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新。（与NO ACTION一致） |
       | CASCADE     | 在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有，则也删除/更新外键在子健中的记录。 |
       | SET NULL    | 在附表中删除对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null（要求改外键允许取null）。 |
       | SET DEFAULT | 父表有变更时，子表将外键列设置成一个默认的值（Innodb不支持）。 |

    7. CASECADE 语法：`alter table 表名 add constriant 外键名称 foreign key (外键字段) references 主表名(主表字段名) on update cascade on delete cascade;`

    8. SET NULL 语法：`alter table 表名 add constriant 外键名称 foreign key (外键字段) references 主表名(主表字段名) on update set null on delete set null;`

11. ### 多表查询

    1. **一对多**：一个部门对应多个员工，一个员工对应一个部门。

       1. 实现：在多的一方建立外键，指向一的一方的主键。

    2. **多对多**：一个选胜可以选修多门课程，一门课程也可以供度过学生选择。

       1. 实现：建立第三张中间表，中间表至少包含两个外键，分别关联两方主键。

       2. 中间表外键语法：

          ```sql
          create table student_course(
              id int auto_increment comment '主键' primary key,
              studentid int not null comment '学生ID',
             	courseid int not null comment '课程ID',
              constraint fk_courseid foreign key (courseid) reference course(id),
              constraint fk_studentid foreign key (studentid) reference student (id)
          ) comment '学生课程中间表';
          ```

    3. **一对一**：一对一关系，用于单表拆分，将一张表的基础字段放在一张表中，其他的详情字段放在另一张表中，提生操作效率。

       1. 实现：在任意一方加入外键，关联另一方的主键，并且设置外键为唯一的UNIUQUE。

    4. **多表查询介绍**

       1. 笛卡尔积：数学中，两个集合A集合和B集合的所有组合情况，多表查询时，需要消除无效的笛卡尔积。
       2. 连接查询
          1. 内连接：相当于查询A、B交集部分数据
          2. 左外连接：查询左表所有数据，以及两张表交集部分数据
          3. 右外连接：查询右表所有数据，以及两张表交集部分数据
          4. 自连接：当前与自身的连接查询，子链接必须使用表别名
       3. 子查询

    5. 连接查询 内连接

       1. **隐士内连接**：`select 字段列表 from 表1, 表2 where 条件...;`
       2. **显示内连接**：`select 字段列表 from 表1 [inner] join 表2 on 连接条件..;` 关键字inner可以省略。

    6. 连接查询 外连接

       1. **左外连接**：`select 字段列表 from 表1 left [outer] join 表2 on 条件...;`
          1. 比如：查询emp表的所有数据，和对应的部门信息（emp有一条记录没有关联数据也会显示出来）
       2. **右外连接**：`select 字段列表 from 表1 right [outer] join 表2 on 条件...;`
          1. 比如：查询dept表的所有数据，和对应的员工信息（所有部门所对应的员工）

    7. 自连接 自己连接自己

       1. **自连接**语法：`select 字段列表 from 表A 别名A join 表A 别名B on 条件...;`
       2. 子链接查询，可以是内连接查询，也可以是外连接查询。

    8. **联合查询** union， union all

       1. union查询：把多次查询的结果合并起来，形成一个新的查询结果集。

       2. ```sql
          #语法
          select 字段列表1 from 表A ...  #结果集1
          union [all]					#有all结果集1和2合并保留重复，没有all结果集1和2合并且去重复
          select 字段列表2 from 表B ...; #结果集2
          #字段列表1和2必须保持一致，字段类型也需要保持一致
          ```

       3. 注意：*对于联合查询的多张表的列数必须保持一致，字段类型也需要保持一致*。

    9. **子查询**

       1. 概念：SQL语句中嵌套select语句，成为嵌套查询，又称子查询。

       2. 语法：`select * from t1 where column1 = (select column1 from t2);`

       3. 子查询外部的语句可以是 insert / update / delete / select 的任何一个。可以进行多层嵌套。

       4. 根据子查询结果不同，分为：

          1. **标量子查询**，即子查询结果为单个值（数字、字符串、日期等最简单形式）

             1. 比如：查询销售部的所有员工信息
             2. 分开查询：`select id from dept where name = "销售部"` 和 `select * from emp where dept_id = 4`
             3. 子查询形式：`select * from emp where dept_id = (select id from dept where name = "销售部")`

          2. **列子查询**，即子查询结果为一列，可以是多行

             1. 常用的操作符：

                | 操作符 | 描述                                   |
                | ------ | -------------------------------------- |
                | IN     | 在指定的集合范围内，多选一             |
                | NOT IN | 不在指定的集合范围之内                 |
                | ANY    | 子查询返回列表中，有任意一个满足即可   |
                | SOME   | 与ANY等同，使用SOME的地方都可以使用ANY |
                | ALL    | 子查询返回列表的所有值都必须满足       |

             2. 比如：查询销售部和市场部的所有员工信息

             3. 分开查询：`select id from dept where name='销售部' or name='市场部'`和`select * from emp where dept_id in (2,4)`

             4. 子查询形式：`select * from emp where dept_id in (select id from dept where name='销售部' or name='市场部')`

          3. **行子查询**，即子查询结果为一行（可以多列）

             1. 常用操作符：=、<>、IN、NOT IN。
             2. 比如：查询与张无忌的薪资及直属领导相同的员工信息
             3. 分开查询：`select salary, managerid from emp where name = '张无忌';`和`select * from emp where salary =12500 and managerid = 1;`
             4. 子查询等同形式：`select * from emp where (salary, managerid) = (12500, 1);`
             5. 子查询形式：`select * from emp where (salary, managerid) = (select salary, managerid from emp where name = '张无忌');`

          4. **表子查询**，即子查询结果为多行多列

             1. 常用的操作符：IN
             2. 比如：查询与张三、李四的职位和薪资相同的员工信息
             3. 分开查询：`select job, salary from emp where name = '张三' or name ='李四';`和`select * from emp where(job, salary) in ( ('职员',3750),('销售',4600) );`
             4. 子查询形式：`select * from emp where(job, salary) in (select job, salary from emp where name = '张三' or name ='李四');`

       5. **提示**：多张表查询时，不要一次性关联所有表，两两关联，即一次关联两个，每次关联使用`and`连接关联条件。

       6. IDEA格式化（美化）行阅读：CTRL + ALT + L

       7. 黑马多表查询[视频案例讲解](https://www.bilibili.com/video/BV1Kr4y1i7ru?p=49&spm_id_from=pageDriver&vd_source=31dc1543590614dbc49f7bf7cfc36195)。

12. ### 事务

    1. 事务时一组操作的集合，它是一个不可分割的工作单位，事务会把所有的操作作为一个整体一起向系统提交或撤销操作请求，即这些操作要么同时成功，要么同时失败。

    2. 默认MySQL的事务时自动提交的，也就是说，当执行一条DML语句，MySQL会立即隐式的提交事务。

    3. 事务操作

       1. 查看并设置手动事务提交：
          1. 查看：`select @@autocommit;`
          2. 设置事务提交方式：`set @@autocommit=0;` 事务自动提交值为`1`。
          3. 提交事务：`commit;`
          4. 回滚事务：`rollback;`
       2. 第二种开启事务的方式（不设置@@autocommit）:
          1. 开启事务：`start transaction 或 begin;`
          2. 提交事务：`commit;`
          3. 回滚事务：`rollback;`

    4. 事务四大特性

       1. 原子性 Atomicity：事务时不可分割的最小操作单元，要么全部成功，要么全部失败。
       2. 一致性 Consistency：事务完成时，必须使所有的数据都保持一致状态。
       3. 隔离性 Isolation：数据库系统提供的隔离机制，保证十五在不受外部并发操作影响的独立环境下运行。
       4. 持久性 Durability：事务一旦提交或回滚，它对数据库中的数据的改变就是永久的。

    5. 并发事务问题

       1. | 问题                               | 描述                                                         |
          | ---------------------------------- | ------------------------------------------------------------ |
          | 脏读 <br /> dirty read             | 一个事务督导另外一个事务还没有提交的数据。                   |
          | 不可重复度<br /> unrepeatable read | 一个事务先后读取同一条记录，但两次读取的数据不同，称之为不可重复读。 |
          | 幻读 <br /> phantom read           | 一个事务按照条件查询数据时，没有对应的数据行，但是在插入数据时，又发现这行数据已经存在，好像出现了“幻影”。 |

    6. 事务的隔离级别

       1. | 隔离级别                                                     | 脏读          | 不可重复读 | 幻读 |
          | ------------------------------------------------------------ | ------------- | ---------- | ---- |
          | Read uncommitted（安全性最差）                               | √（会出现）   | √          | √    |
          | Read committed（Oracle默认）                                 | ×（不会出现） | √          | √    |
          | Repeatable Read (MySQL默认)                                  | ×             | ×          | √    |
          | Serializable（性能最差，多个事务操作同个数据，需要等某个事务操作完毕其他事务才能操作） | ×             | ×          | ×    |

       2. 查看事务隔离级别：

          1. `select @@transaction_isolcation;`

       3. 设置事务隔离级别

          1. `set [session | global] transaction isolation level { read uncommitted | read committed  repeatable read | serializable };`

13. ### 基础结束

    1. 高级sql开始

14. ### 存储引擎

    1. ![MySql体系结构](https://github.com/brant8/mypython/blob/master/pics/mysql_struct.png)

    2. MySQL体系结构

       1. 连接层：最上层时一些客户端和连接服务，主要完成一些类似连接处理、授权认证、及相关的安全方案。服务器也会为安全接入的每个客户端验证它所具有的操作权限。
       2. 服务层：第二层架构主要完成大多数的核心服务功能，如SQL接口，并完成缓存的查询，SQL的分析和优化，部分内置函数的执行。所有跨存储引擎的功能也在这一层实现，如过程、函数等。
       3. 引擎层：存储引擎真正的负责了MYSQL中数据的存储和提取，服务器通过API和鵆引擎进行通信。不同的存储引擎具有不同的功能，这样我们可以根据自己的需要，来选取合适的存储引擎。
       4. 存储层：主要是将数据存储在文件系统之上，并完成与存储引擎的交互。

    3. 存储引擎就是存储数据、建立索引、更新/查询数据等技术的实现方式。存储引擎时基于表的，而不是基于库的，所以存储引擎也可被成为表类型。

    4. 指定存储引擎：`create table 表名(字段 字段类型 [comment 注释]...) engine=innodb [comment 表注释];`

    5. 查看当前数据库支持的存储引擎：`show engines;`

       1. 输出：引擎名、是否支持改引擎、注释、是否支持事务、XA、Savepoints
       2. MySQL早期默认存储引擎：MyISAM

    6. InnoDB：是一种兼顾高可靠性和高性能的通用存储引擎，在MySQL 5.5之后，InnoDB是默认的MySQL存储引擎。

       1. 特点：
          1. DML操作遵循ACID模型，支持事务
          2. 行级锁，提高并发访问性能
          3. 支持外键Foreign Key约束，保证数据的完整性和正确性
       2. 文件：`xxx.idb`
          1. `xxx`代表的是表名，innoDB引擎的每张表都会对应这样一个表空间文件，存储该表的表结构( frm, sdi )、数据和索引。表结构不可打开，储存方式为二进制文件。
          2. 参数：`innodb_file_per_table` 是否每张表对应一个表空间，版本8.0默认打开。
          3. 查看系统变量：`show variables like 'innodb_file_per_table`
          4. CMD查看表结构：`idb2sdi 表名.idb` （需要进入到该目录下）
       3. 逻辑存储结构 ![图示](https://github.com/brant8/mypython/blob/master/pics/mysql_innodb.png)

    7. MyISAM：早期MySQL的默认存储引擎。

       1. 特点：
          1. 不支持事务，不支持外键
          2. 支持表锁，不支持行锁
          3. 访问速度快
       2. 文件：`xx.MYD`数据、`xx.MYI`索引、`xx.自增序号.sdi`表结构（可打开json格式）

    8. Memory：表结构是存储在内存中的，由于受到硬件问题，或断电问题的影响，只能将这些表作为临时表或缓存使用。

       1. 特点：
          1. 内存存放
          2. hash索引（默认）
       2. 文件：`xx.sdi` 储存表结构信息

    9. 存储引擎特点

       | 特点         | InnoDB                 | MyISAM | Memory |
       | ------------ | ---------------------- | ------ | ------ |
       | 存储限制     | 64TB                   | 有     | 有     |
       | 事务安全     | 支持                   | -      | -      |
       | 锁机制       | 行锁 row-level locking | 表锁   | 表锁   |
       | B+tree索引   | 支持                   | 支持   | 支持   |
       | Hash索引     | -                      | -      | 支持   |
       | 全文索引     | 支持（5.6版本以后）    | 支持   | -      |
       | 空间使用     | 高                     | 低     | N/A    |
       | 内存使用     | 高                     | 低     | 中等   |
       | 批量插入速度 | 低                     | 高     | 高     |
       | 支持外键     | 支持                   | -      | -      |

    10. 存储引擎的选择

        1. InnoDB：如果应用对事务的完整性有较高的要求，在并发条件下要求数据的一致性，数据操作除了插入和查询之外，还包含很多的更新、删除操作，那么InnoDB是比较合适的选择。
        2. MyISAM：如果应用以读操作和插入操作为主，只有很少的更新和删除操作，并且对事务的完整性、并发性要求不是很高，那么选择这个存储引擎是非常合适的。现在被MongoDB替代。
        3. Memory：访问速度快，通常用于临时表及缓存。缺陷是对表的大小由限制，太大的表无法缓存在内存中，而且无法保障数据的安全性。现在被Redis取代。

15. ### 索引

    1. MySQL安装与服务

       1. 查询自动生成的root密码：`grep 'temporary password' /var/log/mysqld.log `
       2. 修改root用户密码：`alter user 'root'@'localhost' identified by '1234';`
       3. 参考命令：`./mysqld --initialize-insecure`
       4. 创建一个账户，可以允许远程连接，提示：`'user'@'%'`，远程连接失败尝试关闭防火墙。

    2. 索引 index 是帮助MySQL**高效**获取数据的**数据结构**（**有序**）。在数据之外，数据库系统还维护者满足特定查找算法的数据结构，这些数据结构以某种方式引用（指向）数据，这样就可以在这些数据结构上实现高级查找算法，这种数据结构就是索引。

    3. 索引优缺点

       | 优势                                                        | 劣势                                                         |
       | ----------------------------------------------------------- | ------------------------------------------------------------ |
       | 提高数据检索的效率，降低数据库的IO成本                      | 索引列也是要占用空间的。（比如MyISAM单独的索引文件）         |
       | 通过索引列对数据进行排序，降低数据排序的成本，降低CPU的消耗 | 索引大大提高了查询效率，同时却也降低更新表的速度，如对表进行insert、update、delete时，效率降低 |

    4. 索引结构

       | 索引结构              | 描述                                                         |
       | --------------------- | ------------------------------------------------------------ |
       | B+Tree索引（最常见）  | 最常见的索引类型，大部分引擎都支持B+树索引                   |
       | Hash索引              | 底层数据结构式用哈希表实现的，只有精确匹配索引列的查询才有效，不支持范围查询 |
       | R-tree（空间索引）    | 空间索引式MyISAM引擎的一个特殊索引类型，主要用于地理空间数据类型，通常使用较少 |
       | Full-text（全文索引） | 是一种通过建立倒排索引，快速匹配文档的方式。类似于Lucene，Solr，ES |

    5. 平时所说的索引，若没有特别说明，都是B+树结构组织的索引。

       | 索引       | InnoDB          | MyISAM | Memory |
       | ---------- | --------------- | ------ | ------ |
       | B+tree索引 | 支持            | 支持   | 支持   |
       | Hash索引   | 不支持          | 不支持 | 支持   |
       | R-tree索引 | 不支持          | 支持   | 不支持 |
       | Full-text  | 5.6版本之后支持 | 支持   | 不支持 |

    6. 二叉树

       1. 缺点 [图示](https://github.com/brant8/mypython/blob/master/pics/mysql_binary_tree.png)：顺序插入时，会形成一个链表，查询性能大大降低。大数据量情况下，层级较深，检索速度慢。

    7. B-Tree（多路平衡查找树）[网络视图展示法](https://www.cs.usfca.edu/~galles/visualization/)

       1. [图示](https://github.com/brant8/mypython/blob/master/pics/mysql_b_tree.png) 以一颗最大度数 max-degree 为5（5阶）的b-tree为例，每个节点最多存储4个可以，5个指针（指针值永远比节点大1）

    8. B+Tree

       1. [图示](https://github.com/brant8/mypython/blob/master/pics/mysql_b_p_tree.png)  以一颗最大度数 max-degree 为4（4阶）的b+tree为例，分叶子节点起到索引作用，底层叶子节点保存数据形成单向链表
       2. [图示](https://github.com/brant8/mypython/blob/master/pics/mysql_b_p_tree2.png) MySQL索引数据结构对经典的B+Tree进行了优化。在原B+Tree的基础上，增加一个指向相邻叶子节点的链表指针，就形成了带有顺序指针的B+Tree，提高区间访问的性能。
       3. 页的内容固定大小为16k（即16*1024个字节）。
       4. 树根只有一个节点，这个节点有16k的空间，可以保存的key和指针等于`n*8+(n+1)*6=16*1024`其中n为根节点存储key的数量，n+1表示指针的数量。

    9. Hash

       1. 采用一定的hash算法，将键值换算成新的hash值，映射到对应的槽位上，然后存储在hash表中。
       2. [图示](https://github.com/brant8/mypython/blob/master/pics/mysql_hash.png) 如果两个（或多个）键值，映射到一个相同的槽位上，就产生了hash冲突（hash碰撞），可以通过链表来解决。
       3. Hash索引特点
          1. Hash索引只能用于对等比较（=，in），不支持范围查询（between，>，<，...）
          2. 无法利用索引完成排序操作
          3. 查询效率高，通常只需要一次检索就可以了，效率通常要高于B+Tree索引。（hash碰撞出现后效率一般）
       4. 存储引擎支持：在MySQL中，支持hash索引的式Memory引擎，而InnoDB中具有自适应hash功能，hash索引式存储引擎根据B+Tree索引在指定条件下自动构建的。

    10. 为什么InnoDB存储引擎选择使用B+Tree索引结构

        1. 相对于二叉树，层级更少，搜索效率高
        2. 对于B-tree，无论式叶子节点还是非叶子节点，都会保存数据，这样导致一页中存储的键值减少，指针跟着减少，要同样保存大量数据，只能增加树的高度，导致性能降低。
        3. 相对hash索引，B+tree支持范围匹配及排序操作

    11. 索引分类

        | 分类     | 含义                                                 | 特点                     | 关键字   |
        | -------- | ---------------------------------------------------- | ------------------------ | -------- |
        | 主键索引 | 针对于表中主键创建的索引                             | 默认自动创建，只能由一个 | PRIMARY  |
        | 唯一索引 | 避免同一个表中某数据列中的值重复                     | 可以有多个               | UNIQUE   |
        | 常规索引 | 快速定位特定数据                                     | 可以有多个               |          |
        | 全文索引 | 全文索引查找的式文本中的关键字，而不是比较索引中的值 | 可以有多个               | FULLTEXT |

    12. Innodb存储引擎中，根据索引的存储形式分为下面两种

        | 分类                     | 含义                                                       | 特点                 |
        | ------------------------ | ---------------------------------------------------------- | -------------------- |
        | 聚焦索引 Clustered Index | 将数据存储与索引放到了一块，索引结构的叶子节点保存了行数据 | 必须有，而且只有一个 |
        | 二级索引 Secondary Index | 将数据与索引分开存储，索引结构的叶子节点关联的式对应的主键 | 可以存在多个         |

    13. 聚焦索引与二级索引的案例讲解（未来用于优化SQL语句）![图片](https://github.com/brant8/mypython/blob/master/pics/mysql_cluster_exp.png)

    14. 聚集索引选取规则 

        1. 如果存在主键，主键索引就是聚集索引 [图示](https://github.com/brant8/mypython/blob/master/pics/mysql_cluster.png), 
        2. 如果不存在主键，则把第一个唯一索引 UNIQUE 作为聚焦索引
        3. 如果不存在主键也没有合适的唯一索引，则InnoDB会自动生成一个rowid作为隐藏的聚集索引。

16. ### 索引语法

    1. **创建**索引：`create [unique | fulltext] index index_name on table_name (index_col_name,...);`

    2. **查看**索引：`show index from table_name;`

    3. **删除**索引：`drop index index_name on table_name;`

    4. **补充命令**：`show index from tb_user\G;`可以让输出表格错乱的形式以类似 json 形式罗列出来。

    5. 索引案例：

       1. name字段的值可能会重复，为该字段创建索引
          1. `create index idx_user_name on tb_user(name);` 常规索引
       2. phone手机号字段的值是非空、且唯一的，为该字段创建唯一索引。
          1. `create unqiue index idx_user_phone on tb_user(phone);`
       3. 为profession、age、status创建联合索引
          1. `create index index_user_pro_age_sta on tb_user(profession,age,status);` 顺序有讲究。
       4. 为email建立合适的索引来提升查询效率
          1. `create index idx_user_email on tb_user(email);`

    6. **SQL性能分析**（主要是查询优化）

       1. **SQL执行频率**：
          1. MySQL客户端连接成功后，通过`show [session | global] status`命令可以提供服务器状态信息。
          2. global表示全局，session表示当前会话信息。
          3. 通过如下指令，可以查看当前数据库的insert、update、delete、select的访问频次
          4. `show global status like 'Com_______';` 7个下划线。结果输出Variable_name如`Com_insert`。
          5. *通过查询执行频率来决定当前数据库操作方向来进行优化*。
       2. **慢查询日志**：
          1. 记录了所有执行时间超过指定参数（long_query_time，单位：秒，默认10秒）的所有SQL语句的日志。
          2. MySQL的慢查询日志默认没有开启，需要在MySQL的配置文件（`/etc/my.cnf`）中配置如下信息
             1. 查看有无开启慢查询：`show variable like 'slow_query_log';`
             2. 开启慢查询日志开关：`slow_query_log=1` 在配置文件中
             3. 设置慢查询时间为2秒，SQL语句执行超过2秒，视为慢查询，记录到慢查询日志：`long_query_time=2`
             4. 注释：windows下配置信息在`my.ini`；ubuntu的在`/etc/mysql/mysql.conf.d/mysqld.cnf`
          3. 配置完毕后，需要重新启动mysql服务进行测试，慢查询日志位置存在：`/var/lib/mysql/localhost-slow.log`
          4. linux命令：`tail -f xxx.log` 可以实时查看更新的内容
       3. **profile详情**：（粗略判定性能）
          1. `show profiles;`能够在做SQL优化时帮助我们了解时间耗费到哪里去了。通过`having_profiling`参数，能够看到当前MySQL是福哦支持profile操作。
          2. `select @@having_profiling;`查看是否支持profile 操作。
          3. 默认`profiling`值是`0`是关闭的，可以通过set语句在session/global级别开启profiling
          4. 开启：`set profiling = 1;`
          5. 开启后执行一系列SQL操作，然后通过指令查询执行耗时
          6. 查看SQL耗时基本情况：`show profiles;`
          7. 查看指定query_id的SQL语句各个阶段的耗时情况：`show profile for query query_id;`
          8. 查看指定query_id的SQL语句CPU使用情况：`show profile cpu for query query_id;`
       4. **explain执行计划**（**具体性能优化指标**）
          1. explain或者desc命令获取MySql如何执行select语句的信息，包括在select语句执行过程中如何连接和连接的顺序。
          2. explain也可以查看到是否用到索引。
          3. 语法：`explain select 字段列表 from 表名 where 条件;` 输出结果中的`key`表示索引
          4. 输出结果`id`：
             1. select查询的序列号，表示查询中执行select子句或者是操作表的顺序（id相同，执行顺序从上到下；id不同，值越大，越先执行）。
          5. 输出结果`select_type`：
             1. 表示select类型，常见的取值有simple（简单表，即不适用表连接或子查询）、primary（主查询，即外层的查询）、union（union中的第二个或者后面的查询语句）、subquery（select/where之后包含了子查询）等。
          6. 输出结果`type`：**性能指标**
             1. 表示连接类型，**性能由好到差**的连接类型为：Null、system、const、eq_ref、ref、range、index、all。
             2. Null：查询的时候不用任何表，比如`select 'A';`
             3. system：系统表
             4. const：主键/唯一索引
             5. eq_ref：唯一索引
             6. ref：非唯一性索引
             7. index：用了索引，对整个索引进行遍历扫描
          7. 输出结果`possible_key`：
             1. 显示**可能应用在这张表上的索引**，一个或多个
          8. 输出结果`key`：
             1. **实际使用的索引**，如果为Null，则没有使用索引，有则显示索引值/名。
          9. 输出结果`Key_len`：
             1. 使用到索引的字节数，该值为索引字段最大可能长度，并非实际使用长度，在不损失精确性的前提下，长度越短越好。
          10. 输出结果`rows`：
              1. MySQL认为必须要执行查询的行数，在innodb引擎的表中，是一个估计值，可能并不总是准确的。
          11. 输出结果`filtered`：
              1. 表示返回结果的行数占需读取行数的百分比，filtered的值越大越好。
          12. 输出结果`ref`：
              1. 非唯一索引
          13. 输出结果`Extra`：
              1. 输出结果中没有显示的内容将在extra中显示。

    7. 索引的使用

       1. **验证索引效率**

          1. 在未建立索引之前，执行如下SQL语句，查看SQL的耗时
             1. `select * from tb_sku where sn='100001';`
          2. 针对字段创建索引（针对索引创建B+tree结构，会有耗时）
             1. `create index idx_sku_sn on tb_sku(sn);`
          3. 然后再次执行相同的SQL语句， 再次查看SQL的耗时

       2. **最左前缀法则 Leftmost Prefix**

          1. 如果索引了多列（联合索引），要遵守最左前缀法则。

          2. **最左前缀法则**：指的是查询从索引的最左列开始，并且不跳过索引中的列。

          3. 如果跳过某一列，索引将部分是小（后面的字段索引失效）。

          4. ```sql
             #案例，索引为profession+age+status -> idx_user_pro_age_sta （设置索引的时候有一定顺序）
             explain select * from tb_user where profession = "软件工程" and age =31 and status ='0'; #走索引
             explain select * from tb_user where profession = "软件工程" and age =31; #走索引
             explain select * from tb_user where profession = "软件工程"; #走索引
             explain select * from tb_user where profession = "软件工程" and status='0'; #走索引但是索引值key_len与上一条一样，因为中间跳过一列，后面索引失效
             explain select * from tb_user where age =31 and status ='0'; #不走索引，缺失最左
             explain select * from tb_user where status ='0';#不走索引，缺失最左
             ```

       3. 范围查询

          1. 联合索引中，出现范围查询，范围查询右侧的索引失效。

          2. ```sql
             #案例
             #走索引，但是age使用取值范围，则status索引值失效，索引值为52
             explain select * from tb_user where profession = "软件工程" and age>30 and status ='0'; 
             #规避范围索引失效，尽量使用'>='带有等号的，索引值为54
             explain select * from tb_user where profession = "软件工程" and age>=30 and status ='0'; 
             ```

       4. 索引列运算

          1. 不要再索引列上进行运算操作，索引将失效。

          2. ```sql
             #搜索尾号为15的用户，使用字符串查询函数时，可以查询出结果，但是索引失效
             explain select * from tb_user where substring(phone,10,2) ='15';
             ```

       5. 字符串不加引号

          1. 字符串类型字段使用时，不加引号，索引将失效（即使个别情况下可查询到结果）。

       6. 模糊查询

          1. 如果仅仅是尾部模糊匹配，索引不会失效。如果是头部模糊匹配，索引失效。

          2. ```sql
             explain select * from tb_user where profession like '工程%'; #索引有效
             explain select * from tb_user where profession like '%工程'; #索引无效
             ```

       7. or连接条件

          1. 用or分割开的条件，如果or前的条件中的列有索引，而后面的列中没有索引，那么设计的索引都不会被用到。

          2. ```sql
             #age没有索引 下面的都不会有索引， 若有需要，给age页增加索引
             explain select * from tb_user where id=10 or age=23;
             explain select * from tb_user where phone='123123' or age =23;
             ```

       8. 数据分布影响

          1. 如果mysql评估使用索引比全表慢，则不适用索引。
          2. 比如当搜索的内容大部分都是这个值或者大于这个值，则全表搜索。
          3. 当大部分数据不为null的时候，搜索数据`select .. where po is null`走索引。

       9. SQL提示

          1. 优化数据库的一个重要手段：在SQL语句中加入一些认为的提示来达到优化操作的目的。比如一个字段多个索引(自身索引以及和其他字段联合索引)。
          2. `use index`：`explain select * from tb_user user index(idx_user_pro) where profession='软件工程';` 是给Mysql的**建议使用，**mysql会进行评估选择。
          3. `ignore index`：`explain select * from tb_user ignore index(idx_user_pro) where profession='软件工程';` 忽略该索引。
          4. `force index`：`explain select * from tb_user force index(idx_user_pro) where profession='软件工程';` 强制让mysql使用该索引。

       10. **覆盖索引**

           1. 尽量使用覆盖索引（查询使用了索引，并且需要返回的列，在该索引中已经全部能够找到），减少`select *`。
           2. explain在最后一列`Extra`显示的：
              1. `using index condition`：查找使用了索引，但是需要回表查询数据。性能低。[案例图](https://github.com/brant8/mypython/blob/master/pics/mysql_fugai2.png)
                 1. 比如：`explain select id,profession,age,status,name from tb_user where profession='软件工程' and age=31 and status='0';`
                 2. 其中id主键/聚集索引，profession、age、status二级索引，但是name没有索引，因此二级索引中找不到只能到一级索引找name，需要回表查询。 
              2. `using where; using index`：查找使用了索引，但是需要的数据都在索引列中能找到，所以不需要回表查询数据。性能高。[案例图](https://github.com/brant8/mypython/blob/master/pics/mysql_fugai1.png)
                 1. 比如：`explain select id,profession,age,status from tb_user where profession='软件工程' and age=31 and status='0';`
                 2. 其中id主键/聚集索引，profession、age、status二级索引，且在二级索引中包含id非叶子节点，可直接返回。

       11. 前缀索引

           1.  当字段类型为字符型（varchar，text等）时，有时候需要索引很长的字符串，这会让索引变得很大，查询时，浪费大量的磁盘IO，影响查询效率。此时可以将字符串的一部分前缀，建立索引，这样可以大大节约索引空间，从而提高索引效率。

           2. 语法：`create index idx_xxxx on table_name(column(n));`

           3. 前缀长度：可以根据索引的选择性来决定，而选择性是指不重复的索引值（基数）和数据表的记录总数的比值，索引选择性越高查询效率越高，唯一索引的选择性是1，这是最好的索引选择性，性能也是最好的。[流程图](https://github.com/brant8/mypython/blob/master/pics/mysql_prefix1.png)

           4. ```sql
              select count(distinct email) from tb_user; # Email去重后的数量
              select count(distinct email)/count(*) from tb_user; # 使用完整email（去重后）的完整性
              select count(distinct substring(email,1,5))/count(*) from tb_user; # 选取email的前5个字符（去重）后的选择性
              #对email取5个字符作为前缀的索引
              create index idx_email_5 on tb_user(email(5));
              ```

       12. 单列索引与联合索引

           1. 单列索引：即一个索引只包含单个列。若查询结果要求多个字段，则必定会回表查询。
           2. 联合索引：即一个索引包含了多个列。若查询结果要求的多个字段联合索引都具备，使用的是覆盖索引。直接返回查询结果。创建联合索引的时候需要考虑索引创建顺序。![图说明](https://github.com/brant8/mypython/blob/master/pics/mysql_joint.png)

       13. 索引设计原则

           1. 针对数据量较大，且查询比较频繁的表建立索引。数据量百万条以上。
           2. 针对于常作为查询条件（where）、排序（order by）、分组（group by）操作的字段建立索引。
           3. 尽量选择区分度高（用户名等）的列作为索引，尽量建立唯一索引，区分度越高，使用索引的效率越高。
           4. 如果是字符串类型的字段，字段的长度较长，可以针对字段的特点，建立前缀索引。
           5. 尽量使用联合索引，减少单列索引，查询时，联合索引很多时候可以覆盖索引，节省存储空间，避免回表，提高调查效率。
           6. 要控制索引的数量，索引并不是多多益善，索引越多，维护索引结构的代价也就越大，会影响增删改的效率。
           7. 如果索引列不能存储NULL值，请在创建表时使用NOT NULL约束它。当优化器直到每列是否包含NULL值时，它可以更好地确定哪个索引最有效的用于查询。

17. ### SQL优化

    1. 插入数据

       1. **insert优化**：

          1. 批量插入，如`insert into tb_test values(1,'Tom'),(2,'Cat'),(3,'Jerry');`

          2. 手动提交事务

             ```sql
             start transaction;
             insert into tb_test values(1,'Tom'),(2,'Cat'),(3,'Jerry');
             insert into tb_test values(4,'Tom'),(5,'Cat'),(6,'Jerry');
             insert into tb_test values(7,'Tom'),(8,'Cat'),(9,'Jerry');
             commit;
             ```

          3. 主键顺序插入

             1. 主键乱序插入 ：如 8，1，85，8，...
             2. 主键顺序插入(效率高)：如1，2， 3，4，...

          4. 大批量插入数据

             1. 如果需要一次性插入大批量数据，使用insert性能低，此时可以使用MySQL数据库提供的load指令进行插入。

             2. 格式：每个数据字段用符号分隔（有规律的），每行独占一条数据

                ```sql
                #客户端连接服务端时，加上参数 --local-infile 表示加载本地文件
                root> mysql --local-infile -u root -p
                #设置全局参数local_infile为1，开启从本地加载文件导入数据的开关 查看开关状态 'select @@local_infile;'
                mysql> set global local_infile = 1;
                #执行load指令将准备好的数据，加载到创建好的 表结构中
                mysql> load data local infile 'root/sql1.log' into table 'tb_user' fields terminated by ',' lines terminated by '\n';
                ```

             3. Linux命令：`wc -l xxx.sql` 查看文件中有多少行。

          5. 逐渐优化：

             1. 在InnoDB存储引擎中，表数据都是根据主键顺序阻止存放的，这种存储方式的表成为索引组织表 index organized table IOT。
             2. 页分裂：也可以为空，可以填充一半，也可以100%。每个页包含了2 ~ N行数据（如果一行数据多大，会行溢出），根据主键排列。
             3. 页合并：
                1. 当删除一行记录时，实际上记录并没有被物理删除，只是记录被标记 flaged 为删除并且它的空间变得允许被其他记录声明使用。
                2. 当页中删除的记录达到merge_threshold（默认为页的50%），InnoDB会开始寻找最靠近的页（前或后）看看是否可以将两个页合并以优化空间使用。
                3. 合并页的阈(yu)值 merge_threshold ：可以自己设置，在创建表或者创建索引时指定。

       2. **主键优化 / 聚集索引**

          1. 满足业务需求的情况下，尽量降低主键的长度。
          2. 插入数据时，尽量选择顺序插入，选择使用auto_increment自增主键。
          3. 尽量不要使用UUID做逐渐或者时其他自然主键，如身份证号。
          4. 业务操作时，避免对主键的修改。

       3. **oder by 优化**

          1. `Using filesort`：通过表的索引或全表扫描，读取满足条件的数据行，然后再排序缓冲区`sort buffer`中完成排序操作，所有不是通过索引直接返回排序结果的排序都叫做`FileSort`排序。
          2. `Using index`：通过有序索引顺序扫描直接返回有序数据，这种情况即为`using index`，不需要额外排序，操作效率高。
             1. 通过对其创建对应的字段（联合）索引，查询时效率高，自动使用using index。
             2. 创建索引时可直接按照需求直接排序：`create index idx_user_age_pho on tab_user(age asc, phone desc);` 
          3. 创建索引时需要注意使用**覆盖索引**，即查询的字段需要匹配索引的字段。
          4. Explain中出现的`Collation`中的值A表示升序，D表示降序。
          5. 多字段是，需要遵循最左前缀法则。
          6. 如果不可避免的出现filesort，大数据量排序时，可以适当增大排序缓冲区大小。`sort buffer_size`默认256K。

       4. **group by优化**

          1. ```sql
             #删除掉目前的联合索引idx_user_pro_age_sta
             drop index idx_user_pro_age_sta on tb_user;
             #执行分组操作，根据profession字段分组
             explain select profession,count(*) from tb_user group by profession;
             #创建索引
             create index idx_user_pro_age_sta on tb_user(profession,age,status);
             #执行分组操作，根据profession字段分组
             explain select profession,count(*) from tb_user group by profession;
             #执行分组操作，根据profession字段分组
             explain select profession,count(*) from tb_user group by profession,age;
             ```

          2. 当联合索引中使用where条件和group by时，只要两个语句中包含联合索引键，则满足最左法则。

       5. **limit优化**

          1. 当分页查询`limit(2000000,10)`时，查询当中的10条记录，其他的丢弃，查询排序的代价非常大。

          2. ```sql
             #耗时19秒
             select * from tb_sku order by id limit 900000,10;
             #覆盖索引方式优化 limit
             select id from tb_sku order by id limit 900000,10;
             #同张表使用多表联查方式，耗时11秒
             select s.* from tb_sku s, (select id from tb_sku order by id limit 900000,10) a where s.id=a.id;
             ```

          3. 一般分页查询时，通过创建覆盖索引能够比较好的提高性能，可以通过覆盖索引加子查询形式进行优化。

       6. **count优化**

          1. MyISAM引擎把一个表的总行数存在了磁盘上（没有where条件），因此执行count(*)的时候会直接返回这个数，效率很高。
          2. InnoDB引擎就麻烦了，它执行count(*)的时候，需要把数据一行一行的从引擎读出来，然后累积计数。
          3. 优化思路：自己计数，比如使用Redis。
          4. `count()`时一个聚合函数，对于返回的结果集，一行行的判断，如果count函数的参数不是NULL，累计值就加1，否则不加，最后返回累计值。
          5. 用法及性能：`count(*)` > `count(1)` > `count(主键)` > `count(字段)`
          6. `count()`：InnoDB引擎会遍历整张表，把每一行的主键id值都取出来，返回给服务层。服务层难道主键后，直接按行进行累加（主键不可能为null）。
          7. `count(字段)`：
             1. 没有`not null`约束：InnoDB引擎会遍历整张表把每一行的字段值都取出来，返回给服务层，服务层判断是否为null，不为null，技术累加。
             2. 有`not null`约束：innodb引擎会遍历整张表把每一行的字段都取出来，返回给服务层，直接按行进行累加。
          8. `count(1)`：Innodb引擎会遍历整张表，但不取值。服务层对于返回的每一行，放一个数字`1`进去，直接按行进行累加。
          9. `count(1)`：innodb引擎不会把全部字段取出来，而是专门做了优化，不取值，服务层直接按行进行累加。

       7. **update优化**

          1. ```sql
             #事务1
             begin;
             update student set no='20012' where id = 1;
             commit;
             #事务2 可以成功，主键可以。 原因：InnoDB是行锁
             begin;
             update student set no='20013' where id = 12;
             commit;
             #事务3，name没有索引。
             begin;
             update student set no='20012' where name = '李四';
             commit;
             #事务4，当其他事务更新时，条件判断非索引，则行锁升级为表锁。更新失败
             begin;
             update student set no='20015' where name = '张三';
             commit;
             ```

          2. InnoDB的**行锁是针对索引加的锁**，不是针对记录加的锁，并且该索引不能失效，否则会从行锁升级为表锁。

18. ### 视图

    1. 视图 View 是一种虚拟存在的表。视图中的数据并不在数据库中实际存在，行和列数据来自定义视图的查询中使用的表，并且是再使用视图使动态生成的。

    2. 视图只保存了查询的SQL逻辑，不保存查询结果。在创建视图的时候，主要工作落在创建SQL查询语句上。

    3. ```sql
       #创建 
       # create [or replace] view 视图名称[(列名列表)] as select语句 [with [cascaded | local] check option]
       create or replace view stu_v_1 as select id,name from student where id <=10;
       create or replace view stu_v_1 as select id,name from student where id <=10 with cascaded check option; #插入数据时自动检查数据是否符合视图条件范围
       #查询
       #查看创建视图语句：show create view 视图名称;
       #查看视图数据：select * from 视图名称...;
       show create view stu_v_1;
       select * from stu_v_1;
       #修改
       #方式一：create [or replace] view 视图名称[(列名列表)] as select语句 [with [cascaded | local] check option]
       #方式二：alter view 视图名称[(列名列表)] as select语句 [with [cascaded | local] check option]
       create or replace view stu_v_1 as select id,name,no from student where id<=10; #(指定视图输出id小于10的，大于10的时候select不会输出)
       alter view stu_v1_1 as select id,name from student where id<=10;
       #删除
       #drop view [if exists] 视图名称 [,视图名称]...
       drop view if exists stu_v_1;
       #插入数据到视图实际是到数据表
       insert into stu_v_1 values(6,'Tom');
       ```

    4. 视图检查选项

       1. 当使用`with [local | cascaded] check option`句子创建视图时，Mysql会通过视图检查正在更改的每个行，例如插入，更新，删除，以使其符合视图的定义。
       2. MySQL允许基于另一个视图创建视图，它还会检查以来试图中的规则以保持一致性。为了确定检查的范围，mysql提供了两个选项：CASCADED和LOCAL，默认cascaded。
       3. cascaded和local区别：cascaded会将check option向上传递检查（即使父视图没有检查选项），local递归的找上一个视图的条件现象，若父视图没有检查，则插入更新等操作只限制在本视图。

    5. 视图的更新

       1. 要使视图可更新，视图中的行与基础表中的行之间必须存在一对一关系。
       2. 如果视图包含以下任何一下，则该视图不可更新：
          1. 聚合函数或窗口函数`sum()`、`min()`、`max()`、`count()`等
          2. `distinct`
          3. `group by`
          4. `having`
          5. `union`或者`union all`等其他

    6. 视图的作用

       1. 简单：视图不仅可以简化用户对数据的理解，也可以简化操作。哪些经常使用的查询可以被定义为视图，从而使得用户不必为以后的操作每次指定全部的条件。
       2. 安全：数据库可以授权，但不能授权到数据库特定行和特定的列上。通过视图用户只能查询和修改他们所能见到的数据。
       3. 数据独立：视图可以帮助用户屏蔽真实表结构变化带来的影响。

    7. 案例：

       1. 为了保证数据库表的安全性，开发人员在操作tb_user表使，只能看到的用户的基本字段，屏蔽手机号和邮箱两个字段。
       2. 查询每个学生锁选秀的课程（三张表联查），这个功能在很多的业务中都有使用到，为了简化操作，定义一个视图。

19. ### 存储过程 procedure

    1. 介绍

       1. 存储过程是事先经过编译并存储在数据库中的一段SQL语句的集合，调用存储过程可以简化应用开发人员的很多工作，减少数据在数据库和应用之间的传输，对于提高数据处理的效率是有好处的。
       2. 存储过程思想上很简答， 就是数据库SQL语言层面的代码封装与重用。

    2. 特点：

       1. 封装，重用
       2. 可以接收参数，也可以返回数据
       3. 减少网络交互，效率提升

    3. 创建：

       ```sql
       create procedure 存储过程名字([参数列表])
       begin
       	-- SQL语句
       end;	
       ```

    4. 调用：`call 名称([参数]);`  （需要括号，即使无参）

    5. 查看：

       ```sql
       #查询指定数据库的存储过程及状态信息
       select * from information_schema.routines where routine_schema = 'xxx';
       #查询某个存储过程的定义
       show create procedure 存储过程名称;  #不需要括号
       ```

    6. 删除：`drop procedure [if exists] 存储过程名称;`  

    7. 注意：在命令行中，执行创建存储过程的SQL时，需要通过关键字delimiter指定SQL语句的结束符。**命令行中分号`;`默认为SQL结束符号**。

       1. `delimiter $$`

       2. ```sql
          mysql> delimiter $$	#操作完后再改回去
          mysql> create procedure p1()
          	-> begin
          	-> 		select count(*) from student;
          	-> end$$
          #以$$结尾，否则在student;后sql认为语句已经执行完毕。
          ```

    8. 变量

       1. **系统变量**：是MySQL服务器提供，不是用户定义的，属于服务器层面。分为全局变量Global、会话变量Session（当前sql窗口）。

          1. 查看系统变量	

          ```sql
          show [session | global] variables; #查看所有系统变量
          show [session | global] variables like '......'; #可以通过like模糊匹配方式查找变量 如'auto&'
          select @@[session | global] 系统变量名; #查看指定变量的值
          ```

          1. 设置系统变量

          ```sql
          set [session | global] 系统变量名 = 值;
          set @@[session | global] 系统变量名 = 值;
          ```

          1. 如果没有指定session/global，默认是session，会话变量。
          2. mysql服务重启之后，所设置的全局参数会失效，想要不失效，可以再`/etc/my.cnf`中配置。

       2. **用户自定义变量**：用`@变量名`使用即可

          1. 赋值

             ```sql
             set @var_name=expr[,@var_name = expr]...; #多个变量赋值
             set @var_name:=expr[,@var_name:=expr]...;
             select @var_name:=expr[,@var_name:=expr]...; #使用select多个变量赋值
             select 字段名 into @var_name from 表名; #可以使用函数字段如count(*)
             ```

          2. 使用：`select @var_name;`

          3. 注意：用户定义的变量无需对齐进行声明或初始化，只不过获取到的值为NULL。

       3. **局部变量**：需要定义在局部生效的变量，需要`declare`声明。可用作存储过程内的局部变量和输入参数，局部变量的范围是在其内声明`begin..end`块。

          1. 声明：`declare 变量名 变量类型 [default ...];`

          2. 变量类型就是数字库字段类型：int、bigint、char、varchar、date、time等。

          3. 赋值

             ```sql
             set 变量名 = 值;
             set 变量名 := 值;
             select 字段名 into 变量名 from 表名...;
             #比如
             create procedure p2()
             begin
             	declare stu_count int default 0; #局部变量在begin...end块中间有效
             	select count(*) into stu_count from student;
             	select stu_count;
             end;	
             ```

    9. **if**

       1. ```sql
          if 条件1 then
          	...
          elseif 条件2 then
          	...
          else
          	...
          end if;	
          ```

    10. **存储类型参数**

        1. | 类型  | 含义                                          | 备注 |
           | ----- | --------------------------------------------- | ---- |
           | in    | 该类参数作为输入，也就是需要调用时传入值      | 默认 |
           | out   | 该类参数作为输出，也就是gai参数可以作为返回值 |      |
           | inout | 既可以作为输入参数，也可以作为输出参数        |      |

        2. 用法：

           ```sql
           create procedure 存储过程名称([in/out/inout 参数名 参数类型])
           begin
           	-- sql语句
           end;	
           #调用的时候
           #比如： call(68, @result); 
           #其中 @result 为输出变量 属于用户自定义变量
           ```

    11. **case**

        1. ```sql
           #语法一
           case case_value
           	when when_value1 then statement_list1
           	[when when_value2 then statement_list2]...
           	[else statement_list]
           end case;	
           #语法二
           case 
           	when search_condition1 then statement_list1
           	[when search_condition2 then statement_list2]...
           	[else statement_list]
           end case;
           ```

    12. **while**

        1. ```sql
           #先判定条件，如果条件为true，则执行逻辑，否则，不执行逻辑
           while 条件 do
           	sql逻辑...
           end while;	
           #例子
           create procedure p1(in n int)
           begin
           	declare total int default 0;
           	while n>0 do
           		set total := total + n;
           		set n := n-1;
           	end while;
           	select total;
           end;
           call p1(5);
           ```

    13. **repeat**

        1. ```sql
           #先执行一次逻辑，然后判定逻辑是否满足，如果满足，则退出。如果不满足，则继续下一次循环
           repeat
           	SQL逻辑..
           	until 条件
           end repeat;	
           ```

    14. **loop死循环**

        1. 如果不在SQL逻辑中增加退出循环的条件，可以用其来实现简单的死循环。

        2. Loop配合使用：

           1. `leave`：配合循环使用，退出循环
           2. `iterate`：必须用在循环中，作用时跳过当前循环剩下的语句，直接进入下一次循环。

        3. ```sql
           [begin_label:] loop
           	SQL逻辑...（比如退出 leave begin_label;）
           end loop [end_label];    
           ```

    15. **游标 Cursor**

        1. 用来存储查询结果集的数据类型，在存储过程和函数中使用游标对结果集进行循环处理。

        2. 游标的使用包括游标的声明、open、fetch和close。

        3. ```sql
           #声明游标
           declare 游标名称 cursor for 查询语句; #把查询的结果集存到游标当中
           #打开游标
           open 游标名称：
           #获取游标记录
           fetch 游标名称 into 变量[,变量]; #把对应结果集字段名分别赋给变量，后面可再加insert赋值给别的表
           #关闭游标
           close 游标名称;
           ```

        4. 案例：根据传入的参数usage，查询表tb_user中，所有用户年龄小于等于usage的用户name和专业profession，并将用户的姓名和专业插入到所创建的一张新表(id, name, profession)中，通过循环把游标结果集快速赋值。注意：变量声明需要在游标声明之前，否则报错。

    16. **条件处理程序 Handler**

        1. 可以用来定义再流程控制结构执行过程中遇到问题时对应的处理步骤。

        2. ```sql
           declare handler_action handler for condition_value [,condition_value]... statement;
           #比如循环游标有错误代码（无限循环没有正常关闭），出现错误码自动关闭游标
           #declare exit handler for SQLSTATE '02000' close u_cursor;
           
           handler_action
           	continue：继续执行当前程序
           	exit:终止执行当前程序
           condition_value
           	SQLSTATE sqlstate_value：状态码，如02000
           	SQLWARNING：所有以01开头的SQLSATE代码的简写
           	NOT FOUND：所有以02开头的SQLSTATE代码的简写
           	SQLEXCEPTION：所有没有被SQLWARNING或NOT FOUND捕获的SQLSTATE代码的简写
           	
           ```

20. ### 存储函数 function

    1. 存储函数是有返回值的存储过程，存储函数的参数只能是IN类型。**与存储过程类似**，但必须要有返回值。

    2. ```sql
       create function 存储函数名称([参数列表])
       returns type [characteristic...]
       begin
       	--sql语句
       	return ...;
       end;
       
       characteristic说明：
       	deterministic：相同的输入参数总是产生相同的结果
       	no sql：不包含sql语句。
       	reads sql data：包含读取数据的语句，但不包含写入数据的语句。
       ```

21. ### 触发器 trigger

    1. 触发器是与表有关的数据对象，指在insert、update、delete之前或之后，触发并执行触发器中定义的SQL语句。

    2. 触发器的这种特性可以协助应用在数据库端确保数据行的完整性，日志记录，数据校验等操作。

    3. 使用别名OLD和NEW来引用触发器中发生变化的记录内容，这与其他的数据库是相似的。现在触发器还支持吃触发级，不支持语句级触发。

    4. | 触发器类型     | NEW和OLD                                             |
       | -------------- | ---------------------------------------------------- |
       | insert型触发器 | new表示要将或者已经新增的数据                        |
       | update型触发器 | old表示修改之前的数据，new表示将要或已经修改后的数据 |
       | delete型触发器 | old表示将要或者已经删除的数据                        |

    5. ```sql
       #创建
       create tigger tigeger_name
       beofore/after insert/update/delete
       on table_name for each row --行级触发器
       begin 
       	trigger_stmt 
       	#比如下面的，更新表格inser后触发记录变更操作到日志表中。new.xxx和old.xxx表示新旧数据
       	insert into user_log(id,operation,operation_time,operate_id,operate_params) values
       	(null,'insert',now,new.id,contact('插入的数据内容为： id=',new.id,',name=',new.name));
       end;
       #查看
       show triggers;
       #删除
       drop trigger [schema_name.]trigger_name; --如果没有指定schema_name，默认为当前数据库
       ```

    6. 案例：通过触发器记录tb_user表的数据变更日志，将变更日志插入到日志表user_log中。

22. ### 锁

    1. 锁是计算机协调多个进行或线程并发访问某一资源的机制。

    2. 数据库中，除传统的计算资源（CPU、RAM、I/O）的争用以外，数据也是一种供许多用户共享的资源。

    3. MySQL中的锁：

       1. 全局锁：锁定数据库中的所有表。[示例图](https://github.com/brant8/mypython/blob/master/pics/mysql_full_lock.png)
       2. 表级锁：每次操作所著整张表。
       3. 行级锁：每次操作锁住对应的行数据。

    4. **全局锁**

       1. 特点1：如果在主库上备份，那么在备份期间都不能执行更新，业务基本上就得停摆。
       2. 特点2：如果在从库上备份，那么在备份期间从库不能执行主库同步过来的二进制日志binlog，会导致主从延迟。
       3. 在InnoDB引擎中，我们可以在备份时加上参数`--single-transaction`参数来完成不加锁的一致性数据备份`mysqldump`。

    5. **表级锁**

       1. 每次操作所住整张表。锁定粒度大，发生锁冲突的概率最高，并发度最低。应用在MyISAM、InnoDB、BDB等存储库中。

       2. 表级锁，分为三类

          1. **表锁**：

             1. 表共享读锁 read lock：[示例图](https://github.com/brant8/mypython/blob/master/pics/mysql_readlock.png) 不会阻塞其他客户端的读，但是会阻塞写。

             2. 表独占写锁 write lock：[示例图](https://github.com/brant8/mypython/blob/master/pics/mysql_writelock.png) 自身可读写，会阻塞其他客户端的读/写。

                ```sql
                加锁：lock tables 表名... read/write
                释放锁：unlock tables / 客户端断开连接
                ```

          2. **元数据锁 meta data lock**：

             1. MDL加锁过程是系统自动控制，无需显示使用，在访问一张表的时候会自动加上。

             2. MDL锁主要作用是维护表元数据的数据一致性，在表上有活动事务的时候（未完成的事务），不可以对元数据进行写入操作。为了避免DML与DDL冲突，保证读写的正确性。

             3. 在MySQL5.5中引入MDL，当对一张表进行增删改查的时候，加MDL读锁（共享）；当对表结构进行变更操作的时候，加MDL写锁（排他）。

             4. | 对应SQL                                       | 锁类型                                 | 说明                                             |
                | --------------------------------------------- | -------------------------------------- | ------------------------------------------------ |
                | lock table xxx read/write                     | share_read_only / shared_no_read_write |                                                  |
                | select、select...lock in share mode           | shared_read(读锁)                      | 与shared_read、shared_write兼容，与exclusive互斥 |
                | insert、update、delete、select ... for update | shared_write(写锁)                     | 与shared_read、shared_write兼容，与exclusive互斥 |
                | alter table...                                | exclusive(排他)                        | 与其他的MDL都互斥                                |

             5. 查看元数据锁

                ```sql
                select object_type, object_schema, object_name, lock_type,lock_duration from performance_schema.metadata_locks;
                ```

          3. **意向锁**：

             1. 为了避免DML在执行时，加的行锁与表锁的冲突，在InnoDB中引入了意向锁，是的表锁不用检查每行数据是否加锁，使用意向锁来减少表锁的检查。[图](https://github.com/brant8/mypython/blob/master/pics/mysql_yixianglock.png)

             2. ```sql
                #意向共享锁 IS：
                	由语句 select...lock in share mode 添加
                #意向排他锁 IX：
                	由 insert、update、delete、select...for update 添加。
                #查看意向锁及行锁的加锁情况
                select object_schema, object_name, index_name, lock_type, lock_mode, lock_data from performance_schema.data_locks;
                ```

          4. **行级锁**

             1. 行级锁，每次操作锁对应的行数据。

             2. 锁定粒度最小，发生锁冲突的概率最低，并发读最高。应用在InnoDB存储引擎中。

             3. Innodb的数据是基于索引组织的，行锁是通过对索引上的索引项加锁来实现的，而不是对记录加的锁。

             4. 对于行级锁，主要分三类：

                1. 行锁 Record Lock：锁定单个行记录的锁，放置其他事务对此进行update和delete。在RC、RR隔离级别下都支持。
                2. 间隙锁 Gap Lock：锁定索引记录间隙（不含该记录），确保索引记录间隙不变，放置其他事务在这个间隙进行insert，产生幻读。在RR隔离级别下都支持。
                3. 临键锁 Next-key Lock：行锁和间隙锁组合，同时锁住数据，并所著数据前面的间隙Gap。在RR隔离级别下支持。

             5. InnoDB实现了以下两种行锁

                1. 共享锁 S：允许一个事务去读一行，阻止其他事务获得相同数据集的排他锁。

                2. 排他锁 X：允许获取其他锁的事务更新数据，阻止其他事务获取相同数据集的共享锁和排他锁。

                3. | 当前锁类型 \ 请求锁类型 | S 共享锁 | X 排他锁 |
                   | ----------------------- | -------- | -------- |
                   | S 共享锁                | 兼容     | 冲突     |
                   | X 排它锁                | 冲突     | 冲突     |

                4. 行锁

                   | SQL                           | 行锁类型   | 说明                                     |
                   | ----------------------------- | ---------- | ---------------------------------------- |
                   | insert                        | 排他锁     | 自动加锁                                 |
                   | update                        | 排他锁     | 自动加锁                                 |
                   | delete                        | 排它锁     | 自动加锁                                 |
                   | select (正常)                 | 不加任何锁 |                                          |
                   | select ... lock in share mode | 共享锁     | 需要手动在select之后加lock in share mode |
                   | select ... for update         | 排他锁     | 需要手动在select之后加for update         |

             6. 默认情况下，InnoDB在Repeatable Read事务隔离级别运行，在InnoDB使用next-key锁进行搜索和索引扫描，以防止幻读。

                1. 针对唯一索引进行检索时，对已存在的记录进行等值匹配时，将会自动**优化为行锁**。
                2. InnoDB的行锁时针对于索引加的锁，不通过索引条件检索数据，那么InnoDB将对表中的所有记录加锁，此时就会**升级为表锁**。
                3. 索引上的等值查询（唯一索引），给不存在的记录加锁时，优化为间隙锁。
                4. 索引上的等值查询（普通索引），向右遍历时最后一个值不满足查询需求时，next-key lock退化为间隙锁。
                5. 索引上的范围查询（唯一索引）--会访问到不满足条件的第一个值为止。
                6. *注意：间隙锁唯一的目的时防止其他事务插入间隙。间隙锁可以共存，一个事务采用的间隙锁不会阻止另一个事务在同一间隙上采用间隙锁*。

             7. 
































