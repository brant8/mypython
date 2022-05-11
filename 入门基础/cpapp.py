def display1():
    print('请选择功能----')
    print('1 添加')
    print('2 删除')
    print('3 查询')
    print('4 修改')
    print('5 修改显示所有学员')
    print('6 退出系统')
    print('-' * 20)
info = []

def add_info():
    """添加学院"""
    new_id = int(input("输入学号"))
    new_name = input("输入名字")
    new_tel = int(input("输入手机号"))
    global info
    for i in info:
        if new_name == i['name']:
            print('数据已存在')
            return                      #退出当前函数 并且后续添加学生不再执行
    info_dict = {}
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['tel']=new_tel
    info.append(info_dict)

def del_info():
    """删除学员"""
    del_name = input('要删除的学员：')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break   # 删除完后即可退出for循环
    else:
        print("该学员不存在")
    print(info)
def modify_info():
    """修改函数"""
    modify_name=input("要修改的学员电话")
    global info
    for i in info:
        if modify_name == i['name']:
            j = input("输入要更改电话的学员")
            i['tel']=j  #更改完后终止此循环
            break
    else:
        print("没有此学员")
    print(info)

def select_info():
    select_name=input("查询的用户名： ")
    global info
    for i in info:
        if select_name==i['name']:
            print(f"该学员信息： {i['id']}，姓名是{i['name']}，手机号是{i['tel']}")
            # return
            break
    else:
        print("没有该学员。。")

while True:
    display1()
    user_num = int(input("请输入功能序号： "))
    if user_num == 1:
        add_info()
        print("添加")
    elif user_num == 2:
        del_info()
        print("删除")
    elif user_num == 3:
        select_info()
        print("查询")
    elif user_num == 4:
        modify_info()
        print("修改")
    elif user_num == 5:
        print("显示所有")
        print(info)
    elif user_num == 6:
        print("退出系统")
        break
    else:
        print('输入功能序号有误')