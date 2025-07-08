import asyncio

#不确定参数
def my_function(*kids):
    print("最小的孩子是 " + kids[2])

#关键字参数  接收任意数目的“键=值”形式的参数
def my_function(**kid):
    print("他的姓是 " + kid["lname"])

#默认参数
def show_country(country="Nuowei"):
    print("我来自 " + country)

#仅限位置参数( / )
def my_func(x, /):
    print(x)
my_func(3)       # OK
#my_func(x=3)     # 错误, x只能作为位置参数

#仅限关键字参数( * )
def my_func(*, x):
    print(x)
my_func(x=3)     # OK
#my_func(3)       # 错误, x只能作为关键字

#混合使用
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
my_function(5, 6, c=7, d=8)  # a,b只能用位置传，c,d只能用关键字

#lambda 格式
#lambda 参数列表 : 表达式
x = lambda a,b: a + b + 10  #参数为a，表达式为a + b + 10
print(x(5,1))



def exception_test():
    #异常捕获
    try:
        f = open("demo.txt", "w")
        f.write("写入内容")
    except FileNotFoundError as e:
        print(f"写入文件出错:{e}")
    else:
        print("代码正常运行，没有异常")
    finally:
        f.close()
        print("文件关闭了")

    #抛出异常
    x = "hello"
    if not isinstance(x, int):
        raise TypeError("只允许输入整数类型的数据")


#异步函数  Python3.7
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def multi_count():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    asyncio.run(multi_count())
    asyncio.run(count())