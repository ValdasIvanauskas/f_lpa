import random
import sys
sys.path.append('c:\\temp\\f_kastar')
sys.path.append('c:\\temp\\f_grid')
sys.path.append('c:\\temp\\f_lpa')

import u_lists
import u_grid
import u_graph

from kastar import KAStar
from c_lpa import LPA

path_map_1 = 'c:\\temp\\maps\\lak109d.map'


def get_grid_from_map(path_map):
    lists = u_lists.to_lists_mask(path_map,'.')
    grid = u_grid.lists_to_grid(lists)
    return u_grid.canonize(grid)


def get_random_start_goals(grid):
    idds = u_grid.get_valid_idds(grid)
    random.shuffle(idds)
    start = idds[0]
    goal_1 = idds[1]
    goal_2 = idds[2]
    return start, {goal_1, goal_2}


def get_kastar_nodes(grid, start, goals):    
    kastar = KAStar(grid, start, goals)
    kastar.run()
    return len(kastar._closed)


def get_lpa_nodes(grid, start, goals):
    goal_1, goal_2 = goals
    graph = u_graph.grid_to_graph(grid,start,goal_1)
    node_start = graph.nodes[start]
    node_goal_1 = graph.nodes[goal_1]
    node_goal_2 = graph.nodes[goal_2]
    node_dummy = graph.nodes[999]
    lpa = LPA(graph, node_start, node_dummy)
    lpa.run()
    graph.add_edge(node_goal_1,node_dummy,float('Infinity'))
    graph.add_edge(node_goal_2,node_dummy,0)
    for idd in u_grid.get_valid_idds(grid):
        graph.nodes[idd].h = u_grid.manhattan_distance(grid,idd,goal_2)
    lpa.update_node(node_dummy)
    lpa.run()
    return 0


grid = get_grid_from_map(path_map_1)
start, goals = get_random_start_goals(grid)

grid = u_grid.gen_symmetric_grid(3)
start, goals = 0,{2,8}
print(start,goals)
print(get_kastar_nodes(grid, start, goals))
print(get_lpa_nodes(grid, start, goals))