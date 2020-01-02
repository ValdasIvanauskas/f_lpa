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
    p1 = graph.cost(node_2, node_1) == 10
    
    u_tester.run([p0,p1])
    
    
def tester_rhs():
    
    father_1 = Node(1)
    father_2 = Node(2)
    node_1 = Node(3)
    nodes = [father_1, father_2, node_1]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(father_1, node_1, cost=10)
    
    father_1.generate()
    father_2.generate()
    node_1.generate(father_1)
    
    p0 = True#graph.rhs(father_1) == float('Infinity')
    
    graph.add_edge(father_2, node_1, cost=5)
    p1 = graph.rhs(node_1) == 5
    
    graph.add_edge(node_1, father_2, cost=3)
    p2 = graph.rhs(node_1) == 3
    
    u_tester.run([p0,p1,p2])
    
    
u_tester.print_start(__file__)
tester_add_nodes()
tester_add_edge()
tester_cost()
tester_rhs()
u_tester.print_finish(__file__)