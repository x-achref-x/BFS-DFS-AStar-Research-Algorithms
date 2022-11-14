from collections import defaultdict


class Graphe():
    def __init__(self):
        self.Graphe = defaultdict(list)

    def addEdge(self, u, v):
        if v not in self.Graphe[u]:
            if v == u:
                pass
            else:
                self.Graphe[u].append(v)

    def getFrontier(self, f):
        return self.Graphe[f]


G1 = Graphe()
G1.addEdge(0, 1)
G1.addEdge(1, 2)
G1.addEdge(1, 4)
G1.addEdge(2, 3)
G1.addEdge(4, 5)
print(G1.Graphe)


Explored = []
Frontier = []


Start = int(input("Start From: "))
End = int(input("End in: "))


Frontier.append(Start)


for x in range(6):
    N = Frontier.pop(0)
    print("Exploring ", N, " Now...")
    print("   Frontier: ", Frontier)

    if N == End:
        print("____________________We Found Solution____________________")

    Frontier.extend(G1.getFrontier(N))
    print("   Frontier: ", Frontier)

    Explored.append(N)
    print("  Explored: ", Explored)






'''while i<5:
    i = i+1
    if N == End:
        print("We Found Solution")
    else:
        Explored.append(N)
        
        Frontier.extend(G1.getFrontier(N))
        print("Frontier: ",Frontier)
    if not N:
        N = Frontier.pop(-1)
    else:
        N = Frontier.pop(-1)
        print("No solution!")




#
    #N = Frontier[-1]'''

