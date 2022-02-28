import turtle
import numpy as np
from generate_map import *

class config : 
    input_file = 'input.txt' 


def read_file(file_name) : 
    input_file = open(file_name, 'r')
    lines = input_file.readlines() 
    new_lines = [] 
    for line in lines : 
        new_lines.append(line.strip().split(' '))
    # new_lines = np.array(new_lines).astype(int)
    for i in range(len(new_lines)) : 
        for j in range(len(new_lines[i])) : 
            new_lines[i][j] = int(new_lines[i][j])
    map_shape = new_lines[0][0], new_lines[0][1]
    source = (new_lines[1][0], new_lines[1][1])
    goal = (new_lines[1][2], new_lines[1][3])
    num_obstacles = new_lines[2][0]

    obstacles = [] 

    for i in range(num_obstacles) :
        obstacle = []  
        for j in range(0, len(new_lines[3 + i]), 2):
            x = new_lines[3 + i][j] 
            y = new_lines[3 + i][j + 1]
            obstacle.append((x, y))
        obstacles.append(obstacle)
    return map_shape, source, goal, num_obstacles, obstacles   
if __name__ == '__main__' : 
    map_shape, source, goal, num_obstacles, obstacles = read_file(config.input_file)
    print(obstacles)