#  A* Search Algorithms f = g plus h
# At each step, pick the node with the smallest value of ‘f’ 
# (the sum of ‘g’ and ‘h’) and processes that node/cell. 
# ‘g’ and ‘h’ is defined as simply as possible below:
# Whereas
# g’ is the distance it takes to get to a certain square on the grid 
# from the starting point, following the path we generated to get there. 
# ‘h’ is the heuristic, which is the estimation of the distance 
# it takes to get to the finish line from that square on the grid.

# f(n) = g(n) + h(n), where :

# g(n) = cost of traversing from one node to another. This will vary from node to node

# h(n) = heuristic approximation of the node's value. 
#     This is not a real value but an approximation cost

# Manhattan distance:

# h = abs (curr_cell.x – goal.x) + abs (curr_cell.y – goal.y)
# We must use this heuristic method when we are only permitted to move 
# in four directions - top, left, right, and bottom.



# Return heuristic distance for all nodes

def heuristic(node):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    if node in H_dist.keys():
        return H_dist[node]
    else:
        pass


# Describe graph
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'C': [('B', 2)],
    'D': [('B', 2)],

}
# aStarAlgo('A', 'G')

print(heuristic('A'))