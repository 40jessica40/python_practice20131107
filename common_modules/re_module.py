# 7.1、正则表达式符号
# 四大金刚：match search findall sub split

# 1. match
# （1）匹配字符串
# re.match()必须从字符串开头匹配！match方法尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。主要参数如下：
import re

# re.match(pattter, string)
a = re.match("test", "testji")
print(a)
print(a.group())
print(a.span())
print(re.match('test', "atrenmmedd"))
# （2）单字符匹配
# .  匹配任意一个字符（除了\n）
# [] 匹配[]中列举的字符
# \d 匹配数字，即0-9
# \D 匹配非数字
# \s 匹配特殊字符，如空白，空格，tab等
# \S 匹配非空白
# \w 匹配单词字符
# \W 匹配非单词字符

# .  匹配任意一个字符（除了\n）
import re
a = re.match("..", "rejdjdj")
print(a.group())
b= re.match("ab.", "hdjfhdk")
print(b)

# \d 匹配数字
#  一个\d代表一个数字。开头没匹配到，即使字符串其他部分包含需要匹配的内容，.match也会返回none
print(re.match('\d\d\d', "1239kkdk"))
print(re.match('\d', "kkdk"))
print(re.match('\d\d', "19rrr"))

# \D 匹配非数字
# 开头没匹配到，即使字符串其他部分包含需要匹配的内容.match也会返回none
print(re.match('\D', "1JDLKFLDLjdjd"))
print(re.match('\D\D', "1JDLKFLDLjdjd"))
print(re.match('\D\D\D', "*kwkkJDLKFLDLjdjd"))
print(re.match('\D\D\d', "*kwkkJDLKFLDLjdjd"))

# \s 匹配特殊字符，如空白，空格，tab等
print(re.match("\s\s\d", "  9lll"))
print(re.match("\s\s\d", "9lll"))

# \S 匹配非空白
print(re.match("\S\s\D\D\d", "w ee1kdlld"))
print(re.match("\S\s\D\D\d[a-z1-9]", "w ee1a9"))
print(re.match("\S\s\D\D\d[a-z1-9]", "w ee10"))

# \w 匹配单词、字符，如大小写字母，数字，_ 下划线
print(re.match("\w\w\w.", "4_wlll"))
print(re.match("\w\w\S.", "4_wlll"))
print(re.match("\w\w\d.", "4_wlll"))

# \W 匹配非单词字符
print(re.match("\W\W\d...", "  1111999"))
print(re.match("\W\W\d...", "_ 1111999"))
print(re.match("\W\W\d...", "- 1\n11999"))

# [ ] 匹配[ ]中列举的字符
# 只允许出现[ ]中列举的字符
print(re.match("[a-q0-4].", "a\n343343"))
print(re.match("[a-z0-4].", "7\n343343"))
print(re.match("[a-z0-4].", "1343343"))

# []匹配其中的任意一个,[]只代表一个
print(re.match('[1223]', "122323"))
print(re.match('12[w120]', "122323"))
print(re.match('12[\n120]', "12\n323"))

# [^123]不匹配123中的任意一个
print(re.match('123[^123]', "1231555"))
print(re.match('123[^123]', "1234555"))
print(re.match('123[^123]', "123\n555"))


# [a-z3-5] 匹配a-z或者3-5中的字符
print(re.match('12[a-z1-9]', "12a000000"))

# （3）表示数量
# 像上面写的那些都是匹配单个字符，如果我们要匹配多个字符的话，只能重复写匹配符。这样显然是不人性化的，所以我们还需要学习表达数量的字符

# * 匹配前一个字符出现0次或者无限次，即可有可以无
# + 匹配前一个字符出现1次或者无限次，即至少有一次
# ？匹配前一个字符出现1次或者0次，即要么一次要么没有
# {m}匹配前一个字符出现m次
# {m,}匹配前一个字符至少出现m次
# {m,n}匹配前一个字符至少出现m到n次


# * 出现0次或无数次
print(re.match("1*", "11111"))
print(re.match("1*[001]", "11111"))
print(re.match(".*", "12dff3ddd"))

# + 至少出现一次
print(re.match("1+", "11111"))
print(re.match("1+[001]", "111110"))
print(re.match(".+", "\n989hj"))
print(re.match(".+", "989hj"))

# ？匹配前一个字符出现1次或者0次，即要么一次要么没有
print(re.match("1?", "11111"))
print(re.match("1?[001]", "111110"))
print(re.match(".?", "\n989hj"))
print(re.match(".?", "989hj"))

# {m}匹配前一个字符出现m次
print(re.match("1{2}", "11111"))
print(re.match("1{3}[001]", "111110"))
print(re.match(".{2}", "\n989hj"))
print(re.match(".{6}", "9999989hj"))
print(re.match(".{6}", "99999989hj4545"))

# {m,}匹配前一个字符至少出现m次
print(re.match("1{2,}", "11111"))
print(re.match("1{3,}[001]", "111110"))
print(re.match(".{2,}", "\n989hj"))
print(re.match(".{6,}", "989hj"))
print(re.match(".{6,}", "98955hj"))

# {m,n}匹配前一个字符至少出现m到n次
print(re.match("1{2,2}", "11111"))
print(re.match("1{3,6}[001]", "111110"))
print(re.match(".{2,6}", "\n989hj"))
print(re.match(".{6,7}", "989hj"))
print(re.match(".{6,10}", "98955hj"))


# （4）匹配边界
# ^ 匹配字符串开头
# $ 匹配以字符串结尾
# \b 匹配一个单词的边界
# \B 匹配一个非单词的边界

# ^ 匹配开头字符
# 定义整个字符串必须以指定字符开头
import re
print(re.match("^23k", "23koodo"))
print(re.match("^23k", "23oodo"))
print(re.match("^2.", "23oodo"))
print(re.match("^2.", "33oodo"))

# $ 匹配结尾字符
# 定义整个字符串必须以指定字符串结尾
print(re.match("8*k$", "8jdkaljgdak"))
print(re.match("8*k$", "88888888888k"))
print(re.match("8*k", "8jdkaljgdaku"))

# \b 匹配一个单词的"边界"
# \b：表示字母数字与非字母数字的"边界"，非字母数字与字母数字的"边界"。即下面ve的右边不能有字母和数字,下划线
print(re.match(r'.*ve\b', "ve.jdkd999"))
print(re.match(r'.*ve\b', "ve_jdkd999"))
print(re.match(r'.*ve\b', "ve*jdkd999"))
print(re.match(r'.*ve\b', "ve()jdkd999"))
print(re.match(r'.*ve\b', "ve1dkd999"))
print(re.match(r'.*ve\b', "vejdkd999"))
print(re.match(r'.*ve\b[12]', "ve.1kd999"))
print(re.match(r'.*ve\b[12]', "ve.dkd999"))


# \B 匹配非单词(字母或者数字)"边界"，ve的旁边需要有字母，数字和下划线
print(re.match("ve\B.123*", "ve_123333"))
print(re.match("ve\B", "ve1r23333"))
print(re.match("ve\B", "verr123333"))
print(re.match("ve\B", "ve"))


# （5）匹配分组

# | 匹配左右任意一个表达式
# 只要|两边任意一个表达式符合要求就行
import re
print(re.match(r'\d[1-9]|\D[a-z]','2233'))  #匹配|两边任意一个表达式
print(re.match(r'\d[1-9]|\D[a-z]','asrr'))

# (ab) 将括号中字符作为一个分组
# ()中的内容会作为一个元组字符装在元组中
import re
a = re.match(r'<h1>(.*)<h1>', "<h1>你好啊<h1>")
print(a)
print(a.group())
print(a.groups())
print('----------------------')
b = re.match(r'<h1>(.*)(<h1>)', '<h1>你好啊<h1>')
print(b)
print(b.groups())
print(b.group(0)) # print(b.group())
print(b.group(1))
print(b.group(2))


# 2.search
# 和match差不多用法，从字符串中进行搜索,不像match一样要从开头的时候就要开始匹配

import re
print(re.match(r'\d\d','123test123test'))
print(re.search(r'\d\d','123test123test'))

# 3.findall
# 从字面意思上就可以看到，findall是寻找所有能匹配到的字符，并以列表的方式返回
import re
print(re.search(r'test','123test123test'))
print(re.findall(r'test','123test123test'))  #以列表的方式返回



#re.s 和re.S

# findall中另外一个属性re.S
# 在字符串a中，包含换行符\n，在这种情况下
# 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始。
# 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
#  如下要寻找test.*123的数据，因为test和123在不同的行，如果没加re.s的话，他会在每一个进行匹配查找而不是将字符串作为一个整体进行查找
import re
a = '''testdfdfdfdf123
23234343123'''
b = '''testdfdfdfdf
23234343123'''
print(re.findall(r"test.*123", a))
print(re.findall(r"test.*123", b))
print(re.findall(r"test.*123", a, re.S))

# 4.sub
# sub(要替换的数据，替换成什么，要替换的数据所在的数据)
import re
print(re.sub("python", 'php', "python是世界上最好的编程语言"))

# 5.split
import re
s= "itnnie,djfjd;dfdj:dkf-jdkf;html"
print(re.split(r',', s))
print(re.split(r",|;|:|-", s))
print(re.split(r",|%", s))

# 贪婪与非贪婪
# python里的数量词默认是贪婪的，总是尝试尽可能的匹配更多的字符。python中使用?号关闭贪婪模式
import re
print(re.match("aa\d+", "aa3434"))
print(re.match("aa\d+?", "aa3434"))
s = "this is a number 2333-34-333-22"
# 1.贪婪模式
print(re.match(r'(.*)(\d+-\d+-\d+-\d)', s).groups())
# 结果为('this is a number 233', '3-34-333-2')
# 因为+它会尽可能多的进行匹配，\d，只需要一个3就能满足，所以前面就尽可能多的匹配

# 2.关闭贪婪模式
# 在数量词后面加上 ?，进入非贪婪模式，尽可能少的进行匹配
print(re.match(r'(.*?)(\d+-\d+-\d+-\d)', s).groups())

# 案例
# 1. 匹配手机号
# 要求，手机号为11位，必须以1开头，且第二个数字为35678其种一个
import re
num = '132900933456'
print(re.match("^1[35678]\d{9}", num).group())
print(re.match("^1[35678]\d{9}", "1308907678"))
print(re.match("^1[35678]\d{9}", "19178906543"))

# 2.提取网页源码中所有的文字
# 如下，将其中的所有文字提取出来，去掉标签。思路就是运用sub方法，将标签替换为空
s = """<div>
<p>岗位职责:</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<P>必备要求:</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求:</p>
<p>1、一年以上 Python开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉NVC、MVVM等概念以及相关wEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握SQL，熟练使用 MySQL/PostgresQL中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/cSS/HTML5，JQuery,React.Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项:</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>"""


# 3.提取图片地址
import re

s = """<img data-original="https://img02.sogoucdn.com/app/a/100520024/36189693dc8db6bd7c0be389f8aaddbd.jpg" src="https://img02.sogoucdn.com/app/a/100520024/36189693dc8db6bd7c0be389f8aaddbd.jpg" width="250" height="375" .jpg>"""

result1 = re.search(r"src=\"https.*.jpg\"", s)
print(result1.group())

result2 = re.search(r"src=\"(https.*.jpg)\"", s)  # 我只是想将网址提取出来，所以httpxx加括号，这样我就可以把它单独提取出来，src则不会出来
print(result2.groups()[0])

# 4.从字符串中提取指定范围内的字符串

# （1）提取token的值
import re
str = "csrftoken=ZjfvZBcDMcVs7kzYqexJqtKiJXIDxcmSnXhGD1ObR2deuHzaU0FuCxSmh10fSmhf; expires=Thu, 29 Jun 2023 07:59:04 GMT; Max-Age=31449600; Path=/; SameSite=Lax"
a = re.search(r'=(.*?);', str)
print(a.group(1))    #输出匹配的字符

# （2）从响应包里提取关键词所在的行，可以在正则中添加变量
import re
key = "威胁"
a = """
<body data-spm="7663354">
  <div data-spm="1998410538">
    <div class="header">
      <div class="container">
        <div class="message">
          很抱歉，由于您访问的URL有可能对网站造成安全威胁，您的访问被阻断。
          <div>您的请求ID是: <strong>
781bad0a16702307419116917e43b3</strong></div>
        </div>
      </div>
    </div>
"""
res = re.search(r'<.*>(.*?%s.*?)<.*?>'%(key),a,re.S)
print(res.groups())
print(res.group(1).replace("\n", "").replace(" ", ""))




# 案例3 匹配ip地址
# 简单的匹配一下ip地址

import re
str = "http://100.1.1.1/index.html"
try :
    print(re.search("\d+\.\d+\.\d+\.\d+", str).group())
    print(re.search("\d*?\.\d*?\.\d*?\.\d*",str).group())

except:
    print("找不到相应的ip地址")


