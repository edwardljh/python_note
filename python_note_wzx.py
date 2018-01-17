import time
import datetime
import calendar as cal
import arrow
import random
import math
from array import array
import itertools
import functools
from functools import reduce
import collections
import os
from collections import deque
from collections import namedtuple
from collections import OrderedDict



'''
os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
os.curdir  # 返回当前目录: ('.')
os.pardir  # 获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')   # 可生成多层递归目录
os.removedirs('dirname1')   # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')   # 生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')   # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  # 删除一个文件
os.rename("oldname","newname")  # 重命名文件/目录
os.stat('path/filename')  # 获取文件/目录信息
os.sep    # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    # 输出用于分割文件路径的字符串
os.name    # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  # 运行shell命令，直接显示
os.environ  # 获取系统环境变量
os.path.abspath(path)  # 返回path规范化的绝对路径
os.path.split(path)  # 将path分割成目录和文件名二元组返回
os.path.dirname(path)  # 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  # 如果path是绝对路径，返回True
os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  # 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
'''


timetest = (2017,4,3,17,40,36,0,0,0)
time.strftime("%y%d%m",time.localtime())
time.strftime("%y",time.localtime())
time.localtime(time.time())
cal.month(2016,5)
cal.calendar(2017)
datetime.date(2017,4,6)
time.time() #时间戳
time.clock() #CPU时间
time.gmtime(time.time())
time.gmtime()
time.localtime()
# 前面三个输出的都是下面的格式
# time.struct_time(tm_year=2017, tm_mon=5, tm_mday=9, tm_hour=7, tm_min=12, tm_sec=59, tm_wday=1, tm_yday=129, tm_isdst=0)
time.asctime(time.localtime())
# 将struct_time转换为Tue May  9 15:12:59 2017，这样的格式
time.ctime(time.time())
# 将时间戳转换为Tue May  9 15:12:59 2017，这样的格式
time.mktime(time.localtime())
# 将struct_time转换为时间戳格式
time.strftime('%y',(2017, 5, 9, 7, 12, 59, 1, 129, 0))
# 将tuple按格式转换
time.strptime('20170908','%Y%d%m')
# 将日期转换为struct_time,即time tuple
# 掌握time和calendar包的相关函数
time.strftime('%y',time.gmtime(time.time()))
# 将时间戳转换为time tuple，再转换为格式化时间
time.sleep(1)
# 暂停1秒执行下面的语句

nowtime = arrow.now()   # 返回本地当前日期，2017-07-20T17:35:51.665802+08:00
utctime = arrow.utcnow()    # 返回当前的世界统一时间，即utc时间
arrow.now('US/Pacific')  # 输出某地的当前时间
nowtime.year     # 返回年份
nowtime.month
nowtime.day
nowtime.hour
nowtime.minute
nowtime.second
nowtime.timestamp    # 输出日期的时间戳格式,将日期转换为时间戳
nowtime.datetime # 输出的是datetime的日期格式元组
nowtime.date()
nowtime.time()
nowtime.shift(hours= -1)
nowtime.replace(minutes = -1)    # 在日期上减去一分钟，时间偏移
nowtime.replace(hours = -1)
nowtime.replace(hour = 23)
nowtime.replace(years = -1)
nowtime.replace(seconds = -1)
nowtime.replace(months = -1)
nowtime.replace(days = -1)
nowtime.replace(hours = 5)   # 将日期中的时改为5
nowtime.replace(weeks = +5)  # 将日期加35天,即5周
nowtime.format() # 将arrow的格式日期转换为正常人类常见的日期格式，2017-07-20 17:38:13+08:00
nowtime.format('YYYY-MM-DD HH:mm:ss ZZ')
arrow.now().format('YYYYMMddHHmmssSSSSS')
arrow.get(time.time()).format()   # 将时间戳转换为arrow格式的日期格式，将时间戳转换为日期
arrow.get(13767883664)
arrow.get('20-8-2017', 'DD-M-YYYY').format('YYYY-MM-DD')
arrow.get('13767883664') # 将数字转换为日期，加引号或者不加引号都可以，还可以带小数点
arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
# 该例子说明的是，arrow.get（）方法是将参数转换为日期，参数可以是时间戳，可以是日期字符串
arrow.get('June was born in May 1980', 'MMMM YYYY')  #从文字中提取出日期
arrow.get(2013, 5, 5)
nowtime.replace(minutes = -1).humanize() # 输出'a minute ago'
nowtime.replace(weeks = 2).humanize() # 输出'in 13 days'
nowtime.span('hour')
# 获取小时的起始点


x,y= [2,3] # 输出x=2，y= 3
x,y= [2,3],[4,5] # 输出x= 【2，3】，y= 【4，5】
x,y = y,x # 互换xy的值
a,b,*c= [1,2,3,5,6] # 输出a=1，b=2，c= (3,5,6),元组拆包

中国 = 'china'  # 变量名可以是汉字

lista = [1,2,3,4,5,6,7]
iter = iter(lista)
print(next(iter))
# 迭代器

a = [1,2,3,4,5,6,7,8,9,10]
b = a[0:8:2]
# 输出的b为[1,3,5,7],表示隔1取数
a[:]
a[2:6]
a[2:]
a[:7]
a[-3:-1]
# list切片
c = [x for x in a] # 列表推导式
x = [1,2,3]
y = [4,5,6]
z = [(r,t) for r in x for t in y]
# 列表推导式，生成笛卡尔积
a= 'hello'
print(a[::-1]) # 结果是hello的反转olleh, 步长为负数时就相当于倒着取值


strtest = ' abc '
strtest[::-1] # 翻转字符串
strtest.lstrip() # 去除左边空格，默认空格，里面可以添加其他字符，如'['
strtest.rstrip() # 去除右边空格，strip函数只能去除最左边或最右边的某个指定字符
strtest.strip()  # 同时执行lstrip与rstrip
strtest.rjust(30,'^')   # 右对齐，并凑够30个位置，空白位用|填充，填充符号默认为空格
xstr = 'abcDbRa'
xstr.capitalize()   # 将字符串的首字母大写,其余的小写
xstr.swapcase()  # 将小写字母大写，大写字母小写
xstr.count('b',0,2) # 查找字符串b在xstr中出现的次数，beg和end指定查找范围的起始位置
# bytes.decode(),str.encode(),bytes与str之间的相互转换
xstr.center(11,'v')
# 指定宽度11，并用v填充，相当于在字符串的首尾添加相同数量的v，首尾各自的数量为11-6再除以2，6为xstr长度
# 如果不能被2整除，就左边比右边多一个，vvvabcDbRvv
xstr.endswith('b',0,5)   # 检查xstr在指定范围内是否以字符b结尾，是的话为true，否则为false
xstr.startswith('b',0,5) # 检查xstr在指定范围内是否以字符b开头，是的话为true，否则为false
ystr = 'b   c'
ystr.expandtabs(tabsize = 3) # 将tab字符串转换为空格
xstr.find('bc',0,4)  # 字符串bc是否在xstr中，如果在，返回开始的索引值，否则返回-1
xstr.rfind('bc',0,4)    # 与find类似，只是从右边开始查找
xstr.index('bc',0,4) # 找bc在xstr中的索引，跟find一样，但是如果找不到会报错
xstr.rindex('bc',0,4)    # 与index类似，只是从右边开始
xstr.isalnum()  # 判断字符串是否全部为字母或数字
xstr.isalpha()  # 判断字符串是否全为字母
xstr.isdigit()  # 判断字符串是否全为数字
xstr.islower()  # 判断字符串中的字母是否全为小写
xstr.isupper()  # 判断字符串中的字母是否全为大写
xstr.isnumeric()    # 判断字符串中的字符是否全为数字字符
xstr.isspace()    # 判断字符串是否只包含空格
xlist = ['q','w','ee']
'/'.join(xlist)  # 将序列中的元素以指定的符号拼接起来，q/w/ee
len(xstr)    # 返回字符串长度，len（）这个函数在哪都能用，不只是字符串
max(xstr)
min(xstr)
xstr.lower()
xstr.upper()
zstr = 'abc is ac'
zstr.title() # 所有单词的首字母大写，其余小写
zstr.istitle()  # 判断字符串是否为title标题化字符
zstr.zfill(20)   # 返回长度为20的字符串，如果zstr长度不够20，用0填充，在左边填充,如果20小于字符长度，返回这个字符
wstr = 'ak/djk/dl/d'
wstr.split('/')  # 用指定符号分割字符串，该符号需在字符串中出现，其实就是一个正则
wstr.split('/', 1) # 1指的是分割次数
estr = 'woshi' \
       'sowho' \
       'hahd'
estr.splitlines(keepends = True) # 按照行分割字符串，返回一个包含各行作为元素的列表，keepends若为false，则不包含换行符
xstr.replace('a','ttt',2)    # 将字符串中的a替换为ttt，2指最大替换次数，因为a在xstr中可能存在多个
xstr.__contains__('a') # 字符串是否包含字母a
xstr.partition('c') # 用字母c将字符串分割开
# x in y 判断字符串x是否在y中


list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_1.append(5)     # 向列表中添加一个元素，这个元素可以是列表
list_1.extend(list_2)     # 将另一个序列合并到列表，但是序列中的元素会被拆分开
list_1.insert(1,8)   # 在列表的第二个位置插入8
list_1.remove(1)     # 删除列表中第二个元素
list_1.reverse()     # 倒排列表
list_1.copy()    # 列表的浅复制
list_1.sort()     # 列表元素排序
list_1.pop()     # 移除列表最后一个元素，并返回该元素
list_1.pop(1)   # 移除指定索引的元素，并返回该元素
# list_1.index(1)  # 返回某元素的索引
list_1.count(3)  # 返回某元素在列表中出现的次数
#xlist.clear()   # 移除列表中的所有元素
list_1.index(2)  # 查看某元素的索引
# 列表工厂函数
list_1[1] = 4 # 更改列表元素
list_1 * 2
list_1 + list_1
# 相当于extend

dict_x = {}
dict_x['a'] = 1
dict_x.update({'b':2})
# 以上两种方法都可以将新元素添加到字典中
dicttest = {1:2,3:4}
dicttest.keys() # 获取字典的所有key
dicttest.values() # 获取字典的所有值
for a,b in dicttest.items():
    print(a,b)
d = [('a',3),('t',5)]
e = dict(d)
# 可以直接将d这种格式的转为字典，即列表中的元素为元组
# e.keys(),e.items(),e.values(),del e,e.clear(),del e[key],e.pop(key),e.get(key)
d = {}.fromkeys(('q','r'),1)    #这个方法将1赋给了两个key
# 字典工厂函数
dict() # 空字典
dict(a = 'a',b = 'b',c = 'c')
# 以上方法也是构造字典的方法
dic= {'a':1,'b':2,'c':3}
dic.get('a')
dic.pop('a')

set_x = set([1,2,3,4,5])
set_y = set([6,7,8,9,1])
set_x.add(6)
set_x.remove(6)
set_x | set_y    # 并集
set_x & set_y    # 交集
set_x - set_y    # 差集，在set_x但不在set_y
set_x ^ set_y    # 对称差集，元素在a或者b中，但不会同时出现在ab中
# 可以用set函数去除重复元素

od = OrderedDict((('a',1),('b',2),('c',3)))
# 该函数的作用跟dict（）一样，不一样的是，可以保证里面的key是有序的

dq = collections.deque([1,2,3])
dq.appendleft(4)
dq.append(6)
dq.popleft()
dq.pop()
dq_1= deque([3,3,5,6],maxlen= 10) # 限制deque的长度
dq_1.rotate(2) # 将右边的元素移动到左边，先移动6，再移动5
# 队列dq 与list兼容的方法差不多，但是插入、修改元素速度很快

nt= namedtuple('nt',['a','b','c','d'])
nt(a= 5,b= 6,c= 7,d= 8)
nt.a
# 具名元组就像一个轻量的类，'nt'是类名，abcd是初始变量，也好像一个字典，abcd是keys


random.random()   # 生成0-1内的随机浮点数
random.uniform(5,90)  # 生成5-90内的随机浮点数，包涵上限下限
random.randint(5,100) # 生成5-100内的随机整数，包涵上限，下限
random.randrange(1,100,5) # 生成随机数，这个数在1-100，且以5为步长的数字序列里
random.choice([1,2,3,4,5])
random.choice('python')
# 以上方法都是从序列中随机选择一个元素，字符串也可以哦
random.sample(range(100),20)
random.sample('python',2)
# 以上方法都是从序列中随机选择指定个数的元素，字符串也可以哦，可以理解为采样
random.shuffle(list(range(5)))
# 打乱序列中的顺序


n = itertools.count(1) # 创建一个无限的迭代器，上述代码会打印出自然数序列
n = itertools.count(100,2) # 100开始，2为步长，无限序列
n = itertools.cycle('abc') # 把传入的一个序列无限重复下去,a,b,c,a,b,c不停迭代
n = itertools.repeat('abc',10) #把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数,'abc','abc','abc'
# 上述三个都是无限迭代器
n = itertools.chain('abc','xyz') # 把一组迭代对象串联起来，形成一个更大的迭代器

n = itertools.groupby('aaabbbccaadd') # 把迭代器中相邻的重复元素挑出来放在一起,aaa,bbb,cc,aa,dd
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
# 上述两行代码，指定输出的限制条件，输出1到10
n = itertools.permutations([2,4,5,6],3) # 表示从序列中挑出3个元素进行排列
n = itertools.combinations([2,4,5,6],3) # 表示从序列中挑出3个元素进行组合
n = itertools.product([2,3,4],[5,6,7],[8,9,0]) # 笛卡尔积
n = itertools.islice('abdhklhldhwoh',2,7,2) # 生成一个从字符串第3个字符开始，第8个字符结束，步长为2的迭代器对象
n = itertools.starmap(max,[[5,14,5],[2,34,6],[3,5,2]]) # 针对列表中的每一个元素执行max函数
# n = itertools.imap(lambda x: x*x, [1, 2, 3])
# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准，
# 同理izip,ifilter也是如此


with open('20170627101259.txt','a+') as file:
     print(file.read())

list_3 = range(1,11)
def func1(x):
    return x + 1
map(func1,list_3)   # map函数将参数中的函数依次作用于参数中的序列上

def func2(x,y):
    return x + y
reduce(func2,list_3)
# reduce函数，参数中的函数必须包含两个参数，如果初始值没有给定，那么函数将先作用于序列的前两个元素，然后再作用于结果与后一个元素上，返回一个数值

def func3(x):
    return x > 3
filter(func3,list_3)
# filter是一个过滤函数，会将不符合条件的元素筛选掉，所以参数中的函数需要是一个布尔型函数

reduce(lambda x,y: x*y,range(1,5))
math.factorial(4)
# 上述两行代码都是阶乘的实现


# python内置函数
list_4 = [3,4,2,1,5,6,7,-8,9,10]
sorted(list_4,key = abs,reverse = True)   # 排序
reversed(list_4) # 倒序排列，直接使用reversed函数返回的不是列表，是一个可迭代的对象，就像range，python3特性
abs(-5)  # 绝对值
str(-5)
float(-5)
int(7.8)
round(9.99,1)   # 类似于excel的round函数
math.ceil(9.3) # 向上取整
list(range(5))
pow(2,3) # 2**3
max(list_4)
min(list_4)
len(list_4)   # 获取对象的长度
hash('titanic_train.csv')   # 获取某对象的哈希值
math.pow(5,6)   # 计算5的6次方
all(list_4) # 判断一个序列中元素是否全部不为0或空或false，如果是返回true，否则返回false，简言之，是否全为TRUE
any(list_4) # 判断一个序列中元素是否全部为0或空或false，若是，返回false，若否，返回true，简言之，是否存在TRUE
bin(5) # 返回5的二进制表示
#open()
type(list_4) # 返回一个对象的类型
tuple(list_4) # 将列表转换为元组
set()
sum(list_4)
divmod(5,2) # 取模，返回商和余数，是一个数组
eval('3*7') # 该函数用来执行一个字符串表达式
# a = '[1,2]' eval(a) 字符串中是个列表，eval可以直接将其转换为列表，字典类似
# a = '{1:2,3:4}' eval(a)

for x,y in enumerate(list_4):
    # enumerate函数会将数组或列表组成一个索引序列，如果对一个列表，既要遍历索引又要遍历元素时，可以用该函数
    print(x,y)

list_5 = [1,2,3,4,5]
print(list(enumerate(list_5)))
#list转化后可以输出为列表，每个元素是一个个元组

for x in zip([1,24,5] , [2,4,7]):
    print(x)
# 多个变量并列循环写法
# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组）
# 然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
# 利用*号操作符，可以将list unzip（解压），zip(*zip([1,24,5] , [2,4,7]))

a = 9
if a > 5:
    print(a)
elif a > 9:
    print(6)
elif a > 11:
    print(7)
else:
    print(100)

if a > 5 or a < 100:
    print(a)

if 5 < a < 100:
    print(a)

if a > 5 and a < 100:
    print(a)

if not a == 5:
    print(a)

# print(5,6,'\n',5) 换行符也需要加引号


def fbnq(n):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return [1,1]
    elif n <0:
        return None
    else:
        f= [1,1]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f
# 斐波那契序列生成函数

def f1():
    with open('/Users/ifumai/OneDrive/Python/mlnote/top.txt') as f:
        for line in f:
            yield line
        # 生成器函数

def f2():
    with open('/Users/ifumai/OneDrive/Python/mlnote/top.txt') as f:
        for line in f:
            return line
x= f1()
y= f2()
# y的结果为文件f的第一行，但是x却是一个生成器，返回一个可迭代对象，通过next(x),可以迭代出文件的所有行
# yield只能写在函数里，作为return的一个特例
# 生成器只能遍历一次

'''
生成器可以生成一个可迭代对象，
iter（）也可以
'''

n= 0
while n < 100:
    if n > 10:
        break
    print(n)
    n += 1

while n < 100:
    if n / 2 == 0:
        continue
    print(n)
    n += 1
# break 是跳出整个循环，continue只是跳出本次循环


def f(x):
    n = reduce(lambda x, y: sum(x , y), [i / pow(i, 3) for i in range(1, x, 1)])
    m = reduce(lambda x, y: sum(x , y), [i / pow(i, 3) for i in range(1, x, 2)])
    return n / m

# 闭包
def f1(x):
    def f2(y):
        return x + y
    return f2

a= f1(5)
# 返回f2这个函数
b= a(6)
# 返回11
# 闭包本质上是一个函数，它有两部分组成，嵌套函数和局部变量（包括顶层函数f1的参数）
# 闭包中的顶层函数必须返回的是嵌套函数
# 闭包使得这些变量的值始终保存在内存中
# 闭包使得局部变量在函数外被访问成为可能
# 专业来说,闭包就是内部函数引用闭包作用域的函数或者变量，装饰器就是帮你实现了这一功能

'''
装饰器本质上是一个Python函数，
它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
'''

'''
try:
    print(1/0)
except:
    print('running wrong')
    raise
# raise 可以将具体的异常抛出来
'''


def person(name,age,**kwargs):
     print('name:',name,'age:',age,'other:',kwargs)
person('Frank','37')
person('Frank','37',city='Shanghai')
person('Frank','37',gender='M',job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

'''
输出如下
name: Frank age: 37 other: {}
name: Frank age: 37 other: {'city': 'Shanghai'}
name: Frank age: 37 other: {'gender': 'M', 'job': 'Engineer'}
**kwargs关键字参数
关键字参数可以扩展函数的功能。
比如，在person函数里，保证能接收到name和age这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。
试想正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求
'''

def f(x,y,*args):
    return x + y + sum(args)
# 可变参数
f(1,2,3,4,5)
# 相当于x,y,*args= [1,2,3,4,5]


class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
# 定义类class
studenttest = Student("dawang",20,400)
"%s is %d years old , and the score is %d"%(studenttest.name,studenttest.age,studenttest.score)
"{0} is {1} years old , and the score is {2}".format(studenttest.name,studenttest.age,studenttest.score)
# 格式化字符串，str.format()


class T:
    age = 18
    def __init__(self,name= 'wangyi'):
        self.name= name
    def funcx(self):
        return 5
    def funcy(self):
        return 6
    def __call__(self):
        return 7
# Python 还规定，__init__ 只能返回 None 值

t = T() # 构造实例对象
t.funcx()
t.name
t.age
t()
# 这种写法相当于直接调用__call__(),是一个可调用对象，t.__call__()也是可以的
# 凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable
# __call__可以让对象直接像函数一样使用，类似于重载圆括号
'''
先定义了类，类里面定义的函数都是类实例化为对象后的方法，方法包括类里面定义的函数与变量，可以直接作用于对对象上
事实上，先定义一个类（class），并初始化它的域和方法，然后从属于它的具体对象（object）通过调用这个类的域和方法，
即可得到目标值，这其实是模块化设计的体现
类的初始化函数是用__init__来完成的，_init__()不是类的构造函数，只是用来做初始化的
'''

'''
class Kind:
    __slots__ = ('n', 'a','marriage','tall','__xx')  # 用tuple定义允许绑定的属性名称
    __xx = 5
    def __init__(self, name, age, marriage, tall):
        self.n = name
        self.a = age
        self.marriage = marriage
        self.tall = tall
        self.__xx= 10
        # n,a都是类的属性，它的值是init函数的参数或者常量，但人们通常将类的属性与初始化函数的参数名写为一样的
        # 如果没有初始化，直接kind.person()就可以，但是如果有的话，就必须先构造实例
        # 指定属性默认值，如果在此处写为self.name = 1，构建实例时name参数写什么，输出的都会是1
kind = Kind('wang', 18, 'no', 188)
print(kind.marriage, kind.a, kind.n, kind.tall, kind.person('da', 20, 'yes', 188))
'''

class a:
    def __init__(self):
        print('a1')
        print('a2')

class b(a):
    def __init__(self):
        print('b1')
        super(b,self).__init__()
        print('b2')

class c(a):
    def __init__(self):
        print('c1')
        super().__init__()
        print('c2')

class d(b,c):
    def __init__(self):
        print('d1')
        super().__init__()
        print('d2')
# super函数可以在子类中调用父类的方法，在子类的某方法与父类方法名称重复时，就需要用到super函数


class c:
    def __init__(self, year, month):
        self.year= year
        self.month= month

    @classmethod
    def f1(cls,x): # 这里第一个参数是cls， 表示调用当前的类名
        year, month= map(int, x.split('-'))
        return cls(year, month) # #返回的是一个初始化后的类
    # classmethod 这个装饰器方法就相当于构造了类的一个实例
    '''
    因为有的时候参数可能不符合类实例参数的要求，需要进行改造，
    就是year, month= map(int, x.split('-'))，
    为了省事，为了不用每次先调用改造函数，再构造实例，可以用classmethod装饰器，
    例如实例所需的参数是2017，6，但是有一个字符串是2017-6，那么就需要将字符串改造成2017，6，
    再构造实例，然后再调用f2函数。
    通过classmethod，就可以在构造类的同时就将字符串改造好了,
    这样的好处就是以后重构类的时候不必要修改构造函数,
    只需要额外添加你要处理的函数，
    然后使用装饰符 @classmethod 就可以了
    '''

    def f2(self):
        return self.year, '\n', self.month

    '''
    e= c.f1('2017-6')
    e.f2()
    '''