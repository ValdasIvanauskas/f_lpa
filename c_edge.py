class Edge:
    """
    ===========================================================================
     Description: Edge of two Nodes.
    ===========================================================================
     Attributes:
    ---------------------------------------------------------------------------
        1. idd_1 : int (First Node's Id).
        2. idd_2 : int (Second Node's Id).
        3. cost : float (Cost to move between the Nodes). 
    ===========================================================================
    """
    
    def __init__(self, idd_1, idd_2, cost):
        """
        =======================================================================
         Description: Constructor (Init the Edge with 2 Nodes and the Cost).
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd_1 : int (First Node's Id).
            2. idd_2 : int (Second Node's Id).
            3. cost : float (Cost to move between the Nodes).
        =======================================================================
        """
        self.idd_1 = idd_1
        self.idd_2 = idd_2
        self.cost = cost