

def tuple_test():
    #元组（Tuple）是一种用于存储多个数据的集合类型。与列表不同的是，元组是有序但不可变的数据结构，创建后无法修改

    #曲线修改tuple 转为list
    x = ("pingguo", "xiangjiao", "yingtao")
    y = list(x)
    y[1] = "mihoutao"
    x = tuple(y)
    print(x)
    # 输出: ('pingguo', 'mihoutao', 'yingtao')

    #增加元素  1 转为list  2 使用+
    thistuple = ("pingguo", "xiangjiao", "yingtao")
    y = ("juzi",)  # 注意：单元素元组必须加逗号
    thistuple += y
    print(thistuple)
    # 输出: ('pingguo', 'xiangjiao', 'yingtao', 'juzi')

    #删除
    thistuple = ("pingguo", "xiangjiao", "yingtao")
    del thistuple

    #解包
    fruits = ("pingguo", "mangguo", "mugua", "boluo", "yingtao")
    (green, *tropic, red) = fruits  #星号代表多个元素
    print(green)  # 输出: pingguo
    print(tropic)  # 输出: ['mango', 'mugua', 'boluo']
    print(red)  # 输出: yingtao

    #复制元组元素
    fruits = ("pingguo", "xiangjiao", "yingtao")
    mytuple = fruits * 2
    print(mytuple)
    # 输出: ('pingguo', 'xiangjiao', 'yingtao', 'pingguo', 'xiangjiao', 'yingtao')
    
if __name__ == '__main__':
    tuple_test()