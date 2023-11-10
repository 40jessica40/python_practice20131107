"""异常处理
编写程序时，即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为异常，大多数异常不会被程序处理，程序会中断运行，并抛出异常信息。

如果不想发生异常时，程序被中断执行，可以编写程序处理选定的异常。

1、异常捕获
Python 使用 try/except语句捕捉异常。

try/except 语句用来检测 try 语句块中的错误，从而让 except 语句捕获异常信息并处理。

如果你不想在异常发生时结束你的程序，只需在try里捕获它。"""

# file = open("data.txt","w")
# try:
#     # 写入数据时可能会有问题
#     file.write("写入的数据")
# except IOError as err:
#     print("文件不能写入", err)
#
# file.close()
#

"""2、捕获多个异常
如果一段代码可能会发生多种异常，并想在程序中都想处理，可以使用多个 except 分别捕捉异常。

可以捕捉 Exception异常类型来处理所有的异常，如果有多个时， Exception必须放在最后捕捉该异常，否则无法处理到其它异常。"""
import os



file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)

print(dir_path)

file = open(dir_path+"\demo.txt","r")
try:
    # 写入数据时可能会有问题
    # file.write("写入的数据")
    # print(a)
    print(3 / 0)
    # print([][10])
    # print("hello" + 100)
except IOError as err:
    print("文件不能写入", err)
except NameError:
    print("标识符没有定义")
except ZeroDivisionError:
    print("除数不能为0")
except IndexError:
    print("下标越界了")
except Exception:
    print("程序运行出错，请检查代码")
file.close()

"""3、else操作
Python 使用 else 在处理代码无异常时的后续操作。"""

try:
    n = input("请输入一个数字:")
    num = int(n)
except Exception:
    print("元素无法转换为数字")
else:
    print("转换后成功",num)

"""4、finally操作
Python 使用 finally 处理无论异常是否发异，都要执行的代码，一般用来完成清理工作。"""

try:
   file = open("data.txt","r")
   # file.write("A")
except Exception:
    print("文件操作报错")
finally:
    print("文件已关闭")
    file.close()

"""5、作业
作业要求
编写一个Python程序，可以执行加法、减法、乘法和除法操作。用户可以输入两个数字和运算符，然后计算并输出结果。实现计算器的功能（+、-、*、/），并处理异常情况，比如：输入的不是数字、除数为0等。"""
#


def operation(number_1, symbol, number_2):
    match symbol:
        case "+":
            return number_1 + number_2
        case "-":
            return number_1 - number_2
        case "*":
            return number_1 * number_2
        case "/":
            if number_2 == 0:
                raise Exception("除数不能为0！")
            else:
                return number_1 / number_2
        case _:
            raise Exception(f"您输入的运算符{symbol}有误!")


def calculator():
    try:
        number_1 = int(input("请输入第一个数字：\n"))
        symbol = input("请输入+ - * /其中一个运算符：\n")
        number_2 = int(input("请输入第二个数字：\n"))
    except Exception:
        print("请输入整数数字！")
    else:
        try:
            result = operation(number_1, symbol, number_2)
        except Exception as err:
            print(err)
        else:
            print(f"您输入的计算结果为：{result}")


if __name__ == '__main__':
    calculator()
