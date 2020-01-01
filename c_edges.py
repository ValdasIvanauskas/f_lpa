import sys
#sys.path.append('c:\\python modules\\f_utils')
sys.path.append('c:\\temp\\today\\f_utils')

from c_edge import Edge

class Edges:
    """
    ===========================================================================
     Description: Class of Graph Edges.
    ===========================================================================
     Attributes:
    ---------------------------------------------------------------------------
        1. edges : Dict (Key=FrozenSet(The Two Nodes Id), Val=Cost).
        2. neighbors : Dict (Key=Node's Id, Val=List of Neighbors Nodes Id).
    ===========================================================================
    """
    
    def __init__(self, edges=list()):
        """
        =======================================================================
         Description: Constructor (Init the Dict of Edges).
        =======================================================================
         Arguments:
        -----------------------------------------------------------------------
            1. edges : list of Edges.
        =======================================================================
        """
        self._edges = dict()
        self._neighbors = dict()
        for edge in edges:
            idd_1 = edge.idd_1
            idd_2 = edge.idd_2
            cost = edge.cost
            nodes = frozenset([idd_1, idd_2])
            
            # Fill the Edges Dictionary
            self._edges[nodes] = cost
            
            # Fill the Neighbors Dictionary
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
        s = frozenset({idd_1, idd_2})
        return self._edges[s]
    
    
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
        return self._neighbors[idd]
    
"""
===============================================================================
===============================================================================
===========      Tester     ===================================================
===============================================================================
===============================================================================
"""
def tester():
    
    import u_tester
    
    def tester_get_cost():
        
        idd_1 = 1
        idd_2 = 2
        idd_3 = 3
        edge_1 = Edge(idd_1, idd_2, 3)
        edge_2 = Edge(idd_1, idd_3, 4)
        edges = [edge_1, edge_2]        
        edges_test = Edges(edges)
        
        cost = edges_test.get_cost(idd_1,idd_2)
        p0 = cost == 3
        
        cost = edges_test.get_cost(idd_3, idd_1)
        p1 = cost == 4
        
        u_tester.run([p0,p1])
        
    
    def tester_get_neighbors():
        
        idd_1 = 1
        idd_2 = 2
        idd_3 = 3
        edge_1 = Edge(idd_1, idd_2, 3)
        edge_2 = Edge(idd_1, idd_3, 4)
        edges = [edge_1, edge_2]        
        edges_test = Edges(edges)
        
        neighbors = edges_test.get_neighbors(idd_1)
        p0 = neighbors == [idd_2, idd_3]
        
        neighbors = edges_test.get_neighbors(idd_2)
        p1 = neighbors == [idd_1]
        
        neighbors = edges_test.get_neighbors(idd_3)
        p2 = neighbors == [idd_1]
        
        u_tester.run([p0,p1,p2])
        
    
    u_tester.print_start(__file__)
    tester_get_cost()
    tester_get_neighbors()
    u_tester.print_finish(__file__)
        
#tester()        