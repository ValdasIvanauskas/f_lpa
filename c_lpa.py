from c_opened import Opened

class LPA:
    
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
   
        self.opened = Opened()
        self.opened.push(start)
        
    
    def run(self):
        self.counter = 0
        self.compute_shortest_path()
        print('\ncounter = {0}\n'.format(self.counter))
    
    def compute_shortest_path(self):
        
        while (not self.opened.is_empty()) and (self.opened.best < self.goal or self.graph.rhs(self.goal) != self.goal.g):
            best = self.opened.pop()
            if (best.g > self.graph.rhs(best)):
                best.g = self.graph.rhs(best)
            else:
                best.g = float('Infinity')
                self.update_node(best)
            if self.graph.succ.get(best):
                for neighbor in self.graph.succ[best]:
                    self.update_node(neighbor)
            self.graph.print()
            print('Opened={0}'.format(self.opened))
            self.counter += 1
        
        
    def update_node(self, node):
        if self.opened.contains(node):
            self.opened.remove(node)
        if node.g != self.graph.rhs(node):
            self.opened.push(node)
            
        
    
"""
===============================================================================
===============================================================================
==========      Tester      ===================================================
===============================================================================
===============================================================================
"""
def tester():

    import sys
    sys.path.append('g:\\python modules\\f_utils')
    import u_tester
    
    from c_node import Node
    from c_graph import Graph
    
    def tester_run():
        node_start = Node(1,2)
        node_a = Node(2,5)
        node_b = Node(3,1)
        node_goal = Node(4,0)
        nodes = [node_start, node_a, node_b, node_goal]
        
        graph = Graph(start=node_start)
        graph.add_nodes(nodes)
        graph.add_edge(node_start, node_a, 5)
        graph.add_edge(node_start, node_b, 6)
        graph.add_edge(node_a, node_goal, 5)
        graph.add_edge(node_b, node_goal, 6)
        
        lpa = LPA(graph, node_start, node_goal)
        lpa.run()
        
    def tester_run_2():
        node_start = Node(1,3)
        node_a = Node(2,2)
        node_g1 = Node(3,0)
        node_b = Node(4,2)
        node_g2 = Node(5,0)
        node_dummy = Node(6,0)
        nodes = [ node_start, node_a, node_g1, node_b, node_g2, node_dummy ]
        
        graph = Graph(node_start)
        graph.add_nodes(nodes)
        graph.add_edge(node_start, node_a, 10)
        graph.add_edge(node_start, node_b, 8)
        graph.add_edge(node_a, node_g1, 10)
        graph.add_edge(node_b, node_g2, 8)
        graph.add_edge(node_g1, node_dummy, 0)
        graph.add_edge(node_g2, node_dummy, float('Infinity'))
        graph.add_edge(node_a, node_start, 10)
        graph.add_edge(node_b, node_start, 8)
        graph.add_edge(node_g1, node_a, 10)
        graph.add_edge(node_g2, node_b, 8)
        graph.add_edge(node_dummy, node_g1, 0)
        graph.add_edge(node_dummy, node_g2, float('Infinity'))
        
        lpa = LPA(graph, node_start, node_dummy)
        lpa.run()
        graph.add_edge(node_g1, node_dummy, float('Infinity'))
        graph.add_edge(node_g2, node_dummy, 0)
        graph.add_edge(node_dummy, node_g1, float('Infinity'))
        graph.add_edge(node_dummy, node_g2, 0)
        #node_a.h = float('Infinity')
        #node_g1.h = float('Infinity')
        #node_b.h = 1
        #node_g2.h = 0
        lpa.update_node(node_dummy)
        lpa.update_node(node_g1)
        lpa.update_node(node_g2)
        print('edges changed\n')
        lpa.run()
     
        
    u_tester.print_start(__file__)
    #tester_run()
    tester_run_2()
    u_tester.print_finish(__file__)
  
#tester()
        
        
    
    