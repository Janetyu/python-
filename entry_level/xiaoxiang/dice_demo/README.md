# 模拟掷骰子

## 案例描述
- 通过计算机程序模拟抛掷骰子，并显示各点数的出现次数及频率
- 比如，抛掷2个骰子50次，出现点数为7的次数是8，频率是0.16

- 1.0功能：模拟抛掷1个骰子，并输出其结果
- 2.0功能：模拟抛掷2个骰子，并输出其结果
- 3.0功能：可视化抛掷2个骰子的结果
- 4.0功能：对结果进行简单的数据统计和分析
- 5.0功能：使用科学计算库简化程序，完善数据可视化结果
- 6.0功能：灵活设置骰子个数，并对结果进行统计分析

## 案例分析
- 如何通过Python模拟随机事件？或者生成随机数？
- random模块
	- 遍历列表时，如何同时获取每个元素的索引号及其元素值？
- enumerate()函数
	- 如何将对应的点数和次数关联起来？
- zip()函数
- Python数据可视化
	- matplotlib模块
- 简单的数据统计分析
	- matplotlib直方图
- 使用科学计算库NumPy简化程序

## random模块
- random模块用于生成随机数
- 常用函数

函数| 含义
----|----
random() |生成一个[0, 1.0)之间的随机浮点数
uniform(a, b) |生成一个a到b之间的随机浮点数
randint(a, b) |生成一个a到b之间的随机整数
choice(<list>) |从列表中随机返回一个元素
shuffle(<list>) |将列表中元素随机打乱
sample(<list>, k) |从指定列表中随机获取k个元素

更多random模块的方法请参考：
https://docs.python.org/3/library/random.html

## enumerate()函数
- enumerate()函数用于将可遍历的组合转换为一个索引序列
- 一般用于for循环中，同时列出元素和元素的索引号

`l = {'a','b','c'}`
	
`for i,x in enumerate(l):`
		
`print("{}--{}".format(i,x))`

## zip()函数
- zip()函数用于将对应的元素打包成一个个元组
- 注意：元组中的元素是不可修改的，若要修改需要转换成字典或其他
	- dict(zip(l1, l2))

## matplotlib模块
- matplotlib是一个数据可视化函数库
- matplotlib的子模块pyplot提供了2D图表制作的基本函数
- 例子：https://matplotlib.org/gallery.html

## 散点图绘制
	import matplotlib.pyplot as plt
	\#x, y分别是x坐标和y坐标的列表
	plt.scatter(x, y)
	plt.show()

## 直方图
- 直方图是一种对数据分布情况的图形表示
- 首先要对数据进行分组，然后统计每个分组内数据的数量。
- 作用：
	- 显示各分组频率或数量分布的情况
	- 易于显示各组之间频率或数量的差别

- matplotlib绘制直方图
- plt.hist(data, bins)

		1. data: 数据列表
		2. bins: 分组边界

## NumPy
- NumPy (Numeric Python)：用Python实现的科学计算库
- 包括：
1. 强大的N维数组对象array
2. 成熟的科学函数库
3. 实用的线性代数、随机数生成函数等
- NumPy的操作对象是多维数组ndarray
- ndarray.shape 数组的维度
- 创建数组：np.array(<list>)，np.arrange() …
- 改变数组形状 reshape()

NumPy
- NumPy创建随机数组
- np.random.randint(a, b, size)
创建 [a, b)间形状为size的数组
- NumPy基本运算
- 以数组为对象进行基本运算，即向量化操作
- np.histogram() 输出直方图的统计结果

matplotlib绘图补充
- plt.xticks() 设置x坐标的坐标点位置及标签
- plt.title()设置绘图标题
- plt.xlabel(), plt.ylabel() 设置坐标轴的标签

课后练习
- 灵活设置骰子个数，并对结果进行统计分析
- 比如3个骰子


