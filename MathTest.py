import math

def math_test():
    x = min(5, 10, 25)
    y = max(5, 10, 25)
    print(x)  # 输出: 5
    print(y)  # 输出: 25

    x = abs(-7.25)
    print(x)  # 输出: 7.25

    #4的3次方
    x = pow(4, 3)
    print(x)  # 输出: 64

    #平方根
    x = math.sqrt(64)
    print(x)  # 输出: 8.0


    x = math.ceil(1.4)  # 向上取整，输出 2
    y = math.floor(1.4)  # 向下取整，输出 1
    print(x)
    print(y)

    #pi
    x = math.pi
    print(x)  # 输出: 3.141592653589793

if __name__ == '__main__':
    math_test()