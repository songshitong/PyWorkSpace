#!/usr/bin/python
# -*- coding: UTF-8 -*-
import keyword
# 第一行代码
print('hello ,this is my first python  你好，世界')
print('python保留字:\n'+keyword.kwlist.__str__())
if True:
    print('if result true')
else:
    print('if result false')
var = 100
if (var == 100): print('var 100')

input("\n\n按下 enter 键后退出。")
# import 与 from...import
#
# 在 python 用 import 或者 from...import 来导入相应的模块。
#
# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# ，但是那些由单一下划线（_）开头的名字不在此例。大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来，例如:
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''
x="a"
y="b"
# 换行输出
print(x )
print(y )

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

# 如下实例，查看 max 内置函数的参数列表和规范的文档
help(max)

# Number（数字）
# Python3 支持 int、float、bool、complex（复数） type()查看变亮的对象类型，也使用isinstance判断       type()不会认为子类是一种父类类型。 isinstance()会认为子类是一种父类类型。
a = True
print('a is '+type(a).__name__)

# 当你指定一个值时，Number 对象就会被创建：

var1 = 1
var2 = 10

# 您也可以使用del语句删除一些对象引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]]
del var1
var1 = 2
print('这是删除后的var1')
print(var1)

# 可以对已存在的字符串进行修改，并赋值给另一个变量，如下实例：
var1 = 'Hello World!'
print("更新字符串 :- ", var1[:6] + 'Runoob!')
#字副串 转义字符
# 字符串运算符  %	格式字符串    r/R	原始字符串 - 原始字符串： in	成员运算符  [ : ]	截取字符串中的一部分  *	重复输出字符串
#  %s	 格式化字符串   %d	 格式化整数
# 格式化操作符辅助指令:*	定义宽度或者小数点精度   (var)	映射变量(字典参数)    str.format()，它增强了字符串格式化的功能。
print("My name is %s and weight is %d kg!" % ('Zara', 21))
# Python三引号（triple quotes）
# python中三引号可以将复杂的字符串进行复制:
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）
# >>> hi = '''hi
# there'''
# >>> hi   # repr()
# 'hi\nthere'
# >>> print hi  # str()
# hi
# there


#  2 ** 5 # 乘方   数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符(返回商的整数部分)    复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
# 算数运算副
# 比较运算副
# 赋值运算符  **= 幂赋值运算符	c **= a 等效于 c = c ** a  //=	取整除赋值运算符	c //= a 等效于 c = c // a
# 位运算符 &	按位与运算符 |	按位或运算符    ^	按位异或运算符  ~	按位取反运算符  <<	左移动运算符   >>	右移动运算符
# 逻辑运算符  and	x and y	布尔"与"   or	x or y	布尔"或"      not	not x	布尔"非"
# 成员运算符 in	如果在指定的序列中找到值返回 True，否则返回 False。   not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
# 身份运算符
# 身份运算符用于比较两个对象的存储单元   is	is 是判断两个标识符是不是引用自一个对象（类似 id(x) == id(y)  id（）取对象内存地址）   is not（类似 id(a) != id(b)）	is not 是判断两个标识符是不是引用自不同对象
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
# 八进制数必须写成0o777；二进制必须写成0b111，0x十六进制
# 新增了一个bin()函数用于将一个整数转换成二进制字串。
strr = 'Runoob'
print('2**5 = '+str(2 ** 5))
print(strr)  # 输出字符串
print(strr[0:-1])  # 输出第一个到倒数第二个的所有字符
print(strr[0])  # 输出字符串第一个字符
print(strr[2:5])  # 输出从第三个开始到第五个的字符
print(strr[2:])  # 输出从第三个开始的后的所有字符
print(strr * 2)  # 输出字符串两次

# 斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串  前面加个u表示unicode
print('Ru\noob')
print(r'Ru\noob')
# Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误   Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始

# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
# 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
# 可以使用 del 语句来删除列表的的元素
# Python 表达式	结果 	描述
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	迭代
list = ['abcd', 786, 2.23, 'runoob', 70.2]
del list[1]
list.append(1)
list[2] = 2001
tinylist = [123, 'runoob']


print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开      string、list和tuple都属于sequence（序列）
# 无关闭分隔符
# 任意无符号的对象，以逗号隔开，默认为元组
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
print(tuple)
#  集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
# 向字典添加新内容的方法是增加新的键/值对
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令
#  在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

 # 在序列中遍历时，索引位置和对应值可以使用enumerate()函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# 反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 10, 2)):
    print(i)
# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

dictt = {}
dictt['one'] = "1 - 菜鸟教程"
dictt[2] = "2 - 菜鸟工具"
dictt['one'] = "1 - 菜鸟教程1"#修改字典
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print("dictt is : "+str(type(dictt).__name__))
print(dictt['one'])  # 输出键为 'one' 的值
print(dictt[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典如下
a = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(a)
#
# 循环控制语句 break 语句	在语句块执行过程中终止循环，并且跳出整个循环
# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
# pass 语句	pass是空语句，是为了保持程序结构的完整性 不做任何事情，一般用做占位语句
count = 0
while (count < 3):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")

flag = 1
# while (flag): print('Given flag is really true!')
print("Good bye!")
# 注意：以上的无限循环你可以使用 # CTRL + C 来中断循环

# for循环的语法格式如下：
# for iterating_var in sequence:
#    statements(s)
for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)
print("Good bye")

# 另外一种执行循环的遍历方式是通过索引，如下实例：
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])
print("Good bye!")
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print('\n')
print(next(it))   # 输出迭代器的下一个元素
print(next(it))

# 迭代器对象可以使用常规for语句进行遍历
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print(x, end=" ")
print('\nwhile true:\n')

import sys  # 引入 sys 模块
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        # sys.exit
        break

# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。


def fibonacci(n):  # 生成器函数 - 斐波那契
    aa, bb, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield aa
        aa, bb = bb, aa + bb
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        # sys.exit
        break

# Python 定义函数使用 def 关键字，一般格式如下：
# def 函数名（参数列表）:
#     函数体
# python 中，类型属于对象，变量是没有类型的：
# a=[1,2,3]
# a="Runoob"
# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
print('\n不可变对象传值\n')


def changeint(a1):
    a1 = 10


b1 = 2
changeint(b1)
print(b1) # 结果是 2
# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为Python
# 解释器能够用参数名匹配参数值。
def printme(str):
    "打印任何传入的字符串"
    print(str);
    return;
# 调用printme函数
printme(str="菜鸟教程");

# 以下实例中演示了函数参数的使用不需要使用指定顺序：
# 可写函数说明


def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="runoob");
# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入age参数，则使用默认值：
# 可写函数说明


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="runoob");
print("------------------------")
printinfo(name="runoob");

# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

# 匿名函数
# python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
#     lambda 只是一个表达式，函数体比 def 简单很多。
#     lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#     lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#     虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
# lambda 函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
# 变量作用域
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
#     L （Local） 局部作用域
#     E （Enclosing） 闭包函数外的函数中
#     G （Global） 全局作用域
#     B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
        # 也就是说这这些语句内定义的变量，外部也可以访问，如下代码
if True:
   msg = 'I am from Runoob'
msg
'I am from Runoob'
# 实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
# 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：

def test():
     msg_inner = 'I am from Runoob'
# msg_inner

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# 以下实例修改全局变量 num：
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
# 如果要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量则需要
# nonlocal 关键字了，如下实例：


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()

# 另外有一种特殊情况，假设下面这段代码被运行：(a2=1 没有)
a2 = 10


def test():
    a2 = 1
    a2 += a2
    print(a2)


test()


#  python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
#
# 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
#
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
#  当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端
# 搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
# 这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
# 搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量
print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为：', sys.path, '\n')

# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
# 我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# 如果没有给定参数，那么dir()函数会罗列出当前定义的所有名称
# import fibo, sys
# dir(fibo)
#    模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
#    每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用
#    当你确实知道你在做什么的话，你也可以通过modname.itemname这样的表示法来访问模块内的函数
#    可以使用import 直接把模块内（函数，变量的）名称导入到当前操作模块。比如:
# from fibo import fib, fib2    ？？？？
# fib(500)
   # 这种导入的方法不会把被导入的模块的名称放在当前的字符表中（所以在这个例子里面，fibo这个名称是没有定义的）

   # 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
   # import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个: exc:ImportError
   # 异常被抛出了
   # 如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字


# 标准模块
# Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
# 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
# 这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
# 应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:
#  import sys
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>> sys.ps1 = 'C> '
# C> print('Yuck!')


#  包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B

# 从一个包中导入 *
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
# 作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊

# 使用from Package import specific_submodule这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名

#  如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。
   # 比如，如果模块sound.filters.vocoder 要使用包sound.effects中的模块echo，你就要写成 from sound.effects import echo。
# from . import echo
# from .. import formats
# from ..filters import equalizer

#  无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
# 包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。
# 可以修改这个变量，用来影响包含在包里面的模块和子包。
# 这个功能并不常用，一般用来扩展包里面的模块

#python输入输出
# 输出格式美化
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
#     str()： 函数返回一个用户易读的表达形式。
#     repr()： 产生一个解释器易读的表达形式。

# 读取键盘输入
# Python提供了 input() 置函数从标准输入读入一行文本，默认的标准输入是键盘。
# input 可以接收一个Python表达式作为输入，并将运算结果返回。
# str = input("请输入：");
# print ("你输入的内容是: ", str)

# 读和写文件
# open() 将会返回一个 file 对象，基本语法格式如下:
# open(filename, mode)
#     filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
#     mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

#  python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# 基本接口：
# pickle.dump(obj, file, [,protocol])
# 有了 pickle 这个对象, 就能对 file 以读取的形式打开:
# x = pickle.load(file)
# 注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


# Python3 OS 文件/目录方法
# os 模块提供了非常丰富的方法用来处理文件和目录，具体看api


# Python有两种错误很容易辨认：语法错误和异常。
# 语法错误
# Python 的语法错误或者称之为解析错，是初学者经常碰到的
# try语句按照如下方式工作；
#     首先，执行try子句（在关键字try和关键字except之间的语句）
#     如果没有异常发生，忽略except子句，try子句执行后结束。
#     如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
#     如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
# 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
# 处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
# except (RuntimeError, TypeError, NameError):
#         pass
# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。例如:
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# 使用 else 子句比把所有的语句都放在
# try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。
# 异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。例如:
def this_fails():
    x = 1 / 0
try:
    this_fails()
except ZeroDivisionError as err:
        print('Handling run-time error:', err)

 # Python 使用 raise 语句抛出一个指定的异常
 # raise NameError('HiThere')

# raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
# 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
try:
    raise NameError('HiThere')
except NameError:
        print('An exception flew by!')
        raise

# 用户自定义异常
# 你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自Exception类，或者直接继承，或者间接继承
#  class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     raise MyError(2 * 2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)
#
# raise MyError('oops!')

# 类 Exception 默认的 __init__() 被覆盖。
# 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
# 大多数的异常的名字都以"Error"结尾，就跟标准的异常命名一样。

# 定义清理行为
# try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。 例如:
try:
    raise KeyboardInterrupt
finally: print('Goodbye, world!')

# 以上例子不管 try 子句里面有没有发生异常，finally 子句都会执行。
# 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出

# 预定义的清理行为
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
# 这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

for line in open("myfile.txt"):
    print(line, end="")

# 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# 很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法），像下面这样：
def __init__(self):
    self.data = []
# 类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法。所以在下例中，可以这样创建一个新的实例:
x = MyClass()
# 当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。

# self代表类的实例,代表当前对象的地址，而非类,self.class 则指向类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:

class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()

# 下划线的_的意义？？

# Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
# class DerivedClassName(BaseClassName1):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
# BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
# class DerivedClassName(modname.BaseClassName):

# Python同样有限的支持多继承形式。多继承的类定义形如下例:
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法

# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。
# 类的专有方法：
# __init__: 构造函数，在生成对象时调用
# __del__: 析构函数，释放对象时使用
# __repr__: 打印，转换
# __setitem__: 按照索引赋值
# 等。。

# Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
