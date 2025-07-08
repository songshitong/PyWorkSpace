import json
import re



def str_test():
    # Python 中的字符串实际上是 Unicode 字符构成的数组，因此你可以通过索引访问其中的单个字符
    a = "nihao"
    print(a[1])  # 输出: 'i'

    # 遍历
    for x in "xiangjiao":
        print(x)
    # 获取长度
    a = "nihao shijie"
    print(len(a))  # 输出：12

    # 检查文字存在与不存在
    txt = "shenghuo zhong zuihao de dongxi dou shi mianfei de!"
    print("mianfei" in txt)  # 输出 True
    print("anggui" not in txt)  # 输出 True

    #切片
    b = "nihao, shijie!"
    print(b[2:5])  # 输出 hao
    print(b[:5])  # 输出 nihao  默认从0开始
    print(b[7:])  # 输出 shijie! 自动到结束
    print(b[-6:-1])  # 输出 shiji 从末尾开始计数
    print(a.upper())  # 输出 NIHAO, SHIJIE!  转大写
    print(a.lower())  #转小写
    print(a.strip())  #移除前后空格

    # 占位符
    #F-String是Python 3.6新增的字符串格式化方法 f"字符串"
    age = 36
    txt = f"Wo jinnian {age} sui"
    print(txt)  # 输出: Wo jinnian 36 sui
    #格式化修饰符：
    #:, 数字千位分隔符
    # :.2f 保留两位小数
    # :% 百分比格式
    # :b 二进制格式
    # :x 十六进制格式
    price = 49.567
    txt = f"价格是 {price:.2f} 美元"
    print(txt)

    # format函数
    #format()方法是Python 3.6之前推荐的格式化方式，但速度较慢且较复杂
    age = 36
    txt = "Wo jinnian {} sui".format(age)
    print(txt)  # 输出: Wo jinnian 36 sui

    #json转dict
    # JSON格式的字符串
    json_str = '{ "name":"张三", "age":30, "city":"北京"}'
    # 转换为Python字典
    data = json.loads(json_str)
    # 访问字典中的值
    print(data["name"])  # 输出：张三

    #json转dict
    # Python字典对象
    data = {
        "name": "李四",
        "age": 25,
        "city": "上海"
    }
    # 转换为JSON格式的字符串  indent缩进  sort_keys按照key排序  ensure_ascii是否转为ascii
    json_str = json.dumps(data,indent=2, sort_keys=True,ensure_ascii=False)
    print(json_str)  #{"name": "\u674e\u56db", "age": 25, "city": "\u4e0a\u6d77"}


def re_test():
    #查找所有匹配项，返回一个列表。
    txt = "电话123-4567，备用电话987-6543"
    nums = re.findall(r"\d+", txt)
    print(nums)  # ['123', '4567', '987', '6543']

    #搜索字符串中第一个匹配项，返回Match对象
    text = "我爱Python编程！"
    match = re.search("Python", text)
    if match:
        print("找到匹配：", match.group())
        print(match.start()) #2
        print(match.end())  #8
        print(match.span())  #(2, 8)
    else:
        print("未找到匹配。")

    #根据匹配的内容分割字符串，返回分割后的列表
    txt = "苹果,香蕉;橘子;梨"
    fruits = re.split(r"[;,]", txt)
    print(fruits)  # ['苹果', '香蕉', '橘子', '梨']


    #替换字符串中匹配的内容
    txt = "密码123456"
    result = re.sub(r"\d", "#", txt)  #替换数字为#
    print(result)  # 密码######



if __name__ == '__main__':
    str_test()
    re_test()