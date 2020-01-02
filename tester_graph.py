from c_node import Node
from c_edges import Edges
from c_graph import Graph

import u_tester
    

def tester_add_nodes():
    
    node_1 = Node(1)
    node_2 = Node(2)
    nodes = [node_1, node_2]
    
    graph = Graph()
    graph.add_nodes(nodes)
    
    p0 = graph.nodes[1] == node_1
    p1 = graph.nodes[2] == node_2
    
    u_tester.run([p0,p1])
    
    
def tester_add_edge():
    
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    nodes = [node_1, node_2, node_3]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(node_1, node_2)
    graph.add_edge(node_1, node_3)
    
    p0 = graph.neighbors[node_1] == {node_2, node_3}
    p1 = graph.neighbors[node_2] == {node_1}
    
    u_tester.run([p0,p1])
    
    
def tester_cost():
    
    node_1 = Node(1)
    node_2 = Node(2)
    nodes = [node_1, node_2]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(node_1, node_2, cost=10)
    
    p0 = graph.cost(node_1, node_2) == 10
    
    u_tester.run([p0])
    
    
u_tester.print_start(__file__)
tester_add_nodes()
tester_add_edge()
tester_cost()
u_tester.print_finish(__file__)