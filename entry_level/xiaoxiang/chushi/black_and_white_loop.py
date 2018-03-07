import turtle

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    #提笔 注意不提笔也能画，是另一种图案
    ninja.penup()
    #返回原点
    ninja.setposition(0,0)
    #放笔 重新画下一条线
    ninja.pendown()

    ninja.right(2)

turtle.done()
