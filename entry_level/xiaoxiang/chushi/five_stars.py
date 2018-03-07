import turtle
#迭代五角星绘制
spiral = turtle.Turtle()

for i in range(20):
    #前进的距离
    spiral.forward(i*10)
    #右转角 144度
    spiral.right(144)

turtle.done()
