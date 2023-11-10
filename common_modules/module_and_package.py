"""一、模块
1、什么是模块
Python的模块是用于组织、封装和重用代码的文件，一个Python文件就是一个模块。

一个模块中可以包含变量、函数、类和其他Python语句，它允许将代码逻辑划分为独立的单元，并提供了一种组织代码的方式，使代码更加模块化和易于维护。

Python的模块可以分为三类，非别是内建模块、第三方模块和自定义模块。

2、模块的导入
Python 可通过模块导入引用其它模块中的数据，提供了 import 和 from - import 两种导入方式。
（1） import 导入
Python中使用 import 关键字来导入模块，导入模块后，在当前文件中做为一个对象使用，可以通过 . 来引用模块中定义的函数、变量或类等。"""

import math
result = math.sqrt(25)
print(result)

# 如果被导入的模块名比较长，在使用时会不太方便，也可以使用 as 为模块指定一个别名，一旦指定了别名，原模块名就不能使用了。
import math as m
result = m.sqrt(25)
print(result)

# (2) from - import 导入
# from module_name import object_name 语法，从模块中导入特定的对象，这样可以直接使用对象名，无需使用模块名前缀
from math import sqrt

result = sqrt(25)
print(result)

"""二、包
1、包的概念
在Python中，包 (package) 是用于组织和管理模块 (Module) 的一种层级结构。包是一个特殊的目录，其中包含了一个名为 __init__.py 的文件，用于标记这个目录是一个包。包可以包含其他子包和模块，形成多级层次结构，方便组织和复用代码。
2、 package 用途
组织代码：包可以将相关的模块组织在一起，使得代码结构更加清晰，有助于团队协作和维护。
避免命名冲突：Python的模块是全局的，当不同的模块中定义了相同名称的函数或变量时，可能会引起命名冲突。使用包可以将模块放在不同的包中，避免当不同的模块中定义了相同名称的函数或变量时冲突。
模块复用：包可以作为一个单元来导入和使用，使得代码在不同项目中的复用更加容易。
隐藏内部实现：包可以将一些内容实现隐藏起来，只暴露外部接口，提供更好的封装性。
3、package导入
当前有包组织结构如下：

Project
    |
    |--- mp 
    |    |
    |    |--- __init__.py
    |    |--- mm.py 
    |    |    |
    |    |    |--- show()
    |    |--- nn.py
    |    |    |
    |    |    |--- info()
    |--- main.py """

# (1) 使用import直接导入包中的指定模块
import mp.mm
mp.mm.show()

import mp.nn as nn
nn.info()

# (2)使用from-import 导入包内指定模块或包内指定模块内的成员
from mp import mm
mm.show()

# 导入包内指定模块中的成员
from mp.mm import *
show()


"""4、 __init__.py
__init__.py文件是包的初始化文件，该文件是是区别包与文件夹的关键。

当使用 from-import方式导入时，可以通过在文件中添加魔法属性 __all__ 属性来设置包中哪些模块可以被导入和使用。"""
# 在 __init__.py 中添加下面代码
__all__ = ["mm"]

# main.py中的代码
from mp import *
# 此时只能使用 __all__ 中指定的mm模块，nn 模块不能使用
mm.show()
