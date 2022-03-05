import numpy as np


def generate_ground(map_shape, source, goal, num_obstacles, obstacles): 
    ground = np.zeros(map_shape).astype(int)
    ground[source[0], source[1]] = 1
    ground[goal[0], goal[1]] = 2
    for i in range(num_obstacles) : # original obstacle
        obs = obstacles[i]
        for ob in obs : 
            ground[ob[0], ob[1]] = -2
    for i in range(map_shape[0]) : # boundary
        ground[i][0] = -1 
        ground[i][map_shape[1] - 1] = -1
    for i in range(map_shape[1]) : # boundary
        ground[0][i] = -1 
        ground[map_shape[0] - 1][i] = -1
    ground = draw_edges(ground, num_obstacles, obstacles)
    return ground

def draw_edges(ground, num_obstacles, obstacles) : 
    for i in range(num_obstacles) :
        obstacles[i].append(obstacles[i][0]) 
        for j in range(len(obstacles[i]) - 1) : 
            point_start =  obstacles[i][j]
            point_end = obstacles[i][j + 1]
            current_point = point_start 
            
            x_e, y_e = point_end
            while current_point != point_end: 
                if abs(x_e - current_point[0]) == 1 and abs(y_e - current_point[1]) == 1 :
                    break   
                x_c, y_c = current_point
                 
                if x_c < x_e : 
                    x_c += 1
                elif x_c > x_e :  
                    x_c -= 1

                if y_c < y_e: 
                    y_c += 1
                elif y_c > y_e :  
                    y_c -= 1
                ground[x_c][y_c] = -3
                current_point = (x_c, y_c)
    return ground
