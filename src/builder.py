from tree import *
from visualize import *
import sys

if len ( sys.argv ) != 2:
    sys.stderr.write ( "Usage: python builder.py [ dictionary ]\n" )
else:
    tree = Tree ( )
    f = open ( sys.argv [ 1 ], 'r' )
    f.seek ( 0 )

    for word in f.readlines ( ):
        word = word.strip ( '\n' )
        tree.insert ( word )

    generateImg ( tree )
    f.close ( )
