"""
1、类属性
（1）类属性概念
在 Python 中，一切皆为对象，类也不例外，在程序运行过程中，类也会做为一个对象使用。

类对象与实例对象不同，可以理解为实例对象是由类对象复制而来，每个实例对象之间具有数据独立性。而类对象在程序运行过程中，只有一个。

既然是对象，那么就可以拥有自己的属性，在类中定属性时，属性名有self前缀的是实例属性(self.high)，而在类中直接定义的属性即为类属性。


2） 类属性特征：
在类中直接定义的变量为类属性；
在方法中使用类属性时，需要使用类名作为前缀，类名.类属性名
在类的外部可以通过类名或者实例对象名访问类的属性；
所有的实例对象名共享一个类属性；
类属性的值只能获取，不能直接修改，只能通过方法进行修改；
"""

# 定义一个饮水机类
class WaterDispenser:
    # 剩余水量--类变量
    surplus_water = 1500
    # 出水口
    def water_outlet(self, n):
        WaterDispenser.surplus_water -= n
        print("饮水机提示剩余水量：", WaterDispenser.surplus_water)

    @classmethod
    def modify_surplus_water(cls):
        cls.surplus_water = 100
        return cls.surplus_water


wd1 = WaterDispenser()
wd2 = WaterDispenser()

print(f"饮水机原有水量{WaterDispenser.surplus_water}")
# 第一个饮水机出水100
print("第一个饮水机出水100")
wd1.water_outlet(100)
print(f"第一个饮水机确认水量：{wd1.surplus_water}")
print(f"饮水机真实水量：{WaterDispenser.surplus_water}")



# 第二个饮水机出水200
print("第二个饮水机出水200")
wd2.water_outlet(200)
print(f"第二个饮水机确认水量：{wd2.surplus_water}")
print(f"饮水机真实水量：{WaterDispenser.surplus_water}")

wd2.surplus_water = 10000
print(f"第二个饮水机修改类属性剩余水量后：{WaterDispenser.surplus_water}")

WaterDispenser.surplus_wate = 22222222222
print(f"类名修改类属性剩余水量后：{WaterDispenser.surplus_water}")

print("通过方法修改剩余的水量：",WaterDispenser.modify_surplus_water())
--------------------------------------------------------------------------------------------------
# 饮水机原有水量1500
# 第一个饮水机出水100
# 饮水机提示剩余水量： 1400
# 第一个饮水机确认水量：1400
# 饮水机真实水量：1400


# 第二个饮水机出水200
# 饮水机提示剩余水量： 1200
# 第二个饮水机确认水量：1200
# 饮水机真实水量：1200


# 第二个饮水机修改类属性剩余水量后：1200
# 类名修改类属性剩余水量后：1200

# 通过方法修改剩余的水量：100


"""2、类方法
类方法也可以通过类名直接进行使用，类方法在定义时，需要使用 @classmethod 装饰器进行修饰。

与实例方法不同的是，实例方法有一个默认参数 self，代表当前调用方法的实例对象，而类方法的默认参数为 cls， 该参数也是在使用时，由解释器自动传入的，但传入的对象不是实例对象，而是类对象。

在类方法中，可以通过参数 cls 使用类属性。

一般类方法用来封装工具类使用，将一些复杂的代码逻辑封装成类方法，由类名直接调用，不需要实例对象，比如时间处理，网络请求处理等。

需要注意的是，如果类中即定义了实例属性，又定义了类方法，那么在类方法中是不能使用实例属性的，因为在使用类方法的过程中，实例对象不存在，所以不能使用实例属性。

之所以有类方法的原因就是类方法中的cls参数，主要就是为了使用这个参数去获取类的东西；

注意：classmethod常用在比如时间处理，网络请求处理等"""

# 封装了一个日期时间获取的工具类
import datetime
class Utils:
    now = datetime.datetime.now()

    @classmethod
    def current_date_time(cls):
        return cls.now

    @classmethod
    def current_date(cls):
        return cls.now.strftime("%Y-%m-%d")

    @classmethod
    def current_time(cls):
        return cls.now.strftime("%H-%M-%S")

    @classmethod
    def getYear(cls):
        return cls.now.year

    @classmethod
    def getMonth(cls):
        return cls.now.month

    @classmethod
    def getDay(cls):
        return cls.now.day


print(Utils.current_date_time())
print(Utils.current_date())
print(Utils.current_time())
print(Utils.getYear())
print(Utils.getMonth())
print(Utils.getDay())