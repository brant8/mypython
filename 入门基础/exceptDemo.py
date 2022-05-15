try:
    print(1/0)
except (NameError,ZeroDivisionError) as result:
    print("分母为0")
    print(result)

# print(1/0)

class ShortInputError(Exception):
    def __str__(self): #设置异常描述信息
        return f'异常信息'
    def __init__(self,length, min_len):
        self.length = length
        self.min_len =min_len
def main():
    try:
        con = input('输入密码： ')
        if len(con) < 3:
            raise ShortInputError(len(con),3)	#抛出自定义异常
            # print('异常哈')
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')

print(__name__)

main()