from collections import defaultdict 
from graphviz import Graph

class Coloring_Graph():
   
    # Constructor
    def __init__ (self):
        self.graph = defaultdict(list)
    
    # Input from file
    def input(self, file):
        with open (file) as f:
            line = f.readline().strip().split()
            while line:
                # Adding an Edge to dict
                self.graph[int(line[0])].append(int(line[1]))
                self.graph[int(line[1])].append(int(line[0]))

                line = f.readline().strip().split()
    # Greedy coloring algorithm           
    def color(self):
        # Dict to save color
        color = defaultdict(list)
        
        for note in self.graph:
            if (len(color) == 0):
                color[0].append(note)
                continue
            else:
                for i in range(len(color)):
                    temp = 0
                    for colored_note in color[i]:
                        if (note in self.graph[colored_note]):
                            temp = 1
                            break
                    if (temp == 1):
                        continue
                    else:
                        color[i].append(note)
                        break
                if (note not in color[i]):
                    color[len(color)].append(note)    
        # Out put file
        output_file = Graph('Coloring graph', filename='Greedy Coloring Graph.gv',strict="True")
        output_file.attr( shape="circle", size='1')
        list_color=["red","blue", "yellow","green","gray","snow","DarkOrange1","MediumPurple1","khaki4","orchid", "cyan2", "blue violet", "GreenYellow", 
        "HotPink", "LightGoldenrod4","DarkSeaGreen", "sienna","brown"]
        for i in range (len(color)):
            for note in color[i]:
                output_file.node(str(note),fillcolor=list_color[i],style="filled")
                for opp_note in self.graph[note]:
                    output_file.edge(str(note),str(opp_note))
        output_file.view()  


if __name__ == "__main__":
    graph_color = Coloring_Graph()
    graph_color.input('Color.txt')
    graph_color.color()
