"""python 内置库 json
JSON
JSON是用于存储和交换数据的语法，是一种轻量级的数据交换格式
使用场景
** 接口数据传输
** 序列化
** 配置文件
JSON 结构
键值对形式
数组形式"""

# python 与 JSON 数据类型对应
# Python	    JSON	说明
# dict	        object	字典
# list，tuple	array	序列
# str	        string	字符串
# int，float	number	数字类型
# True	        true	布尔值True
# False     	false	布尔值False
# None	        null	空值

"""JSON 库
可以从字符串或文件中解析JOSN
该库解析JSON后将其转为 Python 字典或列表
常用方法
dumps()：将Python对象编码成JSON字符串
loads()：解码JSON数据，该函数返回Python对象
dump()：Python对象编码，并将数据写入json文件中
load()：从json文件中读取数据并解码为Python对象"""

import json
# 定义python结构
dd = {
    'a':1,
    'b':[1,2,3],
    'c':True,
    'd':False,
    'e':'this',
    'f':None,
    'g':'中问的'
}
print("type----------->", type(dd))
# 将python对象编码为 json字符串
json_data = json.dumps(dd, ensure_ascii=False, indent=4)
# 参数：ensure_ascii若有中文需要是false，默认是true，indent控制缩进的空格数量，默认None没有
print(json_data)
print("type_json_data------>", type(json_data))
data1 = ''' {
    "a": 1,
    "b": [
        1,
        2,
        3
    ],
    "c": true,
    "d": false,
    "e": "this",
    "f": null,
    "g": "中问的"
}'''
print("type_json_data------>", type(data1))

# 以上才是转化为json字符串的正确表达方式


# 定义 json字符串
json2 = '''{"a": 1, "b": [1, 2, 3], "c": true, "qq": false, "rr": "this", "ww": null}'''
# 将json字符串编码为 python 对象
pyd=json.loads(json2)
print(pyd)
# 结果是：{'a': 1, 'b': [1, 2, 3], 'c': True, 'qq': False, 'rr': 'this', 'ww': None}

# 把python对象转化为json字符串写入json文件
import json
dd1 = {
    'a':1,
    'b':[1,2,3],
    'c':True,
    'd':False,
    'e':'this',
    'f':None,
    'g':'中问的'
}
with open('data.json', 'w', encoding="utf8") as ff:
    json.dump(dd1, ff, ensure_ascii=False)
    # ff.write(json_data)
    ff.close()

# 读取json文件并转为python对象
with open('data.json', 'r', encoding='utf-8') as fff:
    cc = json.load(fff)
    print(cc)
# 结果是： {'a': 1, 'b': [1, 2, 3], 'c': True, 'd': False, 'e': 'this', 'f': None}