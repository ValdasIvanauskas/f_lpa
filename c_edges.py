class Edges:
    """
    ===========================================================================
     Description: Class of Graph Edges.
    ===========================================================================
     Methods:
    ---------------------------------------------------------------------------
        1. add(node, node, float) -> None [Add New \ Update Edge]
        2. get_cost(node, node) -> float [Return Cost of the Edge].
        3. get_neighbors(node) -> list of Node [Return List of Neighbor Nodes].
    ===========================================================================
    """
    
    def __init__(self):
        """
        =======================================================================
         Description: Constructor (Init the private dictionaries).
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. edges : list of Edges.
        =======================================================================
        """
        self._cost = dict()
        self._neighbors = dict()                               
        
        
    def add(self, node_1, node_2, cost=float('Infinity')):
        """
        =======================================================================
         Description: Add new Edge.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. node_1 : int (First Node).
            2. node_2 : int (Second Node).
            3. cost : float (The Cost of the Edge).
        =======================================================================
        """
        
        # Fill the _edges Dictionary
        couple = frozenset({node_1, node_2})
        self._cost[couple] = cost
        
        # Fill the _neighbors Dictionary
        if not self._neighbors.get(node_1):
            self._neighbors[node_1] = set()
        if not self._neighbors.get(node_2):
            self._neighbors[node_2] = set()
        self._neighbors[node_1].add(node_2)
        self._neighbors[node_2].add(node_1)
        
        
    def cost(self, node_1, node_2):
        """
        =======================================================================
         Description: Return the Cost to move from Node idd_1 to Node idd_2.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. node_1 : Node (First Node).
            2. node_2 : Node (Second Node).
        =======================================================================
         Return : float (The Cost to move from Node idd_1 to Node idd_2).
        =======================================================================
        """        
        couple = frozenset({node_1, node_2})
        if self._cost.get(couple):
            return self._cost[couple]
        return float('Infinity')
    
    
    def neighbors(self, node):
        """
        =======================================================================
         Description: Return List of Node's Neighbors.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. node : Node.
        =======================================================================
         Return : set of Node (Set of Neighbors).
        =======================================================================
        """
        if self._neighbors.get(node):
            return self._neighbors[node]
        return set()
