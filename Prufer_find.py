from collections import defaultdict

class Graph:

    # Constructor
    def __init__ (self):

        # List to save Edges (first[i]--second[i])
        self.first = []
        self.second = []

    # FUNCTION

    # Adding an Edge
    def addEdge (self, listEdge):
        self.first.append(int(listEdge[0]))
        self.second.append(int(listEdge[1]))
    
    # Importing Edge from file
    def input (self, file):

        # Reading Graph from file
        with open(file) as f:
            # Number of Vertices
            self.Edges_num = int(f.readline().strip())

            # Adding an Edge
            line = f.readline().strip().split()
            while line:

                self.addEdge (line)
                line = f.readline().strip().split()

    # Finding Prufer code
    def findprufer(self):
        list_Prufer = []
        for prufer_num in range (1, self.Edges_num):                            
            for lable in range (1, self.Edges_num + 1):                     
                count = 0 
                for i in range(len(self.first)):
                    if (lable == self.first[i]):
                        count += 1
                        index = i
                for i in range(len(self.second)):
                    if (lable == self.second[i]):
                        count += 1
                        index = i
                if (count == 1):
                    if (self.first[index] == lable):
                        list_Prufer.append(self.second[index])
                    else:
                        list_Prufer.append(self.first[index])
                    del self.first[index]
                    del self.second[index]
                    break
        return list_Prufer
def main():
    prufer = Graph()
    prufer.input('Prufercode.txt')
    print (prufer.findprufer())

if (__name__ == "__main__"):
    main()

            
    




    