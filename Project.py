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


def BFS_DFS(OR):
    Explored = []
    Frontier = []
    Frontier.append(Start)
    while True:
        N = Frontier.pop(OR)
        print("Exploring ", N, " Now...")

        if N == End:
            print("____________________We Found Solution____________________")
            break

        Frontier.extend(G1.getFrontier(N))
        print("   Frontier: ", Frontier)

        Explored.append(N)
        print("  Explored: ", Explored)
##############################################################################


graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}


##############################################################################
G1 = Graphe()
for i in graph:
    for j in graph[i]:
        G1.addEdge(int(i), int(j))
print(G1.Graphe)


Start = int(input("Start From: "))
End = int(input("End in: "))
Methode = int(input("choose a method: \n1- BFS \n2- DFS\n--> "))

if Methode == 1:
    BFS_DFS(0)
if Methode == 2:
    BFS_DFS(-1)
