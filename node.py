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
    
     
    def __init__(self, idd, h, c):
        """
        =======================================================================
         Description: Init Node with Idd.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd : int (Node's Id).
            2. h : float (Heuristic toward Goal Node).
            3. c : Edges (Edges between the Nodes and their Costs).
        =======================================================================
        """
        self.idd = idd
        self.h = h
        self.c = c
    

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

    
    def rhs(self):
        """
        =======================================================================
         Description: Return RHS-Value of the Node.
        =======================================================================
         Return: float (RHS-Value of the Node).
        =======================================================================
        """
        ans = float('Infinity')
        for neighbor in self.c.get_neighbors(self.idd):
            cost = self.c.get_cost(self.idd, neighbor)
            ans = min(ans, cost)
        return ans
    
    
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
    sys.path.append('c:\\python modules\\f_utils')
    
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
        
        c._edges[frozenset({node_1.idd,node_2.idd})] = 5
        
        # G holds old value and RHS updated with a new value
        p0 = node_2.g == 10
        p1 = node_2.rhs() == 5
        
        u_tester.run([p0,p1])
           

    u_tester.print_start(__file__)
    tester_generate()
    tester_update()
    tester_rhs()
    u_tester.print_finish(__file__)
    
tester()
        