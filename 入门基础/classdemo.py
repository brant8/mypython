# class Washer():
#     def wash(self):
#         print("wash machine")
#         print(self)
#     def __init__(self):
#         print(self.width)
#
# #创建对象
# haier = Washer()
#
# print(haier)
# haier.wash()
# haier.height = 500
#
# haier2 = Washer()
# print(haier2)


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


class Furniture():
    def __init__(self,name, area):
        self.name = name
        self.area = area
class Home():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []
    def __str__(self):
        return f'地理位置在{self.address}, 房屋面积时{self.area}，剩余面积{self.free_area}，家具有{self.furniture}'
    def add_funiture(self,item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area = self.free_area - item.area
        else:
            print("没有更多空间了")

bed = Furniture('双人床',6)
chair = Furniture('凳子',996)

bj = Home('北京',1000)
bj.add_funiture(bed)
bj.add_funiture(chair)
print(bj)
