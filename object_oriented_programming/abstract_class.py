


"""前言
抽象基类(abstract base class,ABC)，提到这个概念应该会马上联想到面向对象、继承。作为继承的一种，
它拥有继承中代码共享、提高代码的重用性等优点。例如，下面示例：



抽象基本类的几大特点：
python中抽象基类必须继承自ABC(Abstract Base Class)类；
可以包含类方法、静态方法、普通方法，但是必须至少有一个抽象方法；
抽象基类不能实例化；
子类需要实现基类中定义的所有抽象方法；"""


"""
抽象基类
虽然Python中抽象基类和接口概念非常相近，但是它们还是有一些不同之处，例如：

接口需要被实现的子类完成接口中指定的所有方法，而抽象基类不是，抽象基类则没有这么严格的要求；
接口需要所有方法都是抽象方法，而抽象基类中有抽象方法，也有自己实现的方法；
正是因为抽象基类和接口的不同之处使得接口之所以称为接口、抽象基类之所以称为抽象基类。

为什么使用抽象基类？
抽象基类的存在自然有它的价值。当你学会一种编程语言的语法时，你可以轻松的完成一项功能的开发，但是如果希望把代码完成的更加优美高效，那么就需要在设计模式等方面下一些功夫，抽象基类就是其中的一个选择，抽象基类具有以下优点：

处理继承问题方面更加规范、系统
明确调用之间的相互关系
使得继承层次更加清晰
限定子类实现的方法
什么是抽象基类？
必须包含一个抽象函数(纯虚函数)，它是一个不完整的类，它有已经被实现的方法，也有需要子类重写的方法。

Python抽象基类
抽象基类：通过继承abc模块中的ABC类来实现抽象基类。

抽象方法：通过装饰器@abstractmethod来定义抽象方法，也就是需要子类实现的方法。

装饰器@abstractmethod除了可以实现抽象方法外，还可以装饰类方法(@classmethod)、静态方法(@staticmethod)、属性(@property)。
实现抽象基类："""

from abc import ABC
from abc import abstractmethod


class Database(ABC):

    def register(self, host, user, password):
        print("Host : {}".format(host))
        print("User : {}".format(user))
        print("Password : {}".format(password))
        print("Register Success!")

    @abstractmethod
    def query(self, *args):
        """
        传入查询数据的SQL语句并执行
        """
        pass

    @staticmethod
    @abstractmethod
    def execute(sql_string):
        """
        执行SQL语句
        """
        pass

"""从抽象基类Database 的实现可以看出，它共包含3个方法，其中register 是每个子类都需要的，
直接实现在抽象基类里，是一个普通的类方法。query 和execute 只是在基类中进行类声明，给出了描述，
但并没有实现，它限定了继承Database 的子类必须实现这两个方法。"""


class Component1(Database):
    def __init__(self, host, user, password):
        self.register(host, user, password)

    @staticmethod
    def execute(sql_string):
        print(sql_string)

    def query(self, *args):
        sql_string = "SELECT ID FROM db_name"
        self.execute(sql_string)


class Component2(Database):
    def __init__(self, host, user, password):
        self.register(host, user, password)

    @staticmethod
    def execute(sql_string):
        print(sql_string)

    def query(self, *args):
        sql_string = "SELECT NAME FROM db_name"
        self.execute(sql_string)


if __name__ == '__main__':
    comp1 = Component1("00.00.00.00", "abc", "000000")
    comp2 = Component2("11.11.11.11", "ABC", "111111")
    comp1.query()
    comp2.query()

    """
    输出：
    Host : 00.00.00.00
    User : abc
    Password : 000000
    Register Success!
    Host : 11.11.11.11
    User : ABC
    Password : 111111
    Register Success!
    SELECT ID FROM db_name
    SELECT NAME FROM db_name
    """


