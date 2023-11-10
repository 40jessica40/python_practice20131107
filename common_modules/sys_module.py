"""#第四部分 sys模块
#4.1、sys常用属性
sys指的是解释器系统，os指的是操作系统
#sys.argv获取命令行参数列表，包括脚本名称和传递给脚本的其他参数"""

import sys
script_name = sys.argv
print(script_name)
if len(script_name)<3:
#代码运行之前在Run/Debug configurations的parameters中输入参数，可以输入多个，每个参数之间用空格分隔，如输入127.0.0.1 8080
# 则代码运行时则认为该脚本执行时外部还传递了2个参数（127.0.0.1和8080）配置方法如下截图1和2
    print("请配置服务器的IP和端口")
else:
    print(f"WebServer start on {sys.argv[1]} {sys.argv[2]}")


#sys.version获取当前Python解释器的版本信息
#sys.version_info获取当前Python解释器的版本信息,以元祖形式表示详细的版本号信息

import sys
print(f"当前解释器的版本信息为：{sys.version}")
print(type(sys.version))
print(sys.version_info)
print(sys.version_info[0],sys.version_info[1],sys.version_info[2])


#sys.platform获取当前系统运行的操作系统名称
print(sys.platform)
print(sys.modules)


#返回已导入的模块信息，返回一个字典
for items_key,items_value in sys.modules.items():
    print(f"模块名：{items_key},模块对象：{items_value}")

#sys.path获取模块搜索路径列表，用于指定python解释器搜索模块的路径
print(sys.path)


#4.2 sys常用方法
import time
#获取编码方式
print(sys.getdefaultencoding())
#运行时退出

import time
n = 0
while(True):
    time.sleep(1)
    n += 1
    print(n)
    if n ==5:
        sys.exit()