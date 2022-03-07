import turtle as t
import time as ti
from tkinter import *  # Python 3


def visualization_initialize():
    t.speed(36)
    t.pensize(1)

def rectangle(hor, ver, col):
    t.pendown()  
    t.color('black')
    t.begin_fill()
    for counter in range(1,3): 
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.color(col)
    t.end_fill()
    t.penup()

def visualize_map(ground, source, goal, num_obstacles, obstacles):
    ground[source[0]][source[1]] = 3
    ground[goal[0]][goal[1]] = 4
    
    for i in range(num_obstacles):
        for j in range(len(obstacles[i])):
            ground[obstacles[i][j][0]][obstacles[i][j][1]] = -2 

    
    t.penup()
    t.pensize(1)
    t.goto(0,0)
    t.right(90)
    for i in range(len(ground)):
        t.goto(i * 15, 0)
        for j in range(len(ground[i])):
            if ground[i][j] == -1: # boundary
                t.pendown()    
                rectangle(15,15,'grey')   
                t.penup()
            if ground[i][j] == 0: # zone
                pass
                # t.pendown()    
                # rectangle(15,15,'grey100')   
                # t.penup()
            if ground[i][j] == -3: # obstacle
                t.pendown()    
                rectangle(15,15,'LightSalmon')   
                t.penup() 
            if ground[i][j] == -2: # original obstacle
                t.pendown()    
                rectangle(15,15,'LightSalmon4')   
                t.penup()
            if ground[i][j] == 2: # path
                t.pendown()    
                rectangle(15,15,'firebrick')   
                t.penup()
            if ground[i][j] == 3: # path
                t.pendown()    
                rectangle(15,15,'DeepSkyBlue2')   
                t.penup()
            if ground[i][j] == 4: # path
                t.pendown()    
                rectangle(15,15,'DeepSkyBlue4')   
                t.penup()
            t.forward(15)
    t.done()
    # turtle.bgcolor("black")
    # colors = ["red", "yellow", "blue", "green"]
    # for x in range(200):
    #     t.pencolor(colors[x%4])
    #     t.forward(x)
    #     t.left(91)

            