import numpy as np

class searching_config: 
    agent_move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cost_per_move = 1
    path_notation = 2


    # config for id search
    def __init__(self, ground) : 
        M, N = ground.shape
        self.is_visited = ground < 0 
        self.tracing_map = np.full((M, N), 0, dtype='int,int')

class SimplifiedQueue : 
    def __init__(self) :
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
    # M, N = ground.shape
    queue = SimplifiedQueue()
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
            ground[tracer[0]][tracer[1]] = config.path_notation
            tracer = config.tracing_map[tracer[0]][tracer[1]]

    return ground

class MaxHeap() : 
    def __init__(self):
        self.heap = [] 
    def heapify(self, pos_root, size) : 
        max_pos = pos_root
        left = 2 * pos_root + 1
        right = 2 * pos_root + 2

        if left < size and self.heap[left][3] > self.heap[max_pos][3]:
            max_pos = left 
        if right < size and self.heap[right][3] > self.heap[max_pos][3]:
            max_pos = right
        if max_pos != pos_root:
            self.heap[pos_root], self.heap[max_pos] = self.heap[max_pos], self.heap[pos_root]
            self.heapify(max_pos, size)
    def head(self) : 
        return self.heap[0] 
    def is_empty(self) :
        if len(self.heap) > 0 : 
            return False
        return True
    def push(self, value): # value include x, y, cost
        self.heap.append(value)
        size = len(self.heap)
        if len(self.heap) > 1:
            for i in range(size//2 - 1, -1, -1):
                self.heapify(i, size)
    def pop(self):
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        self.heap.pop(len(self.heap) - 1)  
        for i in range((len(self.heap)//2)-1, -1, -1):
            self.heapify(i, len(self.heap))


def uniform_cost_search(ground, source, goal) : 
    config = searching_config(ground)
    goal_found = False
    queue = MaxHeap()
    x, y = source
    config.is_visited[x][y] = 1
    source = (x, y, (-1, -1), searching_config.cost_per_move)
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
                queue.push((new_step_x, new_step_y, new_step_trace, searching_config.cost_per_move))
                config.is_visited[new_step_x][new_step_y] = 1
            if (new_step_x, new_step_y) == goal : 
                goal_found = True 
                config.tracing_map[goal[0]][goal[1]] = (current_point[0], current_point[1])
                break

    if goal_found : 
        tracer = config.tracing_map[goal[0]][goal[1]]
        while tracer[0] != -1 and tracer[1] != -1:
            ground[tracer[0]][tracer[1]] = config.path_notation
            tracer = config.tracing_map[tracer[0]][tracer[1]]
    return ground
def manhattan_distance(first_point, second_point) : 
    return abs(second_point[0] - first_point[0]) + abs(second_point[1] - first_point[1]) 

def greedy_best_first_search(ground, source, goal) : 
    config = searching_config(ground)
    goal_found = False
    queue = MaxHeap()
    x, y = source
    config.is_visited[x][y] = 1
    source = (x, y, (-1, -1), manhattan_distance(source, goal))
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
                queue.push((new_step_x, new_step_y, new_step_trace, manhattan_distance((new_step_x, new_step_y), goal)))
                config.is_visited[new_step_x][new_step_y] = 1
            if (new_step_x, new_step_y) == goal : 
                goal_found = True 
                config.tracing_map[goal[0]][goal[1]] = (current_point[0], current_point[1])
                break

    if goal_found : 
        tracer = config.tracing_map[goal[0]][goal[1]]
        while tracer[0] != -1 and tracer[1] != -1:
            ground[tracer[0]][tracer[1]] = config.path_notation
            tracer = config.tracing_map[tracer[0]][tracer[1]]
    return ground

def graph_search_asterisk(ground, source, goal) : # graph search asterisk 
    config = searching_config(ground)
    goal_found = False
    queue = MaxHeap()
    x, y = source
    config.is_visited[x][y] = 1
    source = (x, y, (-1, -1), manhattan_distance(source, goal) + searching_config.cost_per_move)
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
                queue.push((new_step_x, new_step_y, new_step_trace, manhattan_distance((new_step_x, new_step_y), goal) + searching_config.cost_per_move))
                config.is_visited[new_step_x][new_step_y] = 1
            if (new_step_x, new_step_y) == goal : 
                goal_found = True 
                config.tracing_map[goal[0]][goal[1]] = (current_point[0], current_point[1])
                break

    if goal_found : 
        tracer = config.tracing_map[goal[0]][goal[1]]
        while tracer[0] != -1 and tracer[1] != -1:
            ground[tracer[0]][tracer[1]] = config.path_notation
            tracer = config.tracing_map[tracer[0]][tracer[1]]
    return ground

def depth_limited_first_search(current_point, current_depth, depth_limit, goal, tracer, config): 
    found_goal = False
    if current_depth > depth_limit:
        return False, []
    
    for step in config.agent_move :   
        new_step_x = current_point[0] + step[0]
        new_step_y = current_point[1] + step[1]
        if config.is_visited[new_step_x][new_step_y] == 0:
            config.is_visited[new_step_x][new_step_y] = 1
            temporary_tracer = tracer  
            temporary_tracer.append((new_step_x, new_step_y))
            if (new_step_x, new_step_y) == goal :
                found_goal = True
                return found_goal, temporary_tracer
            else: 
                temporary_found_goal, temporary_tracer = depth_limited_first_search((new_step_x, new_step_y), current_depth + 1, depth_limit, goal, temporary_tracer, config)
                if temporary_found_goal == True:
                    return temporary_found_goal, temporary_tracer 
    return False, [] 

def iterative_deepening_search(ground, source, goal) : 
    goal_found = False
    x, y = source
    source = (x, y)
    max_deep = ground.shape[0] * ground.shape[1]
    for depth_limit in range(max_deep):
        config = searching_config(ground)
        config.is_visited[x][y] = 1
        current_depth = 0
        current_point = source
        temporary_found_goal, temporary_tracer = depth_limited_first_search(current_point, current_depth, depth_limit, goal, [], config)
        if temporary_found_goal:
            for i, point in enumerate(temporary_tracer):
                ground[point[0]][point[1]] = config.path_notation
            return ground


    return ground