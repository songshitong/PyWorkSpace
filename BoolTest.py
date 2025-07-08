

def bool_test():
    #在Python中，几乎所有非空或非零的值都被评估为True：
    print(bool("nihao"))
    print(bool(123))
    print(bool(["apple", "banana"]))

    #只有少数特定的值会被Python视为False，包括：False  None 数值0  空字符串""  空列表[]  空元组() 空字典{}
    print(bool(False))  # 输出 False
    print(bool(None))  # 输出 False
    print(bool(0))  # 输出 False
    print(bool(""))  # 输出 False
    print(bool([]))  # 输出 False

    #使用 isinstance() 检测类型也返回bool
    x = 200
    print(isinstance(x, int))  # 输出 True
    print(isinstance(x, str))  # 输出 False

if __name__ == '__main__':
    bool_test()