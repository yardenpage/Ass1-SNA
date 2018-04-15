import sys, csv
from collections import Counter
import operator
edgesTuples = [] #pairs of edeges of nodes
allValues = [] #the nodes
nodesDegreeKi = [] #pairs of node and the number of neighbors
neighborsOfNodes = [] #pairs of node and all his neighbors
ValuesEi = [] #pairs of node and his ei value
ValuesCi = [] # pairs of node and his ci value
averageCofficence = 0

#Loads a graph from a text file to the memory.
#The text file is given as an edge list i.e, <source, destination> pairs of node ids.
#The file does not include headers
#You can assume that node ids are integers.
#See karete.csv as an example
#Make sure to load the graph into an efficient data structure
def load_graph(path):
    try:
        # read csv file
        with open(path) as fileObject:
            reader = csv.reader(fileObject.read().splitlines())
            for line in reader:
                # create for each pair a tuple
                element = [ int(x) for x in tuple(line) ]
                edgesTuples.append(element)
        print "Edges"
        print edgesTuples
        print "Number Of Edges"
        print len(edgesTuples)
        calculate_clustering_coefficients()
    except IOError:
        print "The file " + file + " doesn't exist"

#Calculates the clustering coefficient for each of the nodes in the graph
#Should also calculate the average clustering coefficient
#Save the results into an internal data structure for an easy access
def calculate_clustering_coefficients():
    calculateKi()
    findNeighbors()
    calculateEi()
    calculateCoefficients()
    get_average_clustering_coefficient()


def calculateKi():
    #get all the first elements of all the pairs
    distinctVals1 = list(map(lambda line: int(line[0]), edgesTuples))
    #get all the second elements of all the pairs
    distinctVals2 = list(map(lambda line: int(line[1]), edgesTuples))
    #union the values together
    distinctVals1.extend(distinctVals2)
    #print(distinctVals1)
    #find distinct values
    allValuesT = list(set(distinctVals1))
    global allValues
    allValues = sorted(allValuesT)
    print "Nodes"
    print allValues
    print "Number Of Nodes"
    print len(allValues)
    global nodesDegreeKi
    #count for each node how mush neighbors he has
    nodesDegreeKiT = Counter(distinctVals1)
    #sort the values
    nodesDegreeKi = sorted(nodesDegreeKiT.items())
    print "(Node, Number Of Neighbors(Ki))"
    print nodesDegreeKi

def findNeighbors():
    neighborsOfNodesT = []
    for value in allValues:
        listN = []
        i = 0
        while i < len(edgesTuples):
            #case the first element is the wanted node- we will add the second element to his neighbors list
            if edgesTuples[i][0] == value:
                listN.append(edgesTuples[i][1])
            # case the second element is the wanted node- we will add the first element to his neighbors list
            elif edgesTuples[i][1] == value:
                listN.append(edgesTuples[i][0])
            i = i + 1
        #add the list of a node and his neighbors to the total list
        neighborsOfNodesT.insert(value, (value, listN))
    print "(Node, Neighbors)"
    print neighborsOfNodesT
    global neighborsOfNodes
    neighborsOfNodes = neighborsOfNodesT

def calculateEi():
    Ei = []
    index = 0
    for value in neighborsOfNodes:
        key = value[0]
        neighbors = value[1]
        i=0
        j=1
        counter = 0
        # loop over all the elements in the neighbors list
        while i < len(neighbors):
            while j < len(neighbors):
                #check if two neighbors are neighbors of each other
                if checkConnection(neighbors[i], neighbors[j]):
                    counter = counter + 1
                j = j + 1
            i = i + 1
            j = i + 1
        #insert the number of ei of the node to the total list
        Ei.insert(index, (key, counter))
        index = index + 1
    global ValuesEi
    ValuesEi = sorted(Ei)
    print "(Node, Number Of Connections Betweens Neighbors(Ei))"
    print(ValuesEi)

#check if two nodes are neighbors
def checkConnection(x, y):
    index=0
    while index < len(neighborsOfNodes):
        if neighborsOfNodes[index][0] == x:
            i = 0
            while i < len(neighborsOfNodes[index][1]):
                if neighborsOfNodes[index][1][i] == y:
                    return 1
                i = i + 1
            return 0
        index = index + 1
    return 0

#use the formula to calculate ci values
def calculateCoefficients():
    i = 0
    ValuesCiT = {}
    for value in allValues:
        if (nodesDegreeKi[i][1] < 2):
            Ci = 0.0
        else:
            mechane = (float(nodesDegreeKi[i][1]) * float(nodesDegreeKi[i][1] - 1))
            mone = 2 * float(ValuesEi[i][1])
            Ci= mone / mechane
        ValuesCiT[nodesDegreeKi[i][0]]= Ci
        i = i + 1
    global ValuesCi
    ValuesCi = ValuesCiT
    print "(Node: Coefficient (Ci))"
    print ValuesCi

#Returns the average clustering coefficient of the graph
def get_average_clustering_coefficient():
    count = len(ValuesCi)
    summary = sum(ValuesCi.values())
    average= summary/ count
    global averageCofficence
    averageCofficence = average
    print "Average Coefficient"
    print averageCofficence

#Returns the clustering coefficient of a specific node
#Returns -1 for non-existing Id
def get_clustering_coefficient(node_id):
    if node_id in ValuesCi:
        return ValuesCi[node_id]
    return -1

# Returns a list of the clustering coefficients for all the nodes in the graph
# The list should include pairs of node id, clustering coefficient value of that node.
# The list should be ordered according to the clustering coefficient values of high to low
def get_all_clustering_coefficients():
    sortedList = sorted(ValuesCi.items(), key=operator.itemgetter(1), reverse= True)
    return sortedList

if __name__ == "__main__":
    load_graph(sys.argv[1])
    #print get_clustering_coefficient(3)
    print "(Node: Coefficient (Ci))"
    print get_all_clustering_coefficients()
