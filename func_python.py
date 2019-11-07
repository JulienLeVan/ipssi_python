#!/usr/bin/python3

import sys

def moy(a,b):
   "Fonction moyenne"
   c = ( a + b ) / 2
   return(c)

x = int(sys.argv[1])
y = int(sys.argv[2])

print(moy(x,y))

