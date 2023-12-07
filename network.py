import networkx as nx
import matplotlib.pyplot as plt
import json

g = nx.Graph()

drinkNames = []

with open('data.csv') as file:
    for line in file:
        lineList = line.split(",")
        drinkNames.append(lineList[0])
        for item in lineList:
            item.rstrip('\n')
            if item == lineList[0] or not item:
                continue
            #print(item)
            #print(type(item))
            g.add_edge(lineList[0],item)


                        



#test code
#edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]
#g = nx.from_edgelist(edge_list)
            
g.remove_node('\n') 
magic = sorted(g.degree, key=lambda x: x[1], reverse=True)
# line taken from stackoverflow from rodgdor

for item in magic:
    if item[0] not in drinkNames:
        print(item)
 
nx.draw_spring(g, with_labels ='true')
plt.show()
