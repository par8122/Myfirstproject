#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:58:27 2019


"""

#dict subclass that calls a factory function to supply missing values
from collections import defaultdict

class Graph():
    def __init__(self):
        #self.edges is the dict of all the possible next nodes {'a':['b','f']}
        self.edges = defaultdict(list)
        #self.weights from two nodes have all weights,
        #('a', 'b', 10),('a', 'f', 13),
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        #assumes that the edges are two-way
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

#Create an empty graph with no edges.
G = Graph()

#adding a list of edges
edges = [
    ('a', 'b', 10),('a', 'f', 13),('b', 'c', 17),('b', 'g', 7),('c', 'd', 7),
    ('c', 'h', 3),('d', 'e', 14),('d', 'i', 9),('e', 'j', 13),('f', 'g', 6),
    ('f', 'k', 15),('g', 'h', 5),('g', 'l', 10),('h', 'i', 18),('h', 'm', 7),
    ('i', 'j', 4),('i', 'n', 2),('j', 'o', 4),('k', 'l', 5),('k', 'p', 17),
    ('l', 'm', 8),('l', 'q', 13),('m', 'n', 7),('m', 'r', 9),('n', 'o', 20),
    ('n', 's', 14),('o', 't', 7),('p', 'q', 14),('q', 'r', 11),('r', 's', 9),
    ('s', 't', 12),
]

#single edge as tuple of two nodes
for e in edges:
    G.add_edge(*e)
    
#print(G.weights)
    
    

def DijkstraAlg(G, initial, end):
    #Assigning to every node a tentative distance
    #set the distance for intital node to zero
    shtst_path = {initial: (None, 0)}
    #Add the starting node as the initial
    C_node = initial
    #Add the visited node
    visited = set()
    
    while C_node != end:
        #Visit the current node
        visited.add(C_node)
        #look at the neighboure nodes 
        dest = G.edges[C_node]
        #weights of the nodes currently being visited
        weight_to_c_node = shtst_path[C_node][1]
    
       #weight of the edge where the current node and the next node are connected
       #and add weight to current node
        for N_node in dest:
            weight = G.weights[(C_node, N_node)] + weight_to_c_node
            
            #Add current node if not in shortest path
            if N_node not in shtst_path:
                shtst_path[N_node] = (C_node, weight)
            else:
                #If it is in shortest path 
                c_shtst_weight = shtst_path[N_node][1]
                #Update if current the current weight is low
                if c_shtst_weight > weight:
                    shtst_path[N_node] = (C_node, weight)
                    
                    #print([C_node], [weight])
        #The next node to move to the node not visited on the shortest path
        next_dest = {node: shtst_path[node] for node in
                     shtst_path if node not in visited}
        
        #print('Current_node Neighbours:',[next_dest])
        #print('Current_node:',[weight_to_c_node])
        #print('')
        
     #all weighted current nodes
        #print((C_node, weight_to_c_node))

        #The next node is the lowest weight destination
        C_node = min(next_dest, key=lambda k: next_dest[k][1])
        
        
    #The current (C_node) is the destination node
    dest_node = C_node
    #start going back in the shortest possible way through destinations
    #Add node by moving from destination to source
    path = []
    #Repeat until you get the start node
    while dest_node != None:
        path.append(dest_node)
        #Select the next node 
        N_node = shtst_path[dest_node][0]
        #print('next', N_node)
        dest_node = N_node
    #Reverse the list   
    path = path[::-1]
    return path

print('Dijkstra Algorithm')
print('=========================')
#Here start node is 'a' and the target node is 't
print('Shortest path from a -> t is:')
print(DijkstraAlg(G, 'a', 't'))




