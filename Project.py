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
##############################################################################


def Path():
    P = []
    P.append(End)
    C = P[-1]
    while C != Start:
        F = list(M1.getFrontier(C))
        P.append(F[0])
        C = P[-1]
    P.reverse()
    print(P)


##############################################################################

def BFS_DFS(OR):
    Explored = []
    Frontier = []
    Frontier.append(Start)

    while True:
        N = Frontier.pop(OR)
        if N not in Explored:
            print("Exploring ", N, " Now...")
            for i in G1.Graphe[N]:
                M1.addEdge(i, N)

            if N == End:
                print("__________________We Found Solution__________________")
                break

            Frontier.extend(G1.getFrontier(N))
            print("   Frontier: ", Frontier)

            Explored.append(N)
            print("  Explored: ", Explored)


##############################################################################
graph = {
  '1': ['3', '2'],
  '2': ['4'],
  '3': ['4', '5'],
  '4': ['7'],
  '5': ['6', '8'],
  '6': ['9'],
  '7': ['10'],
  '8': ['6'],
  '9': ['12'],
  '10': ['6', '11'],
  '12': ['13']
}


##############################################################################
G1 = Graphe()
M1 = Graphe()
for i in graph:
    for j in graph[i]:
        G1.addEdge(int(i), int(j))
print(G1.Graphe)

##############################################################################

Start = int(input("Start From: "))
End = int(input("End in: "))
Methode = int(input("choose a method: \n1- BFS \n2- DFS\n--> "))

if Methode == 1:
    BFS_DFS(0)
if Methode == 2:
    BFS_DFS(-1)

Path()
