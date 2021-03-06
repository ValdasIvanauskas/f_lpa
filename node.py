from c_edges import Edges

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
    
     
    def __init__(self, idd, h=float('Infinity'), edges=Edges()):
        """
        =======================================================================
         Description: Init Node with Idd.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd : int (Node's Id).
            2. h : float (Heuristic toward Goal Node).
            3. edges : Edges (Edges between the Nodes).
        =======================================================================
        """
        self.idd = idd
        self.h = h
        self._edges = edges
    

    def generate(self, father=None):
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
            self.g = father.g + self._cost(father.idd)
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
        g_new = father.g + self._cost(father.idd)
        if (self.g > g_new):
            self.father = father
            self.g = g_new
    
    
    def rhs(self):
        """
        =======================================================================
         Description: Return RHS-Value of the Node.
        =======================================================================
         Return: float (RHS-Value of the Node).
        =======================================================================
        """
        ans = float('Infinity')
        for idd_neighbor in self._neighbors():
            cost = self._cost(idd_neighbor)
            ans = min(ans, cost)
        return ans
    
    
    def f(self):
        """
        =======================================================================
         Description: Return F value of the Node (g + h).
        =======================================================================
         Return: float
        =======================================================================
        """
        return min(self.g,self.rhs()) + self.h
    
    
    def _cost(self, idd_other):
        """
        =======================================================================
         Description: Return the Cost from Self to Other Node.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. other : Node
        =======================================================================
         Return: float (The Cost from Self to Other Node).
        =======================================================================
        """
        return self._edges.get_cost(self.idd, idd_other)
    
    
    def _neighbors(self):
        """
        =======================================================================
         Description: Return List of Neighbors Id of the Self.
        =======================================================================
         Return: list of int (List of Neighbors Id of the Self).
        =======================================================================
        """
        return self._edges.get_neighbors(self.idd)
    
    
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
            if (min(self.g,self.rhs()) >= min(other.g,other.rhs())):
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
    
tester()
        