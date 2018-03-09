"""
    功能：五角星的绘制
    版本：2.0
    增功能：加入循环操作绘制重复不同大小的图形
"""
import turtle

def draw_penagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    
    count = 1
    
    turtle.pencolor('blue')

    size = 50

    while size <= 100:
        turtle.pensize(count)
        #调用函数、
        draw_penagram(size)
        # size = size + 10
        size += 10
        count += 1

    turtle.exitonclick()

if __name__=='__main__':
    main()
