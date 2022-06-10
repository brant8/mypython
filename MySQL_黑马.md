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

   5. DDL 数据库操作( `[..]`可选 )：

      1. 查询：查询所有数据库 `show databases;`  查询当前数据库 `select database();`
      2. 创建：`create database [if not exists] 数据库名 [default charset 字符集] [collate 排序规则];`
      3. 删除：`drop database [if exists] 数据库名;`
      4. 使用：`use 数据库名;`

   6. DDL 表操作 查询：

      1. 查询当前数据库所有表：`show tables;`
      2. 查询表结构：`desc 表名;`
      3. 查询指定表的建表语句：`show create table 表名;`

   7. DDL 表操作 创建：

      ```sql
      create table 表名(
      	字段1 字段1类型[comment 字段1注释],
          字段2 字段2类型[comment 字段2注释], #如 name varchar(50) comment '姓名',
          ...
      )[comment 表注释];
      ```

   8. DDL 表操作 数据类型：数值类型、字符串类型、日期时间类型。

      1. 



