class Node:
    """
    ===========================================================================
     Description: Node for Lifelong Planning A* Algorithm.
    ===========================================================================
     Attributes:
    ---------------------------------------------------------------------------
        1. idd : int (Node's Id).
        2. h : float (Heuristic to the Goal Node).
        3. neighbor_cost : dict (key=int (Neighbor's Id), val=float (Cost)).
        4. g : float (Cost from Start Node).
        5. rhs : float (Lookahead value based on the g-values of neighbors).
        6. father : int (Best Father Id).
    ===========================================================================
     Methods:
    ---------------------------------------------------------------------------
        1. f() -> float (Return F-Value of the Node (g+h)).
        2. generate(father) -> None (Set Father and G-Value).
    ===========================================================================
    """ 
    
     
    def __init__(self, idd, c, h):
        """
        =======================================================================
         Description: Init Node with Idd.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd : int (Node's Id).
            2. c : Edges (Edges between the Nodes and their Costs).
            3. h : float (Heuristic toward Goal Node).
        =======================================================================
        """
        self.idd = idd
        self.c = c
        self.h = h
    

    def generate(self, father):
        """
        =======================================================================
         Description: Generate a Node (Set Father and G-Value).
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. father : Node (Father's Node).
        =======================================================================
        """
        self.father = father
        if father:
            self.g = father.g + self.c.get_cost(self.idd, father.idd)
        else:
            self.g = 0
            
        
    def update(self, father):
        """
        =======================================================================
         Description: Update Node values if a candidate father is a more
                         optimal than the current father.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. father : Node (Candidate Father).
        =======================================================================
        """
        cost_father = self.c.get_cost(self.idd, father.idd)
        if (self.g > father.g + cost_father):
            self.father = father
            self.g = father.g + cost_father
    
    
    def f(self):
        """
        =======================================================================
         Description: Return F value of the Node (g + h).
        =======================================================================
         Return: float
        =======================================================================
        """
        return self.g + self.h
    
    
    def __eq__(self, other):
        """
        =======================================================================
         Description: Return True if Self equals to Other.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. other : Node
        =======================================================================
         Return: bool (True if Self equals to Other).
        =======================================================================
        """
        if self.idd == other.idd:
            return True
    
    
    def __ne__(self, other):
        """
        =======================================================================
         Description: Return True if Self not equals to Other.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. other : Node
        =======================================================================
         Return: bool (True if Self not equals to Other).
        =======================================================================
        """
        return not self.__eq__(other)
    
    
    def __lt__(self, other):
        """
        =======================================================================
         Description: Return True if Self is less than Other.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. other : Node
        =======================================================================
         Return: bool (True if Self is less than Other).
        =======================================================================
        """
        if (self.f() < other.f()):
            return True
        if (self.f() == other.f()):
            if (self.g >= other.g):
                return True
        return False
    
    
    def __le__(self, other):
        return self == other or self < other
    
    
    def __gt__(self, other):
        """
        =======================================================================
         Description: Return True if Self is greater than Other.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. other : Node
        =======================================================================
         Return: bool (True if Self is greater than Other).
        =======================================================================
        """
        return not (self < other) and not (self == other)
    
    
    def __ge__(self, other):
        return self == other or self > other
    
    
    def __str__(self):
        return str(self.idd)
    
    
    def __hash__(self):
        return self.idd
    
    
"""
===============================================================================
===============================================================================
=========================  Tester  ============================================
===============================================================================
===============================================================================
"""
def tester():
    
    import sys
    sys.path.append('c:\\temp\\today\\f_utils')
    
    import u_tester
    from c_edge import Edge
    from c_edges import Edges
    
    def tester_generate():
        
        edge = Edge(idd_1=1, idd_2=2, cost=10)
        c = Edges([edge])
        
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
        
        father_1 = Node(1)
        father_1.generate(father=None, h=100, neighbor_cost={4:10})      
        
        father_2 = Node(2)
        father_2.generate(father=None, h=200, neighbor_cost={4:20})
        
        father_3 = Node(3)
        father_3.generate(father=None, h=200, neighbor_cost={4:5})
        
        node = Node(4)
        node.generate(father=father_1, h=100, neighbor_cost={1:10,2:20,3:5})
        
        # Father_2 is less attractive from Father_1
        node.update(father_2)
        p0 = node.father == father_1
        p1 = node.g == 10
        
        # Father_3 is more attractive from Father_1
        node.update(father_3)
        p2 = node.father == father_3
        p3 = node.g == 5
        
        u_tester.run([p0,p1,p2,p3])
           

    u_tester.print_start(__file__)
    tester_generate()
    #tester_update()
    u_tester.print_finish(__file__)
    
tester()
        