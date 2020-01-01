

from c_edge import Edge

class Edges:
    """
    ===========================================================================
     Description: Class of Graph Edges.
    ===========================================================================
     Methods:
    ---------------------------------------------------------------------------
        1. get_cost(int, int) -> float [Return Cost of the Edge].
        2. set_cost(int, int, float) -> None [Set new Cost to the Edge].
        3. get_neighbors(int) -> list of int [Return List of Neighbors Id].
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
        
        
    def add(self, idd_1, idd_2, cost=float('Infinity')):
        """
        =======================================================================
         Description: Add new Edge.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd_1 : int (First Node Id).
            2. idd_2 : int (Second Node Id).
            3. cost : float (The Cost of the Edge).
        =======================================================================
        """
        
        # Fill the _edges Dictionary
        couple = frozenset({idd_1, idd_2})
        self._cost[couple] = cost
        
        # Fill the _neighbors Dictionary
        if not self._neighbors.get(idd_1):
            self._neighbors[idd_1] = list()
        if not self._neighbors.get(idd_2):
            self._neighbors[idd_2] = list()
        self._neighbors[idd_1].append(idd_2)
        self._neighbors[idd_2].append(idd_1)
        
        
    def get_cost(self, idd_1, idd_2):
        """
        =======================================================================
         Description: Return the Cost to move from Node idd_1 to Node idd_2.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd_1 : int (First Node Id).
            2. idd_2 : int (Second Node Id).
        =======================================================================
         Return : float (The Cost to move from Node idd_1 to Node idd_2).
        =======================================================================
        """        
        couple = frozenset({idd_1, idd_2})
        if self._cost.get(couple):
            return self._cost[couple]
        return float('Infinity')
    
    
    def get_neighbors(self, idd):
        """
        =======================================================================
         Description: Return List of Node's Neighbors.
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. idd : int (Node's Id).
        =======================================================================
         Return : list of int (List of Neighbors Id).
        =======================================================================
        """
        if self._neighbors.get(idd):
            return self._neighbors[idd]
        return list()
    
"""
===============================================================================
===============================================================================
===========      Tester     ===================================================
===============================================================================
===============================================================================
"""
def tester():
    
    import sys
    #sys.path.append('c:\\python modules\\f_utils')
    #sys.path.append('c:\\temp\\today\\f_utils')
    sys.path.append('g:\\python modules\\f_utils')

    import u_tester
    
        
    def tester_add():
        
        edges = Edges()
        edges.add(idd_1=1, idd_2=2)
        
        p0 = edges.get_cost(idd_1=1, idd_2=2) == float('Infinity')
        
        u_tester.run([p0])
        
        
    def tester_get_cost():
        
        edges = Edges()
        edges.add(idd_1=1, idd_2=2, cost=3)
        edges.add(idd_1=1, idd_2=3, cost=4)
        
        p0 = edges.get_cost(1,2) == 3
        p1 = edges.get_cost(3,1) == 4
        p2 = edges.get_cost(4,5) == float('Infinity')
        
        u_tester.run([p0,p1,p2])            
           
    
    def tester_get_neighbors():
        
        edges = Edges()
        edges.add(idd_1=1, idd_2=2)
        edges.add(idd_1=1, idd_2=3)
        
        p0 = edges.get_neighbors(idd=1) == [2,3]
        p1 = edges.get_neighbors(idd=2) == [1]
        p2 = edges.get_neighbors(idd=3) == [1]
        p3 = edges.get_neighbors(idd=4) == []
        
        u_tester.run([p0,p1,p2,p3])
        
    
    u_tester.print_start(__file__)
    tester_add()
    tester_get_cost()
    tester_get_neighbors()
    u_tester.print_finish(__file__)
        
tester()        