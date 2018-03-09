# 52周存钱挑战
## 案例描述 
- 52周存钱法，即52周阶梯式存钱法，是国际上非常流行的存钱方法。
- 按照52周存钱法，存钱的人必须在一年52周内，每周递存10元
- 例子：
第一周存10元，第二周存20元，第3周存30元，一直到第52周存520元。
这样一年下来会有多少钱呢？
10+20+30+40+50+……+520=13780
- 2.0增加功能：记录每周的存款数
- 3.0增加功能：使用循环直接计数
- 4.0增加功能：灵活设置每周的存款数，增加的存款数及存款周数
- 5.0增加功能：根据用户输入的日期，判断是一年中的第几周，然后输出
相应的存款金额

## 列表
- 列表（list）是有序的元素集合
- 可通过索引访问单个元素，如 l[2], l[-1]
- 可通过区间索引访问子列表内容，如 l[2:5], l[-3:]
- 列表中每个元素类型可以不同
***
|列表操作符| 含义|
| ------------- |:-------------:| -----:|
|list1 + list2  |  合并（连接）两个列表|
|list1 * n    | 重复n次列表内容|
|len(list1)| 返回列表长度（元素个数）|
|x in list1| 检查元素是否在列表中|

***

|列表操作符| 含义|
| ------------- |:-------------:| -----:|
list1.append(x) |将x添加到列表末尾
list1.sort() |对列表元素排序
list1.reverse() |将列表元素逆序
list1.index(x) |返回第一次出现元素x的索引值
list1.insert(i, x) |在位置i处插入新元素x
list1.count(x) |返回元素x在列表中的数量
list1.remove(x) |删除列表中第一次出现的元素x
list1.pop(i) |取出列表中i位置上的元素，并将其删除
***
## math 库
|函数| 含义|
| ------------- |:-------------:| -----:|
math.pi |圆周率
math.ceil(x) |对x向上取整
math.floor(x) |对x向下取整
math.pow(x, y) |x的y次方
math.sqrt(x) |x的平方根
math.fsum(list1) |对集合内的元素求和
… |…

- 更多math库函数请参考： https://docs.python.org/3/library/math.html

***

## for 循环
- 使用for语句可以循环遍历整个序列的内容

	``for < x > in < list1 >:``
	``<body>``
- 循环变量x在每次循环时，被赋值成对应的元素内容
- 与while循环的区别
- for循环的次数固定，即所遍历的序列长度
- while为无限循环
- range(n) 返回一个可迭代的对象
- list(range(n))将迭代类型转换为列表类型

## 函数的参数传递
- 函数通过参数与调用程序传递信息
- 变量的作用范围
- 局部，函数内的变量作用范围只在函数内
- 全局，函数外的变量，在所有函数中都能使用，global
- 函数的形参只接收实参的值，给形参赋值并不影响实参

## datetime库
- 处理时间的标准函数库datetime
- datetime.now() 获取当前日期和时间
- 字符串 -> datetime
datetime.strptime()，解析时间字符串
- datetime -> 字符串
datetime.strftime() 格式化datetime为字符串显示
- 日期时间格式参考：

	https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
- isocalendar() 返回年，周数，及周几
- 更多操作参考：

	https://docs.python.org/3/library/datetime.html#module-datetime