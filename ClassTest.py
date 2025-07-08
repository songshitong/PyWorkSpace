from abc import ABC, abstractmethod
from typing import Protocol,Callable


class Person:
    def __init__(self, name, age): #初始函数  self指向类的当前实例
        self.name = name
        self.age = age

    def __str__(self): #toString方法
        return f"{self.name}({self.age}岁)"


class Student(Person): #继承
    def __init__(self, fname, lname):
        # 显式调用父类的__init__来保留原功能  不调用会覆盖
        Person.__init__(self, fname, lname)
        # 或者使用super()函数
        # super().__init__(fname, lname)
        # 在此添加子类自己的属性、初始化操作
        self.graduationyear = 2025

    #自定义迭代器
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


#python没有接口关键字  可以通过ABC，Protocol，Callable等实现
class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self, query: str) -> dict:
        """必须实现的数据获取接口"""
        pass
# 子类必须实现 fetch_data
class DatabaseFetcher(DataFetcher):
    def fetch_data(self, query: str) -> dict:
        return {"result": "data from database"}

 #Python 3.8+ 的 typing.Protocol 支持鸭子类型（Duck Typing），只需实现相同方法即可视为“接口”匹配
class Renderable(Protocol):
    def render(self) -> str:
       ...
class HTMLPage:
    def render(self) -> str:  # 无需继承，只需方法匹配
        return "<html>...</html>"
def display(component: Renderable) -> None:
    print(component.render())
    # 只要实现 render() 方法即可
display(HTMLPage())  # 正常运行


#Python 的函数是一等公民，可直接作为接口传递
# 定义接口：接收字符串，返回整数
Parser = Callable[[str], int]
def parse_int(s: str) -> int:
    return int(s)
def run_parser(parser: Parser, input_data: str) -> int:
    return parser(input_data)
print(run_parser(parse_int, "42"))  # 输出 42

if __name__ == '__main__':
    p1 = Person("张三", 36)
    print(p1)
    # 删除对象属性
    del p1.age
    # 删除整个对象
    del p1

    #可迭代对象
    #像列表、元组、字典、集合、字符串等，这些都属于可迭代对象(Iterable)。可迭代对象含有一个__iter__()方法（或实现了类似协议），
    # 我们可以通过iter()函数获取到它的迭代器
    #  for循环就是iter()实现，可以将对象通过__iter__和__next__扩展为可迭代对象
    fruits = ["apple", "banana", "cherry"]
    myit = iter(fruits) #获取迭代器
    print(next(myit))  # apple
    print(next(myit))  # banana
    print(next(myit))  # cherry
    #print(next(myit))  # 超出后抛出异常 StopIteration
    pass