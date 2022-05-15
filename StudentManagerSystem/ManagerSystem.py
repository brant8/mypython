import Student
class StudentManagerSystem():
    def __init__(self):
        self.student_list = []
    def run(self): #一般入口函数命名为run
        while True:
            self.show_menu()
            menu_num = int(input("请输入需要的功能： "))
            if menu_num == 1: #添加
                self.add_student()
            elif menu_num ==2:#删除
                self.del_student()
            elif menu_num ==3:#修改
                self.mod_student()
            elif menu_num ==4:#查询
                self.search_student()
            elif menu_num ==5:#显示所有
                self.show_student()
            elif menu_num ==6:#保存
                self.save_student()
            elif menu_num==7:#退出
                break

    @staticmethod
    def show_menu(): #打印功能，没有任何变量
        print("请选择如下功能：")
        print("1：添加学员")
        print("2：删除学员")
        print("3：修改学员")
        print("4：查询学员")
        print("5：显示所有学员")
        print("6：保存学员")
        print("7：退出系统员")

    def add_student(self):
        name = input("请输入姓名：")
        gender = input("请输入性别：")
        tel = input("请输入手机号：")
        student = Student.Students(name,gender,tel)
        self.student_list.append(student)
        # print(self.student_list)

    def del_student(self):
        del_name = input('要删除的学员： ')
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print("查无此人")
        print(self.student_list)
    def mod_student(self):
        stu_name = input("输入要修改学生的姓名")
        for i in self.student_list:
            if i.name == stu_name:
                i.name = input("请输入学员姓名")
                i.gender = input("请输入学员性别")
                i.tel = input("请输入学员电话")
                print(f'{i.name},{i.gender},{i.tel}')
                break
        else:
            print("没有这个人")
    def search_student(self):
        stu_name = input("输入要修改学生的姓名")
        for i in self.student_list:
            if i.name == stu_name:
                print(f'{i.name},{i.gender},{i.tel}')
                break
        else:
            print("没有这个人")
    def show_student(self):
        for i in self.student_list:
            print('姓名\t性别\t电话 ')
            print(f'{i.name}\t{i.gender}\t{i.tel}')
    def save_student(self):
        #1.打开文件
        f = open('student.data','w')
        #2.文件写入数据, 注意：文件写入的数据不能是学员对象的内存地址，需要把学员数据传换成列表字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        #3.文件内数据要求为字符串类型，需要先转换数据类型为字符串类型才能写入数据
        f.write(str(new_list))
        f.close()
    def load_student(self):
        try:
            f = open('student.data','r')
        except:
            f = open('student.data','w')
        else:
            data = f.read()
            # 文件种读取的数据都是字符串且字符串内部为字典数据，古需要转换数据类型，再转换字典为对象后存储到学员列表。
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            f.close()

