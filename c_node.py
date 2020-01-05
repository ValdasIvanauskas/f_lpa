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
    
     
    def __init__(self, idd, h=float('Infinity')):
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
        self.g = float('Infinity')
    

    def set_graph(self, graph):
        self.graph = graph
        
        
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
            self.g = father.g + self.graph.cost(self, father)
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
        g_new = father.g + self.graph.cost(self, father)
        if (self.g > g_new):
            self.father = father
            self.g = g_new
    
    
    def f(self):
        """
        =======================================================================
         Description: Return F value of the Node (g + h).
        =======================================================================
         Return: float
        =======================================================================
        """
        return min(self.g, self.graph.rhs(self)) + self.h
        
    
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
            cost_self = min(self.g, self.graph.rhs(self))
            cost_other = min(other.g, other.graph.rhs(other))
            if cost_self >= cost_other:
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
    
    
