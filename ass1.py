import sys, csv

fileContent = []
distinctVals = []
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
                element = tuple(line)
                fileContent.append(element)
        print fileContent
        calculate_clustering_coefficients()
    except IOError:
        print "The file " + file + " doesn't exist"

#Calculates the clustering coefficient for each of the nodes in the graph
#Should also calculate the average clustering coefficient
#Save the results into an internal data structure for an easy access
def calculate_clustering_coefficients():
    vals =[]
    i=0
    #distinctVals = sorted(map(lambda vals: vals for i in fileContent[i]: vals.append(fileContent[i][0]), fileContent))
    print(distinctVals)
if __name__ == "__main__":
    load_graph(sys.argv[1])