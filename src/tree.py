cpt = -1
class Node ( object ):
    def __init__ ( self, value = None ):
        global cpt
        cpt += 1
        self.value = value
        self.cpt = cpt
        self.children = [ ]
        self.is_terminal = False

class Tree ( object ):
    def __init__ ( self ):
        self._root = Node ( )

    def insert ( self, data ):
        self._insertValues ( data, self._root )

    def _insertValues ( self, data, currNode ):
        if not data:
            return

        if currNode and not currNode.value:
            tmpChild = None

            for child in currNode.children:
                if data [ 0 ] == child.value:
                    tmpChild = child
                    break

            if tmpChild:
                self._insertValues ( data, tmpChild )
            else:
                newNode = Node ( value = data [ 0 ] )
                currNode.children.append ( newNode )
                self._insertValues ( data, newNode )
        else:
            if len ( data ) > 1:
                tmpChild = None

                for child in currNode.children:
                    if data [ 1 ] == child.value:
                        tmpChild = child
                        break

                if tmpChild:
                    self._insertValues (data [ 1: ], tmpChild )
                else:
                    newNode = Node ( value = data [ 1 ] )
                    currNode.children.append ( newNode )
                    self._insertValues ( data [ 1: ], newNode )
            else:
                currNode.is_terminal = True

    def dotFormatExport ( self, file ):
        self._dotFormatTree ( self._root, file )

    def _dotFormatTree ( self, currNode, file ):
        for child in currNode.children:
            opt = ( " [ label = " + child.value + " ]; " + str ( child.cpt ) + " [ color = \"red\" ];\n" if child.is_terminal else " [ label = " + child.value + " ];\n" )

            if not currNode.value:
                file.write ( "\t" + "0 -> " + str ( child.cpt ) + opt )
            else:
                file.write ( "\t" + str ( currNode.cpt ) + " -> " + str ( child.cpt ) + opt )

            self._dotFormatTree ( child, file )
