import sys
sys.path.append('c:\\python modules\\f_utils')
import u_tester

from c_node import Node
from c_graph import Graph


def tester_generate():
    
    node_1 = Node(1)
    node_2 = Node(2)
    nodes = [node_1, node_2]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(node_1, node_2, cost=10)
    
    node_1.generate()
    p0 = node_1.father == None
    p1 = node_1.g == 0
    
    node_2.generate(father=node_1)
    p2 = node_2.father == node_1
    p3 = node_2.g == 10   
    
    u_tester.run([p0,p1,p2,p3])
    
    
def tester_update():
    
    father_1 = Node(1)
    father_2 = Node(2)
    node_1 = Node(3)
    nodes = [father_1, father_2, node_1]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(father_1, node_1, 20)
    graph.add_edge(father_2, node_1, 10)
    
    father_1.generate()
    node_1.generate(father=father_1)
    
    father_2.generate()
    node_1.update(father=father_2)
    
    p0 = node_1.father = father_2
    p1 = node_1.g == 10
    
    u_tester.run([p0,p1])
    
    
def tester_f():
    
    node_1 = Node(idd=1, h=100)
    node_2 = Node(idd=2, h=100)
    nodes = [node_1, node_2]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(node_1, node_2, 10)
    
    node_1.generate()
    node_2.generate(father=node_1)
    
    p0 = node_1.f() == 100
    p1 = node_2.f() == 110
    
    graph.add_edge(node_1, node_2, 5)
    p2 = node_2.f() == 105
    
    u_tester.run([p0,p1,p2])
    
    
def tester_lt():
    
    father_1 = Node(idd=1, h=200)
    father_2 = Node(idd=2, h=200)
    
    node_1 = Node(idd=3, h=10)
    node_2 = Node(idd=4, h=90)
    nodes = [father_1, father_2, node_1, node_2]
    
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edge(father_1, node_1, cost=90)
    graph.add_edge(father_2, node_2, cost=10)
    
    father_1.generate()
    father_2.generate()
    node_1.generate(father_1)
    node_2.generate(father_2)
    
    p0 = node_1 < father_1
    p1 = node_1 < node_2
    
    graph.add_edge(father_2, node_2, cost=5)
    p2 = node_2 < node_1
    
    u_tester.run([p0,p1,p2])
    
    
    
    
u_tester.print_start(__file__)
tester_generate()
tester_update()
tester_f()
tester_lt()
u_tester.print_finish(__file__)