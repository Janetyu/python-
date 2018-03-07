import turtle
#画红蓝双环
painter = turtle.Turtle()

#画笔上色 蓝
painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123)

#画笔上色 红
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()
