def set_test():
    #集合（Set）是一种用于存储多个不同元素的数据结构，具有无序、不重复且元素不可修改的特点
    #集合元素无法通过索引访问，因此无法进行切片
    #由于集合没有固定的顺序，所以你不能使用索引访问元素，不能使用索引遍历
    #Python中True和1，False和0在集合里视为相同的值：
    thisset = {"pingguo", "xiangjiao", "yingtao", True, 1, 2}
    print(thisset)
    # 输出示例: {True, 2, 'xiangjiao', 'yingtao', 'pingguo'} (1被视为True，忽略重复)

    #新增元素
    thisset = {"pingguo", "xiangjiao", "yingtao"}
    thisset.add("juzi")
    print(thisset)
    # 输出示例: {'juzi', 'pingguo', 'xiangjiao', 'yingtao'}
    #使用update()方法添加多个元素  重复元素合并为一个
    thisset = {"pingguo", "xiangjiao", "yingtao", "mugua"}
    tropical = {"boluo", "mangguo", "mugua"}
    thisset.update(tropical) #update的参数适用于任何可迭代对象
    print(thisset)
    # 输出示例: {'boluo', 'mangguo', 'pingguo', 'xiangjiao', 'mugua', 'yingtao'}

    #使用remove()方法删除元素  不存在抛出异常
    #discard()方法同样可以删除集合中的元素，但如果元素不存在，不会抛出错误
    #pop()方法会随机删除并返回集合中的一个元素
    #clear()方法可以清空集合中所有元素
    #使用del关键字删除集合
    thisset = {"pingguo", "xiangjiao", "yingtao"}
    thisset.discard("juzi")
    print(thisset)


    #集合与其他可迭代对象的合并  |是set与set合并    自动去重
    set1 = {"a", "b", "c",1}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)
    print(set3)
    # 输出示例: {'a', 1, 2, 3, 'b', 'c'}

    #intersection()返回集合中共有的元素
    set1 = {"pingguo", "xiangjiao", "yingtao"}
    set2 = {"google", "microsoft", "pingguo"}
    set3 = set1.intersection(set2)
    print(set3) # 输出: {'pingguo'}

    #difference()返回集合中不在其他集合里的元素
    set1 = {"pingguo", "xiangjiao", "yingtao"}
    set2 = {"google", "pingguo"}
    set3 = set1.difference(set2)
    print(set3) #{'xiangjiao', 'yingtao'}

if __name__ == '__main__':
    set_test()