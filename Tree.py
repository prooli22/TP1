"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.

   Pris dans Goodrich, Tamassia & Goldwasser
   Data Structures & Algorithms in Python (c)2013
"""
#from ListQueue import ListQueue
    
#ADT Tree "interface"
class Tree:

    #inner class position
    class Position:

        def element( self ):
            pass

        def __eq__( self, other ):
            pass

        def __ne__( self, other):
            return not( self == other )

    #get the root
    def root( self ):
        pass

    #get the parent
    def parent( self, p ):
        pass

    #get the number of children
    def num_children( self, p ):
        pass

    #get the children
    def children( self, p ):
        pass

    #get the number of nodes
    def __len__( self ):
        pass

    #ask if a position is the root
    def is_root( self, p ):
        return self.root() == p

    #ask if a position is a leaf
    def is_leaf( self, p ):
        return self.num_children( p ) == 0

    #ask if the tree is empty
    def is_empty( self ):
        return len( self ) == 0

    #get the depth of a position
    def depth( self, p ):
        #returns the number of ancestors of p
        if self.is_root( p ):
            return 0
        else:
            return 1 + self.depth( self.parent() )

    #get the height of a position using depth (not efficient)
    def height1( self, p ):
        #returns the maximum depth of the leaf positions
        return max( self.depth( p ) for p in self.positions() if self.is_leaf( p ))

    #get the height of a position by descending the tree (efficient)
    def height( self, p ):
        #returns the height of the subtree at Position p
        if self.is_leaf( p ):
            return 0
        else:
            return 1 + max( self.height( c ) for c in self.children( p ) )

    #print the subtree rooted by position p
    #using a preorder traversal
    def preorder_print( self, p, indent = "" ):
        print( indent + str( p ) )
        for c in self.children( p ):
            self.preorder_print( c, indent + "    " )

    #print the subtree rooted by position p
    #using a postorder traversal
    def postorder_print( self, p ):
        for c in self.children( p ):
            self.postorder_print( c )
        print( p )

    #print the subtree rooted by position p
    #using a breadth-first traversal
    # def breadth_first_print( self ):
    #     Q = ListQueue()
    #     Q.enqueue( self.root() )
    #     while not Q.is_empty():
    #         p = Q.dequeue()
    #         print( p )
    #         for c in self.children( p ):
    #             Q.enqueue( c )
            
