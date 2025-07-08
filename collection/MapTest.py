def map_test():
    #在Python 3.7及之后的版本中是有序的，在更早的版本中是无序的
    #除了使用花括号创建字典，也可以使用dict()方法创建
    thisdict = {
        "xingming":"zhangsan",
        "nianling": 30,
        "guojia": "japan"
    }
    print(thisdict)
    thisdict = dict(xingming="zhangsan", nianling=36, guojia="nuowei")
    print(thisdict)

    #访问字典
    # ["key"]与get()：获取字典中指定键的值。
    # keys()：查看当前所有键。
    # values()：查看当前所有值。
    # items()：查看所有键值对（元组形式）。
    # in关键字：判断字典中是否包含某键。

    #修改
    thisdict = {
        "pinpai": "Fute",
        "xingming": "Mustang",
        "nianfen": 1964
    }

    # 将 'nianfen' 更新为2018
    thisdict["nianfen"] = 2018
    thisdict.update({
        "pinpai": "Fute",
        "xingming":"liu"
    })
    print(thisdict)

    #删除
    # pop不存在报错
    #在Python 3.7+版本中，popitem()会移除最新插入的键值对（有序特性）。在Python 3.6及之前的版本中则随机移除一个条目
    #del关键字可删除指定键，也可删除整个字典对象   不存在也报错
    #使用clear()方法清空字典内容
    thisdict = {
        "pinpai": "Fute",
        "xinghao": "Mustang",
        "nianfen": 1964
    }
    thisdict.pop("xinghao")
    del thisdict["pinpai"]
    print(thisdict)

    #遍历
    for k in thisdict:
        print(k)
        print(thisdict[k])
    for v in thisdict.values():
        print(v)
    for k in thisdict.keys():
        print(k)
    for k, v in thisdict.items():
        print(k, v)


if __name__ == '__main__':
    map_test()