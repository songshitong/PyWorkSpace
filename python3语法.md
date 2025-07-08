
https://www.cnpython.com/python/syntax.html

缩进用于划分代码块，使用的空格数量保持一致，否则会报错
```
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")
```

Python变量的创建是在你为其赋值时自动完成的,不需要类似int x或string y这样先进行声明
```
x = 5
y = "Hello, World!"

命名常见风格：
Camel Case
myVariableName = "zhangsan"
Pascal Case
MyVariableName = "zhangsan"
Snake Case
my_variable_name = "zhangsan"
```

通常来说，在函数内部定义的变量只能在该函数内使用。然而，如果想在函数内部创建或修改全局变量，需要使用 global 关键字：
```
def myfunc():
    global x
    x = "feichang bang"

myfunc()

print("Python shi " + x)
```

nonlocal
nonlocal用于嵌套函数之间，让内层函数修改外层函数的变量，但不是全局变量
```
def outer():
    x = "外层函数变量"
    def inner():
        nonlocal x  # 声明修改外层函数x
        x = "被内层函数改动了"
    inner()
    return x
print(outer())  # 输出: 被内层函数改动了
```

数据类型
```
x = str("nihao shijie")      # 字符串(str)  单引号或双引号效果相同
y = int(20)                  # 整数(int)
z = -3j    #复数，j代表虚部
z = float(20.5)              # 浮点数(float)
a = list(("pingguo", "li"))  # 列表(list)
b = tuple(("pingguo", "li")) # 元组(tuple)
c = range(6)                 # 范围(range)
d = dict(name="zhangsan", age=30)  # 字典(dict)
e = set(("pingguo", "li"))   # 集合(set)
f = frozenset(("lanmei", "yingtao")) # 不可变集合(frozenset)
g = bool(5)                  # 布尔(bool)
h = bytes(5)                 # 字节(bytes)
i = bytearray(5)             # 字节数组(bytearray)
j = memoryview(bytes(5))     # 内存视图(memoryview)
k = None                     # NoneType类型
```

运算符
```
/	除法	    x / y
%	取余   	x % y
**	幂运算	x ** y
//	整除	    x // y

逻辑运算符
and、or、not
```

pass关键字  暂时什么都不做
```
def test():
    pass
if b > a:
    pass     
```

 