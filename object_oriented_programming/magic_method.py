"""
一、 Python魔法方法介绍
1、什么是魔法函数
所谓魔法函数（Magic Methods），是Python的一种高级语法，它是Python的内置函数，在相应的场景Python会自动去找到相应的魔法函数去处理相应的操作。可以重新Python内置的魔法函数，但是不可以自己定义Python中没有的魔法函数；
特点：
Python中以双下划线(xx)开始和结束的函数，可以重写但不能自定义，如果不重写系统就会使用Python预先定义好的逻辑，如果重新就会实现我们自己需要的逻辑，就像构造方法__init__，如果不重写在实例化的时候也会去调用，但是是不接收任何参数的构造方法，如果想要接收参数那我们就需要去重写这个方法。
调用类实例化的对象的方法时自动调用魔法函数。
在自己定义的类中，可以实现之前的内置函

__new__ 用来创建类并返回这个类的实例
__init__ 把传入的参数用来初始化该实例
__del__ 在对象生命周期调用结束时被调用
__str__ 实现类到字符串的转化，当我们print一个实例化的类时，输出的是类的名称以及实例的ID, __str__可以让我们手动打印对象的一些属性或者是在类里
自己实现一个方法来返回我们需要的信息

"""


"""
2、 魔法函数有什么作用？
魔法函数可以为我们写的类增加一些额外功能。举个简单的例子，我们定义一个“人”的类People，当中有属性姓名name、年龄age。当需要利用sorted函数对一个People的数组进行排序，排序规则是按照name和age同时排序，即name不同时比较name，相同时比较age。由于People类本身不具有比较功能，
所以我们需要重新Python内置的比较函数去实现需要的比较逻辑，比如："""

"""
我们定义一个“人”的类People，当中有属性姓名name、年龄age。当需要利用sorted函数对一个People的数组进行排序，排序规则是按照name和age同时排序，
即name不同时比较name，相同时比较age。由于People类本身不具有比较功能，所以我们需要重新Python内置的比较函数去实现需要的比较逻辑
"""

# __lt__(self, other)
# __lt__函数即less than函数，定义小于符号(<)的行为.


# 当你需要利用sorted函数对一个People的数组进行排序，
# 且排序规则是按照name和age同时排序，即name不同时比较name，相同时比较age.
# 由于People类本身不具有比较功能，所以需要自定义，你可以这么定义People类.

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ":" + str(self.age)

    def __lt__(self, other):
        return self.name < other.name if self.name != other.name else self.age < other.age


res = []
for item in sorted([People("abc", 18), People("abe", 19), People("abe", 12), People("abc", 17)]):
    res.append(str(item))

print("\t".join(res))

# 输出：
# abc: 17
# abc: 18
# abe: 12
# abe: 19

# ps: 当没有__lt__时，会出现错误
# TypeError: '<'
# not supported
# between
# instances
# of
# 'People' and 'People'

"""
二、python常用的魔法方法

1.构造方法

我么最为熟知的基本魔法方法是__init__,我们可以用它来指明一个对象初始化的行为。然而，当我们调用
x=SomeClass()的时候，__init__并不是第一个被调用的方法。事实上，第一个被调用的是__new__,这个
方法才真正的创建了实例。当这个对象的生命周期结束的时候，__del__会被调用。让我们进一步理解这三个方法：


__new__ (cls,[…])

__new__ 是对象实例化时第一个调用的方法，它只取下 cls 参数，并把其他参数传给 __init__ 。__new__ 很少使用，但是也有它适合的场景，尤其是当类继承自一个像元组或者字符串这样不经常改变的类型的时候。
__init__ (self,[…])

类的初始化方法。它获取任何传给构造器的参数（比如我们调用 x = SomeClass(10, ‘foo’) ， __init__ 就会接到参数 10 和 ‘foo’ 。__init__ 在Python的类定义中用的最多。
__del__ (self)

__new__ 和 __init__ 是对象的构造器， __del__ 是对象的销毁器。它并非实现了语句 del x (因此该语句不等同于 x.__del__ ())。而是定义了当对象被垃圾回收时的行为。
当对象需要在销毁时做一些处理的时候这个方法很有用，比如 socket 对象、文件对象。但是需要注意的是，当Python解释器退出但对象仍然存活的时候， __del__ 并不会 执行。 所以养成一个手工清理的好习惯是很重要的，比如及时关闭数据库连接等。

"""

from os.path import join


class FileObject:
    '''文件对象的装饰类，用来保证文件被删除时能够正确关闭。'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # 使用读写模式打开filepath中的filename文件
        self.file = open(join(filepath, filename), 'r+')

    # 当程序运行结束进行垃圾回收的时候会自动调用这个方法
    def __del__(self):
        # 为了确保忘记关闭文件导致内存泄漏，在这里关闭文件并销毁对象
        print("__del__")
        self.file.close()
        del self.file


if __name__ == '__main__':
    file = FileObject(filepath="",filename='del.txt')
    """
    执行完之后会打印__del__
    """



"""   
2、 操作符
使用Python魔法方法的一个巨大优势就是可以构建一个拥有Python内置类型行为的对象。这意味着我们可以避免使用非标准的、丑陋的方式来表达简单的操作。在一些语言中，这样做很常见:

if instance.equals(other_instance):
    # do something
这样做让代码变得冗长而混乱。不同的类库可能对同一种比较操作采用不同的方法名称，这让使用者需要做很多没有必要的工作。运用魔法方法的魔力，我们可以定义方法 __eq__：

if instance == other_instance:
    # do something  
这是魔法力量的一部分，这样我们就可以创建一个像内建类型那样的对象了！ """

"""
1） 比较操作符
Python包含了一系列的魔法方法，用于实现对象之间直接比较，而不需要采用方法调用。同样也可以重载Python默认的比较方法，改变它们的行为。
__cmp__ 是所有比较魔法方法中最基础的一个，它实际上定义了所有比较操作符的行为（<,==,!=,等等），但是它可能不能按照你需要的方式工作（例如，判断一个实例和另一个实例是否相等采用一套标准，而与判断一个实例是否大于另一实例采用另一套）。__cmp__ 应该在 self < other 时返回一个负整数，在 self == other 时返回0，在 self > other 时返回正整数。最好只定义你所需要的比较形式，而不是一次定义全部。如果你需要实现所有的比较形式，而且它们的判断标准类似，那么 __cmp__ 是一个很好的方法，可以减少代码重复，让代码更简洁。
__eq__(self, other)：定义等于操作符(==)的行为。

__ne__(self, other)：定义不等于操作符(!=)的行为。

__lt__(self, other)：定义小于操作符(<)的行为。

__gt__(self, other)：定义大于操作符(>)的行为。

__le__(self, other)：定义小于等于操作符(<)的行为。

__ge__(self, other)：定义大于等于操作符(>)的行为。
"""


class Word(str):
    '''单词类，按照单词长度来定义比较行为'''

    def __new__(cls, word):
        # 注意，我们只能使用 `__new__` ，因为str是不可变类型
        # 所以我们必须提前初始化它（在实例创建时）
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]
            # Word现在包含第一个空格前的所有字母
        return str.__new__(cls, word)
    # def __init__(self, word):
    #     # 注意，我们只能使用 `__new__` ，因为str是不可变类型
    #
    #     # 1.不可变数据类型：数值类型（int、float、bool）、string（字符串）、tuple（元组）
    #     # 2.可变数据类型：list（列表）、dict（字典）、set(集合)
    #     # 3.可变数据类型更改值后，内存地址不发生改变；不可变数据类型更改值后，内存地址发生改变
    #     # __new__在对于不可变数据类型，元类，单例模型中使用，这是因为只要提前将数据或者类实例进行提前
    #     # 处理才能返回，而任何__init__只能进行定义而不能进行处理返回,__init__ 的作用只是刷新和更改刚创建的这个实例对象的状态。
    #     # 所以我们必须提前初始化它（在实例创建时）
    #     if ' ' in word:
    #         print("Value contains spaces. Truncating to first space.")
    #         self.word = word[:word.index(' ')]
    #         # Word现在包含第一个空格前的所有字母
        # return str.__new__(cls, word)

    def __gt__(self, other):
        if len(self) > len(other):
            return f"{self}的长度>{other}"

    def __lt__(self, other):
        if len(self) < len(other):
            return f"{self}的长度<{other}"

    def __ge__(self, other):
        if len(self) >= len(other):
            return f"{self}的长度>={other}"

    def __le__(self, other):
        if len(self) <= len(other):
            return f"{self}的长度<={other}"

    def __eq__(self, other):
        if len(self) == len(other):
            return f"{self}的长度={other}"

    def __ne__(self, other):
        if len(self) != len(other):
            return f"{self}的长度!={other}"


if __name__ == '__main__':

    w1 = Word(" hello")
    w2 = Word("world")
    w3 = Word("  python")
    print(w3 > w1)
    print(w2 < w3)
    print(w1 >= w2)
    print(w1 <= w2)
    print(w1 == w2)
    print(w3 != w1)
    """
    输出：
    python的长度>hello
    world的长度<python
    hello的长度>=world
    hello的长度<=world
    hello的长度=world
    python的长度!=hello
    """

"""除了使用重写需要的比较方法之外，还可以使用@total_ordering装饰器重写部分比较方法而实现所有的比较方法；
被重写的类必须重写__eq__以及其他方法（__ne__,__lt__,__ge__,__gt__,__le__）中的一个。@total_ordering
会自动实现没有重写的其他比较功能"""

from functools import total_ordering


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


@total_ordering
class StudentOrdering:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # 重写相等比较方法
    def __eq__(self, other):
        return self.grade == other.grade

    # 重写小于比较方法
    def __lt__(self, other):
        return self.grade < other.grade


if __name__ == '__main__':
    # 非比较类进行比较直接报错
    student1 = Student("Alice", 85)
    student2 = Student("Bob", 75)
    print(student1 < student2)  # TypeError: '<' not supported between instances of 'Student' and 'Student'

    # 比较类
    student1 = StudentOrdering("Alice", 85)
    student2 = StudentOrdering("Bob", 75)
    student3 = StudentOrdering("Charlie", 85)
    print(student1 < student2)  # False
    print(student1 > student2)  # True
    print(student1 == student3)  # True
    print(student1 <= student3) # True
    print(student3 >= student2) # True
    print(student1 != student3) # False


"""
（2） 数值操作符
就像我们可以使用比较操作符来比较类的实例，也可以定义数值操作符的行为，把数值操作符分为5类："""


"""
一元操作符，
常见算数操作符，
反射算数操作符，
增强赋值操作符，
类型转换操作符，

一元操作符
一元操作符只有一个操作符。

__pos__(self)：实现取正操作，例如 +some_object。

__neg__(self)：实现取负操作，例如 -some_object。

__abs__(self)：实现内建绝对值函数 abs() 操作。

__invert__(self)：实现取反操作符 ~。

__round__(self， n)：实现内建函数 round() ，n 是近似小数点的位数。

__floor__(self)：实现 math.floor() 函数，即向下取整。

__ceil__(self)：实现 math.ceil() 函数，即向上取整。

__trunc__(self)：实现 math.trunc() 函数，即距离零最近的整数。

*常见算数操作符
算术操作符就是算术运算符，比如+、-、*、/等；

__add__(self, other)：实现加法操作。

__sub__(self, other)：实现减法操作。

__mul__(self, other)：实现乘法操作。

__floordiv__(self, other)：实现使用 // 操作符的整数除法。

__div__(self, other)：实现使用 / 操作符的除法。

__truediv__(self, other)：实现 true 除法，这个函数只有使用 from **future** import division 时才有作用。

__mod__(self, other)：实现 % 取余操作。

__divmod__(self, other)：实现 divmod 内建函数。

__pow__：实现 ** 操作符。

__lshift__(self, other)：实现左移位运算符 << 。

__rshift__(self, other)：实现右移位运算符 >> 。

__and__(self, other)：实现按位与运算符 & 。

__or__(self, other)：实现按位或运算符 | 。

__xor__(self, other)：实现按位异或运算符 ^ 。

*反射算数运算符
反射算数运算的概念请自行百度；

__radd__(self, other)：实现反射加法操作。

__rsub__(self, other)：实现反射减法操作。

__rmul__(self, other)：实现反射乘法操作。

__rfloordiv__(self, other)：实现使用 // 操作符的整数反射除法。

__rdiv__(self, other)：实现使用 / 操作符的反射除法。

__rtruediv__(self, other)：实现 true 反射除法，这个函数只有使用 from __future__ import division时才有作用。

__rmod__(self, other)：实现 % 反射取余操作符。

__rdivmod__(self, other)：实现调用 divmod(other, self) 时 divmod 内建函数的操作。

__rpow__：实现 ** 反射操作符。

__rlshift__(self, other)：实现反射左移位运算符 << 的作用。

__rshift__(self, other)
实现反射右移位运算符 >> 的作用。

__rand__(self, other)：实现反射按位与运算符 & 。

__ror__(self, other)：实现反射按位或运算符 | 。

__rxor__(self, other)：实现反射按位异或运算符 ^ 。

*增强赋值运算符
所谓增强赋值运算就是同时使用了赋值符合运算符，比如：

x = 5
x += 1 # 也就是 x = x + 1
这些方法都应该返回左侧操作数应该被赋予的值（例如， a += b iadd 会返回 a + b ，这个结果会被赋给 a ）,下面是方法列表：

__iadd__(self, other)：实现加法赋值操作。

__isub__(self, other)：实现减法赋值操作。

__imul__(self, other)：实现乘法赋值操作。

__ifloordiv__(self, other)：实现使用 //= 操作符的整数除法赋值操作。

__idiv__(self, other)：实现使用 /= 操作符的除法赋值操作。

__itruediv__(self, other)：实现 true 除法赋值操作，这个函数只有使用 from **future** import division 时才有作用。

__imod__(self, other)：实现 %= 取余赋值操作。

__ipow__：实现 **= 操作。

__ilshift__(self, other)：实现左移位赋值运算符 <<= 。

__irshift__(self, other)：实现右移位赋值运算符 >>= 。

__iand__(self, other)：实现按位与运算符 &= 。

__ior__(self, other)：实现按位或赋值运算符 | 。

ixor(self, other)：实现按位异或赋值运算符 ^= 。

*类型转换操作符
也就是在定义数据类型以及数据类型转换时用到的魔法函数：

__int__(self)：实现到int的类型转换。

__long__(self)：实现到long的类型转换。

__float__(self)：实现到float的类型转换。

__complex__(self)：实现到复数的类型转换。

__oct__(self)：实现到八进制数的类型转换。

__hex__(self)：实现到十六进制数的类型转换。

__index__(self)：实现当对象用于切片表达式时到一个整数的类型转换。如果你定义了一个可能会用于切片操作的数值类型，你应该定义 index。

__trunc__(self)：当调用 math.trunc(self) 时调用该方法， trunc 应该返回 self 截取到一个整数类型（通常是long类型）的值。

__coerce__(self)：该方法用于实现混合模式算数运算，如果不能进行类型转换， coerce 应该返回 None 。反之，它应该返回一个二元组 self 和 other ，这两者均已被转换成相同的类型。


"""



































