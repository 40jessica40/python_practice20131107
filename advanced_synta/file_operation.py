"""文件操作
在程序中操作文件和使用图形界面操作文件的过程基本一致，都要进行找到文件位置，打开文件，读写文件，关闭文件等操作。

1、打开文件
Python 使用 open 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

完整格式：
open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

简化格式：open(filename, mode='r', encoding=None)；
filename: 必需，指定打开文件的路径（相对或者绝对路径）；
mode: 可选，文件打开模式，默认为r只读模式；
encoding: 一般使用 utf8；
mode参数常见下表
r 只读
w 写
a 追加
b 二进制的模式 主要是用于图片等的方式
t 文本模式（默认）


2、关闭文件
文件在操作完以后，需要将其关闭，close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。
close() 方法允许调用多次。
格式：fileObject.close()；

3、写入文件
fileObject.write( str )： 用于向文件中写入指定字符串。如果文件打开模式为b ，则要将字符串转换成 bytes 类型的二进制字符串,函数返回成功写入数据的长度。
"""
import sys

with open("index.html", mode='w', encoding="utf8") as index:
    index.write("<h1>写入文章的标题<h1>")
    index.write("\h")
    index.write("<p>写入文章的内容。。。<p>")


# file = open("index.html", "w")
# # 写入数据
# result1 = file.write("<h1>文件写入标题</h1>")
# result2 = file.write("\n")
# result3 = file.write("<p>文件写入内容。。。。。。</p>")
# print("result1=", result1)# result1= 15
# print("result2=", result2)# result2= 1
# print("result3=", result3)# result3= 19

"""fileObject.writelines(seq)：用于向文件中写入一序列的字符串。这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
# 注意：不要被方法名所迷惑，如果每个元素独占一行，需要在数据后指定换行符 \n 。"""

import os

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)

print("The current file is at: " + file_path)
print("The directory of the current file is at: " + dir_path)

datas = ['AAAAA\n',"BBBBBBBBBB\n", "CCCCCCCCCC\n", "DDDDD\n", "FFFFFFFFFFF\n","GGGGGGGGGGG\n"]
try:
    file = open(dir_path+".\index.html", 'w')
    print(" dir_path----->", dir_path+"\index.html")
    r = file.writelines(datas)
    file.close()
except:
    print("异常")

"""
4、读取文件
fileObject.read(size=-1)：用于从文件读取指定的字节数，如果未给定或为负则读取所有。
注意光标的位置，连续读取文件没有关闭的时候，光标会随着读取而向后移动，不会回到默认起始位置；"""

file = open(dir_path+".\index.html", 'r')
result1 = file.read(10)
print("result1------------->", result1)
file.close()


file = open(dir_path+".\index.html", 'r')
result2 = file.read()
print("result2-------------->", result2)
file.close()


"""fileObject.readline(size=-1)： 用于从文件读取整行，包括 \n 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 \n 字符。
该方法默认读取一行，如果指定了长度，会读取这一行中的给定长度，并且如果文件不关闭，光标也不会回到默认起始位置，再次读取会从光标所在位置读取这一行剩下的内容；"""

file = open(dir_path+".\index.html", 'r')
result3 = file.readline(10)
print("result3-------------->", result3)
file.close()

file = open(dir_path+".\index.html", 'r')
result4 = file.readlines()
print("result4-------------->", result4)

#
# import os
#
# file_path = os.path.abspath(__file__)
# dir_path = os.path.dirname(file_path)
#
# with open(dir_path+r"\advanced_synta\mlower.jpg", 'r', encoding="utf8") as file:
#     data = file.read()
#     binary_content = data.encode()
#     print("------------------->", binary_content)
#
# # 将二进制数据写入文件
# with open("example.dat", "wb") as binary_file:
#     binary_file.write(binary_content)
#
# # 从二进制文件中读取二进制数据
# with open("example.dat", "rb") as binary_file:
#     binary_content = binary_file.read()
#
# # 将二进制数据解码为文本
# text_content = binary_content.decode()
#
# # 将文本数据写入文件
# with open("example.txt", "w") as text_file:
#     text_file.write(text_content)


# 5、作业
# 作业要求
# 编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来
"""
作业要求
编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来
"""

def file_write(filename,msg,mode='a',encoding='utf8'):
    """
    文件写入方法，支持写入：字符串和一序列的字符串
    :param filename:文件名称
    :param msg:写入内容
    :param mode:文件打开方式
    :param encoding:内容编码
    :return:
    """
    file = open(filename,mode,encoding=encoding)
    if isinstance(msg,str):
        # 写入字符串类型
        file.write(msg)
    elif isinstance(msg,list):
        # 写入序列字符串
        file.writelines(msg)
    else:
        # 关闭文件
        file.close()
        raise Exception("msg type erroe")
     # 关闭文件
    file.close()

def file_read(filename,size=-1,mode='r',encoding='utf8'):
    """
    读取文件，支持读取一行或所有
    :param filname: 文件名
    :param size: -1表示读取所有，
    :param mode: 文件打开方式
    :param encoding: 内容编码
    :return:
    """
    file = open(filename, mode, encoding=encoding)
    if size == -1:
        # 读取所有内容
        content = file.read()
        file.close()
        return content
    elif size == 1:
        # 读取一行
        content = file.readline()
        file.close()
        return content
    else:
        # 关闭文件
        file.close()
        raise Exception("size error")


if __name__ == '__main__':
    # 写入文件
    filename = 'demo1.txt'
    msg = "霍格沃兹测试开发学社\n"
    file_write(filename, msg)
    # msg = ["AAAAAAAAAAAA\n","BBBBBBBBBBBB\n","CCCCCCCCCCCC\n","DDDDDDDDDDDD\n"]
    # file_write(filename, msg)

    # 读取文件
    line = file_read(filename,1)
    print(line)
    all = file_read(filename)
    print(all)