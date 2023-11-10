import random

#1、随机获取一个数
#随机获取[0，1)的浮点数
r= random.random()
print(r)

#随机获取[a,b]之间的一个整数
r = random.randint(1, 100)
print(r)

#随机获取[a,b]之间的一个浮点数
r = random.uniform(1,100)
print(r)

#2、随机获取指定列表或元祖,集合中的一个元素
import random
list = [1,3,4,6,8,9,30]
r= random.choice(list)
r1= random.choices(list, k=3)
print(r)
print(r1)

t = tuple(list)
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号( )，列表使用方括号[ ]，逗号隔开
# 一个元素的元组tup1 = (50,)
print(t)
# for i in [1, 4]:
for i in range(9):
    print("i------>", i)
    r = random.choice(t)
    print("r---->", r)
r2 = random.choices(t)
print(r2)

import random
print(random.choices(range(1, 100), k=10))
# 返回10个随机的1到100之间的整数


#3、打乱指定列表或元祖的顺序
list = [1,2,4,5,5,6,7,8,9,10]
r = random.shuffle(list)
t = tuple(list)
print("t------>", t)
# mutableSequnence 要求的是可变的
# r1 = random.shuffle(t)


#练习，实现一个公司的年会抽奖程序
#需求：1、从文件中读取参与抽奖的员工名字；2、抽奖：分别按顺序抽取锦鲤精，一，二，三等奖；3，每次抽完奖都需要将已经中奖的员工名字从抽奖名单中移除
import random
if __name__ == '__main__':
    name_file = "C:/Users/dell/PycharmProjects/python_practice20231107/common_modules/ff.txt"
    jiangxiang = ['锦鲤奖','一等奖','二等奖','三等奖']
    name_list = []
    # 读取参与抽奖的员工姓名
    try:
        file1 = open(name_file,'r')
        name_list = file1.readlines()
    except Exception as err:
        print("文件读取错误，请检查参与抽奖员工姓名文件是否存在，详细报错信息如下：", err)
    else:
        file1.close()

    while(True):
    # 抽奖
        try:
            random.shuffle(name_list)
            xinyuner = random.choice(name_list)
            item = jiangxiang[0]
            print(f'获得{item}的幸运儿是：', xinyuner)
        #移除已获奖人员名单
            name_list.remove(xinyuner)
            jiangxiang.remove(item)
        except Exception as err1:
            print("所有员工都中奖啦！")
            break
        else:
            Flag = input("请输入Y或y继续抽奖，其他字符表示退出抽奖程序：")
            if Flag != 'Y' and Flag != 'y':
                print("退出抽奖程序，欢迎下次再来！")
        break