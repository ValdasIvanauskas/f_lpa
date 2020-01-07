class Graph:
    
    def __init__(self, start=None):
        """
        =======================================================================
         Description: Constructor (Init Attributes).
        =======================================================================
        """
        self.nodes = dict()
        self.cost = dict()
        self.pred = dict()
        self.succ = dict()
        self.start = start
    
    
    def print(self):
        for node in self.nodes.values():
            idd = node.idd
            g = node.g
            rhs = self.rhs(node)
            f = node.f()
            print('idd={0}, g={1}, rhs={2}, f={3}'.format(idd,g,rhs,f))
        print()
    
    
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
            #node.set_graph(self)
    
    
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
        # Add to cost dictionary
        self.cost[(node_1,node_2)] = cost
        
        # Add to _neighbors dictionary
        if self.succ.get(node_1):
            self.succ[node_1].add(node_2)
        else:
            self.succ[node_1] = {node_2}
            
        if self.pred.get(node_2):
            self.pred[node_2].add(node_1)
        else:
            self.pred[node_2] = {node_1}
    
    
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
        for neighbor in self.pred[node]:
            cost = neighbor.g + self.cost[(neighbor, node)]
            ans = min(ans, cost)
        return ans
   