# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:59 2020

@author: User
"""

"""
===============================================================================
===============================================================================
=========================  Tester  ============================================
===============================================================================
===============================================================================
"""
def tester():
    
    import sys
    sys.path.append('c:\\python modules\\f_utils')
    
    import u_tester
    from c_edges import Edges
    
    def tester_generate():
        
        edges = Edges()
        edges.add(idd_1=1, idd_2=2, cost=10)
        
        node_1 = Node(idd=1, h=None, c=c)
        node_1.generate(father=None)
        
        node_2 = Node(idd=2, h=None, c=c)
        node_2.generate(father=node_1)
    
        p0 = node_1.g == 0
        p1 = node_1.father == None
        p2 = node_2.g == 10
        p3 = node_2.father == node_1
        
        u_tester.run([p0,p1,p2,p3])
        
        
    def tester_update():
        
        edge_1 = Edge(idd_1=1, idd_2=4, cost=10)
        edge_2 = Edge(idd_1=2, idd_2=4, cost=20)
        edge_3 = Edge(idd_1=3, idd_2=4, cost=5)
        edges = [edge_1, edge_2, edge_3]
        c = Edges(edges)
        
        node_1 = Node(idd=1, h=None, c=c)
        node_1.generate(father=None)      
        
        node_2 = Node(idd=2, h=None, c=c)
        node_2.generate(father=None)
        
        node_3 = Node(idd=3, h=None, c=c)
        node_3.generate(father=None)
        
        node_4 = Node(idd=4, h=None, c=c)
        node_4.generate(father=node_1)
        
        # Node_2 is less attractive father from Node_1
        node_4.update(node_2)
        p0 = node_4.father == node_1
        p1 = node_4.g == 10
        
        # Node_3 is more attractive father from Node_1
        node_4.update(node_3)
        p2 = node_4.father == node_3
        p3 = node_4.g == 5
        
        u_tester.run([p0,p1,p2,p3])
        
    
    def tester_rhs():
        
        edge = Edge(idd_1=1, idd_2=2, cost=10)
        c = Edges([edge])
        
        node_1 = Node(idd=1, h=None, c=c)
        node_1.generate(father=None)
        
        node_2 = Node(idd=2, h=None, c=c)
        node_2.generate(father=node_1)
        
        couple = frozenset({node_1.idd,node_2.idd})
        c._edges[couple] = 5
        
        # G holds old value and RHS updated with a new value
        p0 = node_2.g == 10
        p1 = node_2.rhs() == 5
        
        u_tester.run([p0,p1])
        
        
    def tester_f():
        
        edge = Edge(idd_1=1, idd_2=2, cost=10)
        c = Edges([edge])
        
        node_1 = Node(idd=1, h=None, c=c)
        node_1.generate(father=None)
        
        node_2 = Node(idd=2, h=100, c=c)
        node_2.generate(father=node_1)
        
        couple = frozenset({node_1.idd,node_2.idd})
        c._edges[couple] = 5
        
        # G holds old value and RHS updated with a new value
        p0 = node_2.f() == 105
        
        u_tester.run([p0])
        
        
    def tester_eq():
        
        node_1 = Node(idd=1)
        node_2 = Node(idd=2)
        node_3 = node_1
        
        p0 = node_1 == node_3
        p1 = not (node_1 == node_2)
        
        u_tester.run([p0,p1])
        
        
    def tester_ne():
        
        node_1 = Node(idd=1)
        node_2 = Node(idd=2)
        node_3 = node_1
        
        p0 = not node_1 != node_3
        p1 = node_1 != node_2
        
        u_tester.run([p0,p1])
        
        
    def tester_lt():
        
        node_1 = Node(idd=1, h=100)
        node_1.generate(father=None)
        
        node_2 = Node(idd=2, h=200)
        node_2.generate(father=None)
        
        # node_1.f < node_2.f
        p0 = node_1 < node_2
        
        edge_1 = Edge(idd_1=1, idd_2=2, cost=90)
        edge_2 = Edge(idd_1=3, idd_2=4, cost=10)
        edges = [edge_1, edge_2]
        c = Edges(edges)
        
        father_1 = Node(idd=1)
        father_1.generate(father=None)
        
        node_1 = Node(idd=2, h=10, c=c)
        node_1.generate(father=father_1)
        
        father_2 = Node(idd=3)
        father_2.generate(father=None)
        
        node_2 = Node(idd=4, h=90, c=c)
        node_2.generate(father=father_2)
        
        # node_1.f == node_2.f and node_1.g > node_2.g
        p1 = node_1 < node_2        
        
        father_3 = Node(idd=5)
        
        u_tester.run([p0,p1])
           

    u_tester.print_start(__file__)
    tester_generate()
    tester_update()
    tester_rhs()
    tester_f()
    tester_eq()
    tester_ne()
    tester_lt()
    u_tester.print_finish(__file__)
    
#tester()
        