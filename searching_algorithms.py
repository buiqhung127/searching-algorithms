import numpy as np

class searching_config: 
    agent_move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def __init__(self, ground) : 
        M, N = ground.shape
        self.is_visited = ground < 0 
        self.tracing_map = np.full((M, N), 0, dtype='int,int')

        

class SimplifiedQueue : 
    def __init__(self, M, N) :
        self.queue = []  
    def push(self, value) : 
        self.queue.append(value)
    def is_empty(self) : 
        if len(self.queue) == 0:
            return True
        else:
            return False
    def head(self): 
        return self.queue[0]
    def pop(self):
        self.queue.pop(0)


def breadth_first_search(ground, source, goal) : 
    config = searching_config(ground)
    goal_found = False
    M, N = ground.shape
    queue = SimplifiedQueue(M, N)
    x, y = source
    config.is_visited[x][y] = 1
    source = (x, y, (-1, -1))
    queue.push(source)
    
    
    while not queue.is_empty() and not goal_found:
        current_point = queue.head()
        queue.pop()
         
        config.tracing_map[current_point[0]][current_point[1]] = current_point[2]

        new_step_x = current_point[0]
        new_step_y = current_point[1]

        for step in config.agent_move : 
            
            new_step_x += step[0]
            new_step_y += step[1]
            new_step_trace = (current_point[0], current_point[1])
            if config.is_visited[new_step_x][new_step_y] == 0:
                queue.push((new_step_x, new_step_y, new_step_trace))
                config.is_visited[new_step_x][new_step_y] = 1
            if (new_step_x, new_step_y) == goal : 
                goal_found = True 
                config.tracing_map[goal[0]][goal[1]] = (current_point[0], current_point[1])
                break

    if goal_found : 
        tracer = config.tracing_map[goal[0]][goal[1]]
        while tracer[0] != -1 and tracer[1] != -1:
            print(tracer)
            ground[tracer[0]][tracer[1]] = 2
            tracer = config.tracing_map[tracer[0]][tracer[1]]
    return ground