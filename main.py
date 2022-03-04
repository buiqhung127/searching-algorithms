import numpy as np
from generate_map import *
from searching_algorithms import breadth_first_search, uniform_cost_search, greedy_best_first_search, graph_search_asterisk, iterative_deepening_search
from visualization import visualize_map

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
    map_shape, source, goal, num_obstacles, obstacles = read_file(config.input_file)
    ground = generate_ground(map_shape, source, goal, num_obstacles, obstacles)
    # ground_1 = breadth_first_search(ground, source, goal)
    # print(ground_1)
    # ground_2 = uniform_cost_search(ground, source, goal)
    # print(ground_2)
    # ground_3 = greedy_best_first_search(ground, source, goal)
    # print(ground_3)
    ground_4 = graph_search_asterisk(ground, source, goal)
    print(ground_4)
    visualize_map(ground_4)
    # ground_5 = iterative_deepening_search(ground, source, goal)
    # print(ground_5)
    # heap = MaxHeap()
    # heap.insert(3)
    # heap.insert(2)
    # heap.insert(4)
    # heap.insert(8)
    # heap.insert(1)
    # heap.insert(7)
    # heap.insert(2)
    # heap.insert(11)
    # heap.insert(8)
    # heap.insert(12)
    # heap.insert(9)


    # print(heap.heap)
    # for i in range(len(heap.heap)//2):
    #     print(heap.heap[i], heap.heap[2*i +1], heap.heap[2* i + 2])
    # for i in range(11):
    #     print(heap.head(), end=' ')
    #     heap.pop()