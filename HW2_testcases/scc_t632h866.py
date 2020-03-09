import sys
import copy
from collections import defaultdict

class Scc:

    global output #output list so we can sort the list later
    output = []
    output.append([])
    global templist # temp list to record the output
    templist = []

    def __init__(self,vertices):
        self.graph = defaultdict(list) # to build the graph
        self.V= vertices #record the number of the nodes

    def Dfs(self,mark,vertex):
        mark[vertex]= True# Mark the visited node
        templist.append(vertex)
        for i in self.graph[vertex]:#run the nearby nodes
            if mark[i]==False:
                self.Dfs(mark,i)

    def Edge(self,nodea,nodeb):
        self.graph[nodea].append(nodeb) # add line to the graph

    def Opposite(self):# get the Opposite way of the graph
        instance = Scc(self.V)
        for i in self.graph: #record connected nodes to the current node
            for j in self.graph[i]:
                instance.Edge(j,i)
        return instance

    def Record_Vertices(self,mark,vertex,accumulation):
        mark[vertex]= True# Mark the visited node
        for i in self.graph[vertex]:#run the nearby nodes
            if mark[i]==False:
                self.Record_Vertices(mark,i,accumulation)
        accumulation = accumulation.append(vertex)

    def Printoutput(self): #print the output
        count = 0
        accumulation = []
        mark =[False]*(self.V)
        for i in range(self.V):
            if mark[i]==False:
                self.Record_Vertices(mark,i,accumulation)

        gr = self.Opposite()
        mark =[False]*(self.V)

        while accumulation:
            i = accumulation.pop()
            if mark[i]==False:
                gr.Dfs(mark,i)
                for j in templist:
                    output[count].append(j+1)
                count += 1
                output.append([])
                templist.clear()
        output.pop()

        for i in range (len(output)):
            output[i].sort()
        output.sort(key=lambda x: x[0])

        for row in output:
            for col in row:
                print(col, end=" ")
            print()

# Create a graph given in the above diagram
my_file = open( sys.argv[ 1 ], 'r' )
amount = my_file.readline() # the number of nodes
size = int(amount) # string to int
my_file.readline()#read the empty line
node_a = [] # outgoes node
node_b = [] # received node
temp_b = [] # 2d list to store received nodes first

x = 0
for i in range(size):
    temp = my_file.readline() # read which node outgoes to
    temp = temp.strip("\n") # remove the \n at the end of each line
    temp_b.append(temp.split(" ")) # split the whole string to each individual number

for i in range(len(temp_b)):
    for j in range(len(temp_b[i])):
        if(temp_b[i][0]!=''):
            node_a.append(i) # record the starting node number

for i in range(size-1,-1,-1):
    if (temp_b[i]==['']):
        del(temp_b[i]) # delete the empty line for received node
    else:
        temp_b[i] = list(map(int, temp_b[i])) # map int to each string number

for i in range(len(temp_b)):
    for j in range(len(temp_b[i])):
        node_b.append(temp_b[i][j]-1) # record the received node number

instance = Scc(size)# input the how many nodes we have
for i in range (len(node_a)):
    instance.Edge(node_a[i], node_b[i]) # call the egde function to build the graph
instance.Printoutput()# print the result
