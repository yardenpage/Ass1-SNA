import sys, csv
from collections import Counter
edgesTuples = []
allValues = []
nodesDegreeKi = []
neighborsOfNodes = []
ValuesEi = []
ValuesCi = []
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
        #print edgesTuples
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
    distinctVals1 = list(map(lambda line: int(line[0]), edgesTuples))
    distinctVals2 = list(map(lambda line: int(line[1]), edgesTuples))
    distinctVals1.extend(distinctVals2)
    #print(distinctVals1)
    allValuesT = list(set(distinctVals1))
    #print allValuesT
    global allValues
    allValues = allValuesT
    global nodesDegreeKi
    nodesDegreeKiT = Counter(distinctVals1)
    nodesDegreeKiT = sorted(nodesDegreeKiT.items())
    nodesDegreeKi = nodesDegreeKiT
    print nodesDegreeKi

def findNeighbors():
    neighborsOfNodesT = []
    for value in allValues:
        listN = []
        i = 0
        while i < len(edgesTuples):
            if edgesTuples[i][0] == value:
                listN.append(edgesTuples[i][1])
            elif edgesTuples[i][1] == value:
                listN.append(edgesTuples[i][0])
            i = i + 1
        neighborsOfNodesT.insert(value, (value, listN))
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
        while i < len(neighbors):
            while j < len(neighbors):
                if checkConnection(index + 1, neighbors[i], neighbors[j]):
                    counter = counter + 1
                j = j + 1
            i = i + 1
            j = i + 1
        Ei.insert(index, (key, counter))
        index = index + 1
    print Ei
    global ValuesEi
    ValuesEi = Ei

def checkConnection(index, x, y):
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

def calculateCoefficients():
    i = 0
    ValuesCiT = []
    for value in allValues:
        if (nodesDegreeKi[i][1] < 2):
            Ci = 0
        else:
            Ci= 2 * float(ValuesEi[i][1]) / (float(nodesDegreeKi[i][1]) * float((nodesDegreeKi[i][1] - 1)))
        ValuesCiT.insert(i, (nodesDegreeKi[i][0], Ci))
        i = i + 1
    global ValuesCi
    ValuesCi = ValuesCiT
    print ValuesCi

#Returns the average clustering coefficient of the graph
def get_average_clustering_coefficient():
    count = len(ValuesCi)
    summary = sum(j for i,j in ValuesCi)
    average= summary/ count
    global averageCofficence
    averageCofficence = average
    print averageCofficence
    
if __name__ == "__main__":
    load_graph(sys.argv[1])
