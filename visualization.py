import turtle as t
import time as ti
from tkinter import *  # Python 3

def rectangle(hor,ver,col):
    t.pendown() #tạo con trỏ
    t.pensize(1) #kích cỡ
    t.color(col)
    t.begin_fill()
    for counter in range(1,3): #đây là một vòng lặp (loop)
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

def visualize_map(ground):
    t.speed(10)
    t.penup()
    t.pensize(1)
    t.goto(0,0)
    t.right(90)
    for i in range(len(ground)):
        t.goto(i * 15, 0)
        for j in range(len(ground[i])):
            if ground[i][j] == -1:
                t.pendown()    
                rectangle(15,15,'grey')   
                t.penup()
            if ground[i][j] == 0:
                pass
                # t.pendown()    
                # rectangle(15,15,'grey100')   
                # t.penup()
            if ground[i][j] == -3:
                t.pendown()    
                rectangle(15,15,'LightSalmon')   
                t.penup() 
            if ground[i][j] == -2:
                t.pendown()    
                rectangle(15,15,'LightSalmon4')   
                t.penup()
            if ground[i][j] == 2:
                t.pendown()    
                rectangle(15,15,'firebrick')   
                t.penup()
            t.forward(15)
    t.done()
    # turtle.bgcolor("black")
    # colors = ["red", "yellow", "blue", "green"]
    # for x in range(200):
    #     t.pencolor(colors[x%4])
    #     t.forward(x)
    #     t.left(91)

            