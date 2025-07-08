def list_test():
    #list可以包含不同的数据类型
    mylist = ["zhangsan", 18, True, "lisi", 3.14]
    print(mylist)
    #长度
    print(len(mylist))
    #数据类型
    print(type(mylist))  # 输出 <class 'list'>

    #通过构造函数创建列表
    mylist = list(("pingguo", "xiangjiao", "yingtao"))
    #元素访问通过[] 支持负索引
    print(mylist[-1])
    print(mylist[:2])
    print(mylist[1:])
    #in 元素存在
    print("pingguo" in mylist)
    #修改多个列表元素（索引范围）
    thislist = ["pingguo", "xiangjiao", "yingtao", "juzi", "mihoutao"]
    thislist[1:3] = ["heimei", "xigua"]
    print(thislist)
    #如果插入的元素数量超过了被替换的元素数量，列表的长度会相应增加：
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    thislist[1:2] = ["heimei", "xigua"]
    print(thislist) #输出: ['pingguo', 'heimei', 'xigua', 'yingtao']
    #如果插入元素的数量少于被替换的元素数量，列表长度将减少：
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    thislist[1:3] = ["xigua"]
    print(thislist) # 输出: ['pingguo', 'xigua']

    #insert() 不会发生替换
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    thislist.insert(2, "xigua")
    print(thislist)

    #元素追加 append() 和 extend()
    # append()
    # 只追加单个元素，若追加的是列表或元组，则整体作为单个元素追加到列表末尾。
    # extend()
    # 可以将任意可迭代对象的所有元素分别添加到列表末尾。
    mylist = ["pingguo", "xiangjiao", "yingtao"]
    # 使用append()
    mylist.append(["juzi", "mihoutao"])
    print(mylist)
    # 输出: ['pingguo', 'xiangjiao', 'yingtao', ['juzi', 'mihoutao']]
    # 使用extend()
    mylist.extend(["juzi", "mihoutao"])
    print(mylist)
    # 输出: ['pingguo', 'xiangjiao', 'yingtao', ['juzi', 'mihoutao'], 'juzi', 'mihoutao']

    #元素删除
    # remove()方法用于删除列表中指定的元素（第一次出现的）
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    thislist.remove("xiangjiao")
    print(thislist)
    # 输出: ['pingguo', 'yingtao']

    # pop()
    # 方法用于删除指定索引位置的元素，若不指定索引，则默认删除最后一项：
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    thislist.pop(1)
    print(thislist)  # 输出: ['pingguo', 'yingtao']
    #使用关键字del可以删除指定索引的元素：
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    del thislist[1]
    print(thislist)  # 输出: ['pingguo', 'yingtao']
    del thislist #删除整个

    #     clear() 清空列表内容
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    thislist.clear()
    print(thislist)  # 输出: []

    #列表遍历
    fruits = ["pingguo", "xiangjiao", "yingtao"]
    for fruit in fruits:
        print(fruit)
    #部分索引
    fruits = ["pingguo", "xiangjiao", "yingtao"]
    for i in range(len(fruits)):
        print(fruits[i])
    #while
    fruits = ["pingguo", "xiangjiao", "yingtao"]
    i = 0
    while i < len(fruits):
        print(fruits[i])
        i += 1
    #列表推导式
    # 列表推导式的标准语法：   条件是过滤，表达式也可以对结果操作
    # newlist = [表达式 for 变量 in 可迭代对象 if 条件]
    fruits = ["pingguo", "xiangjiao", "yingtao"]
    [print(fruit) for fruit in fruits]
    #结果表达式修改
    numbers = [x * 2 for x in range(5)]
    print(numbers)
    # 输出: [0, 2, 4, 6, 8]
    #使用条件表达式
    fruits = ["pingguo", "xiangjiao", "yingtao"]
    newlist = [x if x != "xiangjiao" else "chengzi" for x in fruits]
    print(newlist)
    # 输出: ['pingguo', 'orange', 'yingtao']

    #排序  默认情况下，sort()方法将列表元素按字母顺序升
    mylist = ["juzi", "mihoutao", "pingguo", "xiangjiao", "lizhi"]
    mylist.sort()
    print(mylist)
    # 输出: ['juzi', 'lizhi', 'mihoutao', 'pingguo', 'xiangjiao']
    #降序
    numbers = [100, 20, 5, 90, 30]
    numbers.sort(reverse=True)
    print(numbers)
    # 输出: [100, 90, 30, 20, 5]
    #自定义规则
    def myfunc(n):
        return abs(n - 50) #根据数字与50的距离进行排序

    numbers = [100, 50, 65, 82, 23]
    numbers.sort(key=myfunc)
    print(numbers)
    # 输出: [50, 65, 23, 82, 100]

    #不区分大小写  或者全按小写
    mylist = ["pingguo", "Juzi", "xiangjiao", "Yingtao"]
    mylist.sort(key=str.lower)
    print(mylist)
    # 输出: ['Juzi', 'pingguo', 'xiangjiao', 'Yingtao']

    #反转列表
    mylist = ["juzi", "mihoutao", "pingguo"]
    mylist.reverse()
    print(mylist)
    # 输出: ['pingguo', 'mihoutao', 'juzi']

    #复制列表
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    mylist = thislist.copy()
    print(mylist)
    # 输出: ['pingguo', 'xiangjiao', 'yingtao']
    #内置的list()函数创建列表的副本
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    mylist = list(thislist)
    print(mylist)
    # 输出: ['pingguo', 'xiangjiao', 'yingtao']

    #使用切片（[:]）方法复制列表
    thislist = ["pingguo", "xiangjiao", "yingtao"]
    mylist = thislist[:]
    print(mylist)
    # 输出: ['pingguo', 'xiangjiao', 'yingtao']

if __name__ == '__main__':
    list_test()