"""第五部分 os模块
#python的内置库os提供了与操作系统交互的函数，允许您与操作系统进行各种操作，如文件和目录操作，环境变量访问，进程管理等。
#5.1 路径操作"""

import os
#获取当前路径
print("当前路径", os.getcwd())
#切换到指定路径下
os.chdir("/Users/PycharmProjects/pythonProject2/my_dir")
#path相关的操作：返回绝对路径
path = os.getcwd()
path1 = path + "/pactice.py"
print(path1)

#path相关的操作：返回指定路径的文件名
print("指定文件的文件名",  os.path.basename(path))

#path相关的操作：返回指定路径的目录
print('目录为', os.path.dirname(path))

#path相关的操作：将指定路径分隔成文件名和路径，并以一个元祖的形式储存
import os
path = os.getcwd()
path1 = path + "/pactice.py"
print(os.path.split(path1))

#path相关操作：将多个路径连接起来形成一个路径
str1, str2 = os.path.split(path)
path_new = os.path.join(str1, str2)

#path相关操作：判断一个路径是否存在

print("路径存在吗？", os.path.exists(path))
#path相关操作：判断是否是目录
print("是否是目录", os.path.isdir(path))
#path相关操作：判断是否是文件

print("判断是否是文件", os.path.isfile)
#path相关操作：获取文件大小
print("获取文件大小", os.path.getsize(path))


#5.2 目录和文件操作
#列出当前目录内容
import os
print(os.listdir)

#创建一个新目录
import os
os.mkdir('aa')
open('aa/test.txt', 'w')

#递归创建多级目录
import os
os.makedirs('a/b/c/d')

#删除目录
import os
os.rmdir('aa')
#给文件或目录重命名
import os
os.rename('mp','mp_new')
#删除文件
import os
os.remove('aa/test.txt')

#其他操作
#获取系统名称,windows系统值为nt，在linux,macos系统中值为：posix
import os
print('系统名称为：', os.name)

#获取系统分隔符
import os
print('系统分隔符为：', os.sep)

#更改文件权限模式，mode是权限模式，通常用八进制表示，如0o755
import os
file_path = 'C:/Users/dell/PycharmProjects/python_practice20231107/common_modules/ff.txt'
os.chmod(file_path, 0o753)
