import numpy as np
from generate_map import *
from searching_algorithms import breadth_first_search, uniform_cost_search, greedy_best_first_search, graph_search_asterisk, iterative_deepening_search
from visualization import visualize_map, visualization_initialize

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
    map_shape = new_lines[0][0] + 1, new_lines[0][1] + 1 # width height
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
    
    visualization_initialize()
    map_shape, source, goal, num_obstacles, obstacles = read_file(config.input_file)

    ground = generate_ground(map_shape, source, goal, num_obstacles, obstacles)
    print('Please choose algorithms to visualization :')
    print('1. Breadth-first search')
    print('2. Uniform-cost search')
    print('3. Iterative deepening search')
    print('4. Greedy-best first search')
    print('5. Graph-search A*')
    print('0. Quit')
    cmd = input('>>')

    if cmd == '1':
        new_ground, cost = breadth_first_search(ground, source, goal) 
    elif cmd == '2':
        new_ground, cost= uniform_cost_search(ground, source, goal)
    elif cmd == '3':
        new_ground, cost = iterative_deepening_search(ground, source, goal)
    elif cmd == '4':
        new_ground, cost = greedy_best_first_search(ground, source, goal)
    elif cmd == '5':
        new_ground, cost = graph_search_asterisk(ground, source, goal)
    print('Visualization in progress!')
    visualize_map(new_ground, source, goal, num_obstacles, obstacles)       
    print('Cost:', cost) 
    print('Visualization in done!')
