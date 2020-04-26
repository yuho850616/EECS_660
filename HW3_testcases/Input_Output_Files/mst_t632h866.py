import sys
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.graph = []  #to build the graph
        self.V= vertices  # nodes number
   
    def Edge(self,u,v,w): 
        self.graph.append([u,v,w])  #add nodei nodej weight to the graph
  
    def utility(self, parent, i):  #utility function
        if parent[i] == i: 
            return i 
        return self.utility(parent, parent[i]) 
  
    def union(self, parent, rank, x, y):  #union by rank
        x_start = self.utility(parent, x) 
        y_start = self.utility(parent, y) 
        if rank[x_start] > rank[y_start]: 
            parent[y_start] = x_start 
        elif rank[x_start] < rank[y_start]: 
            parent[x_start] = y_start 
        else : 
            parent[y_start] = x_start 
            rank[x_start] += 1
  
    def kruskal(self): 
        final =[]
        i = 0 
        a = 0 
        parent = []  
        rank = [] 
        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        while a < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.utility(parent, u) 
            y = self.utility(parent ,v) 
            if x != y: 
                a = a + 1     
                final.append([u,v]) 
                self.union(parent, rank, x, y)             
        for i in final:
            for j in i:
                print(j, end=" ")
            print()
f = open ( sys.argv[1] , 'r')
l = []
l = [ line.split() for line in f]
list = ( [list( map(int,i) ) for i in l] )
node_i = []
node_j = []
weight = []

for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j]!=0:
            node_i.append(i)
            node_j.append(j)
            weight.append(list[i][j])

g = Graph(len(list))

for i in range(len(node_i)):
    g.Edge(node_i[i],node_j[i],weight[i])

g.kruskal() 