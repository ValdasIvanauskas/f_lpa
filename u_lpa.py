import sys
sys.path.append('g:\\python modules\\f_grid')

import u_grid
import numpy as np

import u_graph
from c_node import Node
from c_lpa import LPA


li_1 = [0,1,2,3,4]
li_2 = [5,6,-1,8,9]
li_3 = [10,11,-1,13,14]
li_4 = [15,16,-1,18,19]
li_5 = [20,21,22,23,24]
li = [li_1, li_2, li_3, li_4, li_5]

grid = np.array(li)
idd_start = 11
idd_goal_1 = 8
idd_goal_2 = 18

graph = u_graph.grid_to_graph(grid, idd_start, idd_goal_1)
node_goal_1 = graph.nodes[idd_goal_1]
node_goal_2 = graph.nodes[idd_goal_2]
node_dummy = graph.nodes[999]

graph.add_edge(node_goal_1, node_dummy, 0)
graph.add_edge(node_dummy, node_goal_1, 0)
graph.add_edge(node_goal_2, node_dummy, float('Infinity'))
graph.add_edge(node_dummy, node_goal_2, float('Infinity'))

lpa = LPA(graph, graph.start, node_dummy)
lpa.run()
graph.add_edge(node_goal_1, node_dummy, float('Infinity'))
graph.add_edge(node_dummy, node_goal_1, float('Infinity'))
graph.add_edge(node_goal_2, node_dummy, 0)
graph.add_edge(node_dummy, node_goal_2, 0)
for node in set(graph.nodes.values())-{node_dummy}:
    node.h = u_grid.manhattan_distance(grid,node.idd,idd_goal_2)
node_dummy.g = float('Infinity')
lpa.update_node(node_dummy)
lpa.update_node(node_goal_1)
lpa.update_node(node_goal_2)

print('\nEdges have been changed\n')
graph.print()
print('Opened={0}'.format(lpa.opened))

lpa.run()
