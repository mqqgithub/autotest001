try:
    a = input("输入一个数：")
    if(not a.isdigit()):
        raise Exception("a 必须是数字")
except Exception as e:
    print("引发异常1：", e)