"""
    功能：模拟掷骰子
    版本：1.0
    2.0新增功能：模拟投掷两个骰子
    3.0新增功能：可视化投掷两个骰子的结果
    4.0新增功能：直方图可视化结果
    5.0新增功能：科学计算
    6.0灵活设置骰子个数，并对结果进行统计分析
"""
import matplotlib.pyplot as plt
import numpy as np

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    total_times = 10000

    #骰子个数
    num = int(input("请输入骰子数量："))

    #创建总的骰子列表，用来装每一个骰子（列表）
    roll_arr = []

    # 记录骰子的结果
    for i in range(num):
        roll_arr_i = np.random.randint(1,7,size=total_times)
        roll_arr.append(roll_arr_i)
    result_arr = sum(roll_arr)

    print(len(roll_arr))

    hist,bins = np.histogram(result_arr,bins=range(num,6*num+2))
    print(hist)
    print(bins)

    #数据可视化
    plt.hist(result_arr,bins=range(num,6*num+2),normed=1,edgecolor='black',linewidth=1,rwidth=0.8)

    #初始化x坐标具体点数的值，后面替换为3点，4点......
    tick_labels = [0]*(num*6+1-num)
    count = 0

    #设置x坐标点显示
    for j in range(num,num*6+1):
        tick_labels[count] = str(j) + '点'
        count += 1
    tick_pos = np.arange(num,6*num+1) + 0.5
    plt.xticks(tick_pos, tick_labels)
    
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()
    
    
if __name__ == '__main__':
    main()
