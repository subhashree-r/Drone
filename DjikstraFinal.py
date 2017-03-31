# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:08:33 2017

@author: subha
"""

# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
from recipe import priorityDictionary
#from priodict import priorityDictionary

def Dijkstra(G,start,end=None):

    D = {}	# dictionary of final distances
    P = {}	# dictionary of predecessors
    Q = priorityDictionary()	# estimated distances of non-final vertices
    Q[start] = 0
        	
    for v in Q:
        D[v] = Q[v]
#        print v
        if v == end: break
        		
        for w in G[v]:
    			vwLength = D[v] + G[v][w][0]
    			if w in D:
    				if vwLength < D[w]:
    					raise ValueError, "Dijkstra: found better path to already-final vertex"
    			elif w not in Q or vwLength < Q[w]:
    				Q[w] = vwLength
    				P[w] = v
	
    return (D,P)
			
def shortestPath(G,start,end):
	
    
    D,P = Dijkstra(G,start,end)
#    print "D{0}".format(D)
#    print "P{0}".format(P)
    Path = []
    while 1:
    		Path.append(end)
    		if end == start: break
    		end = P[end]
    Path.reverse()
    return Path