from c_node import Node
from c_edges import Edges

import sys
sys.path.append('c:\\python modules\\f_utils')
#sys.path.append('c:\\temp\\today\\f_utils')
#sys.path.append('g:\\python modules\\f_utils')

import u_tester


def tester_add():
    
    node_1 = Node(1)
    node_2 = Node(2)
    edges = Edges()
    edges.add(node_1, node_2, cost=10)
    
    p0 = edges.cost(node_1, node_2) == 10
    
    node_3 = Node(3)
    p1 = edges.cost(node_1, node_3) == float('Infinity')
    
    u_tester.run([p0,p1])
        
        
def tester_cost():
    
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    
    edges = Edges()
    edges.add(node_1, node_2, cost=3)
    edges.add(node_1, node_3, cost=4)
    
    p0 = edges.cost(node_1, node_2) == 3
    p1 = edges.cost(node_1, node_3) == 4
    
    node_4 = Node(4)
    p2 = edges.cost(node_1, node_4) == float('Infinity')
 
    u_tester.run([p0,p1,p2])            
       

def tester_neighbors():
    
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    
    edges = Edges()
    edges.add(node_1, node_2)
    edges.add(node_1, node_3)
    
    p0 = edges.neighbors(node_1) == {node_2,node_3}
    p1 = edges.neighbors(node_2) == {node_1}
    p2 = edges.neighbors(node_3) == {node_1}
    
    node_4 = Node(4)
    p3 = edges.neighbors(node_4) == set()
    
    u_tester.run([p0,p1,p2,p3])
    

u_tester.print_start(__file__)
tester_add()
tester_cost()
tester_neighbors()
u_tester.print_finish(__file__)
        
        