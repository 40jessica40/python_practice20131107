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

print("通过方法修改剩余的水量：", WaterDispenser.modify_surplus_water())
# --------------------------------------------------------------------------------------------------
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

注意：classmethod一般用作类属性(共有属性)的处理，常用在比如时间处理，网络请求处理等"""

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


"""3、静态方法
静态方法在定义时，需要使用 @staticmethod 装饰器进行装饰，与类方法不同的是，静态方法没有默认参数。

静态方法和普通的函数本质上是一样的，只是定义在了类中。

一般情况下，静态方法同类方法一样，也是在封装工具类时使用，区别在于，静态方法中不需要使用类属性（不是不能使用，只是不建议）。

注意：静态方法中不需要使用类属性，独立开来的，比较有个性，谁也不张 """


class Calc:
    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def sub(n1, n2):
        return n1 - n2

    @staticmethod
    def mul(n1, n2):
        return n1 * n2

    @staticmethod
    def div(n1, n2):
        return n1 / n2


print(Calc.add(10, 20))
print(Calc.sub(10, 20))
print(Calc.mul(10, 20))
print(Calc.div(10, 20))

"""4、封装
（1）什么是封装
封装是面向对象编程中三大特征之一，指的是将数据和操作数据的方法打包在一起，形成一个类或对象。

封装的目的是隐藏对象的内部实现细节，提供一个安全且易于使用的接口，使得对象之间的交互更加简单和可靠。

封装主要包括以下几个方面的内容：

数据隐藏：通过将对象的数据属性设置为私有或受保护的，防止外部直接访问和修改对象的数据。这样可以确保对象的数据在被操作时不会被意外篡改或破坏。
方法封装：将对象对自身数据的操作封装在方法中，只通过方法来访问和修改对象的数据。这样可以确保对对象的操作符合预期，避免了外部错误地修改对象的数据。
接口定义：通过定义公共接口，将对象的功能暴露给外部使用者。使用者只需关心如何使用接口提供的方法，而不需要了解内部实现细节。这样可以提高代码的可读性和可维护性，同时也能够实现代码的模块化和复用。
（2）封装的优势
数据安全性：封装隐藏了对象的内部实现细节，保护了数据的完整性和安全性。外部无法直接访问或修改对象的数据，必须通过规定的方法进行操作，减少了意外错误的发生。
代码模块化：封装将对象的数据和操作打包在一起，实现了代码的模块化。不同的对象可以独立开发和测试，降低了代码的耦合性，增加了系统的可维护性和扩展性。
简化接口：封装将对象的功能通过公共接口暴露给外部，隐藏了内部实现细节。外部使用者只需了解接口的使用方法，而无需关心具体的实现。这降低了外部使用者的使用难度，也提高了代码的可读性和易用性。
（3） 无下划线前缀(公有权限)
Python 中默认定义的属性和方法，都是公有的方法。无论是在类外，还是在派生的子类中，都可以进行访问，类似其它语言中的 public 修饰符的作用。
（4） _ 单下划线前缀（保护权限）
Python 在类中使用 单下划线前缀 实现其它语言中 protected 保护权限的功能，在属性或方法（包括类属性和类方法，作用相同）前添加一个单下划线，该属性或方法，在当前类中可以访问，在类外理论上不可访问（使用时不提示，但写出来程序可以运行，但有警告），在通过继承派生的子类中可以访问；"""

class A(object):
    def __init__(self):
        # 公有属性
        self.a = 10
        # 保护属性
        self._b = 20

    # 公有方法
    def show(self):
        # 在类中使用公有属性
        print(f"A: {self.a}")
        # 在类中使用保护属性
        print(f"B: {self._b}")
        # 在类中使用保护权限的方法
        self._display()

    # 保护权限的方法
    def _display(self):
        print(f"B: {self._b}")


obj = A()
# 在类外使用公有属性
print(obj.a)# 10
# 在类外无法使用保护仅限的属性（不建议这样使用）
print(obj._b)# 20

# 在类外使用公有方法
"""
A: 10
B: 20
B: 20
"""
obj.show()
# 在类外无法使用保护权限的方法（不建议这样使用）
obj._display()# B: 20


"""5） __ 双下划线前缀（私有属性）
Python 在类中使用 双下划线前缀 实现其它语言中 private 私有权限的功能，在属性或方法（包括类属性和类方法，作用相同）前添加一个双下划线，
该属性或方法，只能在当前类中可以访问，在类外任何位置不可访问（只是理论上不可访问，通过某些方式，还是可以在类外访问，不建议这样使用）。

注意：私有属性和方法，属于实例属性和方法，只能实例进行调用，但是不能直接调用，通过某些方式，还是可以在访问"""

class A(object):
    def __init__(self):
        # 公有属性
        self.a = 10
        # 保护属性
        self._b = 20
        # 私有属性
        self.__c = 30

    # 公有方法
    def show(self):
        # 在类中使用公有属性
        print(f"A: {self.a}")
        # 在类中使用保护属性
        print(f"B: {self._b}")
        # 在类中使用私有属性
        print(f"C: {self.__c}")
        # 在类中使用保护权限的方法
        self._display()
        # 在类中使用私有方法
        self.__info()


    # 保护权限的方法
    def _display(self):
        print(f"B: {self._b}")

    # 私有权限的方法
    def __info(self):
        # 在类中使用私有属性
        print(f'C: {self.__c}')
obj = A()
# 在类外使用公有属性
print(obj.a)# 10
# 在类外无法使用保护仅限的属性（不建议这样使用）
print(obj._b)# 20
# 在类外使用私有属性，访问失败
# print(obj.__c)# AttributeError: 'A' object has no attribute '__c'
# 在类外使用公有方法
"""
A: 10
B: 20
C: 30
B: 20
30
"""
obj.show()
# 在类外无法使用保护权限的方法（不建议这样使用）
# obj._display()# B: 20
# 在类外访问私有方法，访问失败
# obj.__info()# AttributeError: 'A' object has no attribute '__info'. Did you mean: '_A__info'?

"""5、继承
（1）什么是继承
继承是面向对象编程中的三大概念之二，指的是一个类基于另一个类来创建。

创建出来的新类称为子类或派生类。被继承的类称为父类或基类。

通过继承，子类可以继承父类的属性和方法，并且可以在此基础上添加新的属性和方法，或者对继承的属性和方法进行修改重构。

A、继承的特点
继承关系：继承创建了一个父类和子类之间的关系。子类继承了父类的特性，包括属性和方法。子类可以重用父类的代码，减少了代码的冗余。
子类的扩展：子类可以在继承父类的基础上，添加新的属性和方法。这样可以对父类进行扩展，使得子类具有更多的功能。
代码共享和重用：通过继承，子类可以共享父类的代码。父类中通用的属性和方法可以被多个子类继承和使用，提高了代码的重用性，并减少了开发时间和成本。
继承的层次结构：继承可以形成一个层次结构，其中一个父类可以有多个子类，而子类又可以成为其他子类的父类。这种层次结构可以更好地组织和管理代码，使得代码更加结构化和模块化。
B、继承的优势
代码重用：继承允许子类重用父类的代码，减少了代码的冗余，提高了代码的可维护性和复用性。
扩展性：通过继承，子类可以在父类的基础上添加新的属性和方法，实现对父类的扩展，使得子类具有更多的功能。
类型的兼容性：由于子类继承了父类的特性，子类可以被当作父类的实例来使用。这样，在需要父类类型的地方，可以使用子类的实例，增加了代码的灵活性和可扩展性。

（2）单继承
单继承是指一个子类只继承一个父类。"""
class A(object):
    # A 继承自 object 根类
    def show(self):
        print("父类A的方法")

class B(A):
    # B类 继承自 A类
    def display(self):
        print("子类B的方法")

b = B()
# 子类对象使用自己的方法
b.display()
# 子类对象使用父类的方法，如果父类没有该方法则继续向上查找，直到根类
b.show()

"""（3）方法重写(重构)
在子类中，可以对父类中的方法实现进行重写（方法名不变，内部逻辑发生改变），实现新的功能实现。
当子类和父类方法名和参数都相同时，子类调用的是子类的方法；"""
class A(object):
    # A 继承自 object 根类
    def show(self):
        print("父类A的方法")

class B(A):
    # 子类重写父类方法
    def show(self):
        print("子类B的方法")

b = B()
# 当子类方法与父类方法同名时，调用子类方法
b.show()

"""（4）super()调用父类方法
如果在子类中还要使用父类中的方法，可以使用 super()函数来调用父类中的方法。比如在重写父类方法时，还要保留父类方法的功能。"""
class A(object):
    # A 继承自 object 根类
    def show(self):
        print("父类A的方法")

class B(A):
    # 子类重写父类方法
    def show(self):
        # 使用 super() 调用父类方法
        super().show()
        print("子类B的方法")

b = B()
# 当子类方法与父类方法同名时，调用子类方法
b.show()


"""（5）单继承的初始化
在子类对象初始化时，需要给出父类初始化所需的参数，然后使用 super() 调用父类初始化方法去初始化父类的属性。"""


class A(object):
    # A 继承自 object 根类
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

b = B("A","B")
print(b.a)# 这是父类的属性
print(b.b)# 这是子类的属性

"""（6）继承的访问控制
无论在方法的重写，还是初始化时，父类的工作就让父类自己去完成，子类只负责自己部分的实现。

比如：如果在初始化时，想在子类中初始化父类的一个私有属性，这是不能实现的，但是可以调用父类的初始化方法对私有属性进行初始化；"""

class A(object):
    # A 继承自 object 根类
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def show(self):
        print(f"父类中A: {self.a}")
        print(f"父类中B: {self._b}")
        print(f"父类中C: {self.__c}")


class B(A):
    def __init__(self,a,b,c,d):
        # 使用super()调用父类的构造方法，对父类私有属性进行赋值
        super().__init__(a,b,c)
        self.d = d

    def show(self):
        # 使用super()调用父类方法
        super().show()
        print(f"子类中D: {self.d}")

b = B(1,2,3,4)

b.show()

"""（7）多继承
多继承是指一个子类可以同时继承多个父类，此时子类同时拥有多个父类中的属性和方法；"""

class FA(object):
    def fa_show(self):
        print("FA Show Run...")

class FB(object):
    def fb_show(self):
        print("FB Show Run...")

class S(FA, FB):
    def s_show(self):
        print("S Show Run...")


s = S()
s.s_show()
s.fa_show()
s.fb_show()

"""（8） 多继承同名方法查找顺序
如果在一个子类所继承的多个父类中，具有同名方法，那么在调用该方法名的方法时，Python 会使用C3算法实现的 MRO（方法解析顺序）顺序来确定查找的先后顺序，一般情况可以理解成是按继承类的书写顺序。 也就是哪个父类写在括号的前面就调用哪个父类的方法；"""
class FA(object):
    def show(self):
        print("FA Show Run...")

class FB(object):
    def show(self):
        print("FB Show Run...")

# class S(FA,FB):
class S(FB,FA):
    def s_show(self):
        print("S Show Run...")

s = S()
s.s_show()
s.show()

"""（9）多继承初始化
在多继承中，由于有多个父类，每个父类的属性都需要单独初始化，这时 super() 函数只能引用继承书写顺序上的第一个父类，其它的父类是无法通过 super()引用的，所以也就无法利用 super()函数进行初始化。

此时，可以使用直接指定父类名的方式调用该父类中的方法。

此方法也适用于多继承中的方法重写。"""

class FA(object):
    def __init__(self, a):
        self.a = a

class FB(object):
    def __init__(self, b):
        self.b = b

class S(FB, FA):
    def __init__(self, a, b, c):
        FA.__init__(self, a)
        FB.__init__(self, b)
        self.c = c


c = S(1,2,3)
print(c.a)
print(c.b)
print(c.c)

"""6、多态
（1）什么是多态
多态是面向对象编程中三大概念之三，它允许不同的对象对同一个消息作出不同的响应。

简单来说，多态是指同一个方法或操作符在不同的对象实例上可以有不同的行为。这意味着可以通过一个共同的接口或基类引用不同的子类对象，并根据实际的对象类型来调用相应的方法。

多态性的实现通常通过继承和方法重写来实现。在继承关系中，子类可以重写父类的方法，在父类引用子类对象时，调用的实际上是子类重写后的方法。"""

# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")

# 患者
class Patient:
    def needDoctor(self, doctor):
        doctor.cure()

if __name__ == '__main__':
    oldDoctor = Father()
    littleDoctor = Son()
    patient = Patient()

    patient.needDoctor(oldDoctor)
    patient.needDoctor(littleDoctor)

"""（2）鸭子类型
鸭子类型（Duck Typing）是一种动态类型的概念，它源自于“走起来像鸭子、叫声像鸭子、看起来像鸭子，那么它就是鸭子”的观念。

在鸭子类型中，一个对象的适用性不是由它的类或接口决定，而是由它的方法和属性是否与所需的方法和属性匹配来决定。换句话说，只要一个对象具有特定方法和属性，我们就可以将其视为具有相同类型。

举个例子，如果我们需要一个能“叫”的对象，并且某个对象有一个名为quack()的方法，那么我们可以将该对象视为一个“鸭子”，不管它实际上是什么类的对象。换句话说，我们关注的是对象的行为而不是其类型。

鸭子类型在动态语言中特别常见，比如 Python。在 Python 中，不需要显式地继承或实现接口，只要一个对象具有必需的方法和属性，它就可以被认为是某种类型。这使得 Python 具有灵活性和简洁性，可以更自由地处理不同类型的对象。

鸭子类型通常是动态语言的特性，相比于静态类型语言，Python它在编译时没有类型检查。这意味着无法在编译阶段对类型不匹配或缺失方法和属性进行检测，可能会导致运行时错误。"""

# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")

# 兽医
class AnimalDoctor:
    def cure(self):
        print("使用兽医方法进行治疗。。。")

# 患者
class Patient:
    def needDoctor(self, doctor):
        doctor.cure()


if __name__ == '__main__':
    oldDoctor = Father()
    littleDoctor = Son()
    animalDoctor = AnimalDoctor()

    patient = Patient()

    patient.needDoctor(oldDoctor)
    patient.needDoctor(littleDoctor)
    patient.needDoctor(animalDoctor)

"""（3）类型检查
Python 中提供了 isinstance() 和 issubclass() 两个函数，用来对数据进行检查判断。
A、 isinstance(obj, type)
格式：isinstance(obj, type)，判断 obj 对象是否是 Type 指定类型或其父类类型的实例。
B、issubclass(Type1, Type2)
格式： issubclass(Type1, Type2)，判断 Type1 是否是 Type2 的子类；"""