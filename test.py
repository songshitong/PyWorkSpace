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
