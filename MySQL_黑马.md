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

    1. 高级下

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

    2. 索引 index 是帮助MySQL高效获取数据的数据结构（**有序**）。在数据之外，数据库系统还维护者满足特定查找算法的数据结构，这些数据结构以某种方式引用（指向）数据，这样就可以在这些数据结构上实现高级查找算法，这种数据结构就是索引。

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
    6. SQL性能分析（主要是查询优化）
       1. SQL执行频率：
          1. MySQL客户端连接成功后，通过`show [session | global] status`命令可以提供服务器状态信息。
          2. global表示全局，session表示当前会话信息。
          3. 通过如下指令，可以查看当前数据库的insert、update、delete、select的访问频次
          4. `show global status like 'Com_______';` 7个下划线。结果输出Variable_name如`Com_insert`。
          5. *通过查询执行频率来决定当前数据库操作方向来进行优化*。





































