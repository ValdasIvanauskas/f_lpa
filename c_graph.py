class Graph:
    
    def __init__(self, start=None):
        """
        =======================================================================
         Description: Constructor (Init Attributes).
        =======================================================================
        """
        self.nodes = dict()
        self._cost = dict()
        self.neighbors = dict()
        self.start = start
    
    
    def add_nodes(self, nodes):
        """
        =======================================================================
         Description: Add Nodes to the Graph.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. nodes : list of Node.
        =======================================================================
        """
        for node in nodes:
            self.nodes[node.idd] = node
            node.set_graph(self)
    
    
    def add_edge(self, node_1, node_2, cost=float('Infinity')):
        """
        =======================================================================
         Description: Add Edge to the Graph.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. node_1 : Node (First Node of the Edge).
            2. node_2 : Node (Second Node of the Edge).
            3. cost : float (Cost of the Edge).
        =======================================================================
        """
        # Add to _cost dictionary
        couple = frozenset({node_1, node_2})
        self._cost[couple] = cost
        
        # Add to _neighbors dictionary
        if self.neighbors.get(node_1):
            self.neighbors[node_1].add(node_2)
        else:
            self.neighbors[node_1] = {node_2}
            
        if self.neighbors.get(node_2):
            self.neighbors[node_2].add(node_1)
        else:
            self.neighbors[node_2] = {node_1}
        
    
    def cost(self, node_1, node_2):
        """
        =======================================================================
         Description: Return the real Cost from Node_1 to Node_2.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. node_1 : Node.
            2. node_2 : Node.
        =======================================================================
         Return: float (The real Cost from Node_1 to Node_2).
        =======================================================================
        """
        couple = frozenset({node_1, node_2})
        return self._cost[couple]
    
    
    def rhs(self, node):
        """
        =======================================================================
         Description: Return the RHS-Value of the Node.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. node : Node.
        =======================================================================
         Return: float (RHS-Value of the Node).
        =======================================================================
        """
        if self.start:
            if node == self.start:
                return 0
        ans = float('Infinity')
        for neighbor in self.neighbors[node]:
            cost = neighbor.g + self.cost(node, neighbor)
            ans = min(ans, cost)
        return ans
   