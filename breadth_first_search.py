import numpy as np


class SimplifiedQueue : 
    def __init__(self, M, N) :
        self.queue = np.zeros((M * N)) 
        self.head_pointer = 0 
        self.tail_pointer = -1 
    def push(self, value) : 
        self.tail_pointer += 1 
        queue[tail_pointer] = value
    def is_empty() : 
        if tail_pointer < head_pointer : 
            return True 
        else:
            return False
    def head(): 
        return queue[self.head_pointer]
    def pop():
        self.head_pointer += 1


def bread_first_search() : 
    pass