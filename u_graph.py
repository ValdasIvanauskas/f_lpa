import sys
sys.path.append('g:\\python modules\\f_grid')
import u_grid

from c_graph import Graph
from c_node import Node

def grid_to_graph(grid, idd_start, idd_goal_1):
    
    node_start = Node(idd_start,u_grid.manhattan_distance(grid,idd_start,idd_goal_1))
    graph = Graph(node_start)
    
    nodes = list()
    for idd in u_grid.get_valid_idds(grid):
        h = u_grid.manhattan_distance(grid,idd,idd_goal_1)
        node = Node(idd,h,graph)
        nodes.append(node)
    node_dummy = Node(999,0,graph)
    nodes.append(node_dummy)
    graph.add_nodes(nodes)
    graph.start = graph.nodes[idd_start]
    
    for idd in u_grid.get_valid_idds(grid):
        row, col = u_grid.to_row_col(grid, idd)
        for neighbor in u_grid.get_neighbors(grid, row, col):
            node_1 = graph.nodes[idd]
            node_2 = graph.nodes[neighbor]
            graph.add_edge(node_1, node_2, cost=1)
            graph.add_edge(node_2, node_1, cost=1)
    node_goal_1 = graph.nodes[idd_goal_1]
    graph.add_edge(node_goal_1,node_dummy,0)
    
    return graph
        




