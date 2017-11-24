def generateImg (tree):
    file = open ( "tree.dot", "w" )
    file.write ( "digraph Tree {\n" )

    tree.dotFormatExport ( file )

    file.write ( "}\n" )
    file.close ( )
