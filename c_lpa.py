from c_opened import Opened

class LPA:
    
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
   
        self.opened = Opened()
        self.opened.push(start)
        
    
    def run(self):
        self.compute_shortest_path()
    
    
    def compute_shortest_path(self):
        while (self.opened.best < self.goal or self.graph.rhs(self.goal) != self.goal.g):
            best = self.opened.pop()
            if (best.g > self.graph.rhs(best)):
                best.g = self.graph.rhs(best)
            else:
                best.g = float('Infinity')
                self.update_node(best)
            for neighbor in self.graph.neighbors[best]:
                self.update_node(neighbor)
            print(best)
        print('finish')
        
        
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
    sys.path.append('c:\\python modules\\f_utils')
    import u_tester
    
    from c_node import Node
    from c_graph import Graph
    
    def tester_run():
        node_start = Node(1,2)
        node_a = Node(2,10)
        node_b = Node(3,7)
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
     
        
    u_tester.print_start(__file__)
    tester_run()
    u_tester.print_finish(__file__)
  
tester()
        
        
    
    