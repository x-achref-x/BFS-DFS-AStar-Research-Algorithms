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


def Path(E):
    if (End in E):
        print("__________________We Found Solution_________________")

        Map = Graphe()
        for i in E:
            for j in G1.Graphe[i]:
                Map.addEdge(j, i)

        Back_Track = []
        Back_Track.append(End)
        C = Back_Track[-1]
        while C != Start:
            F = list(Map.getFrontier(C))
            Back_Track.append(F[0])
            C = Back_Track[-1]
        Back_Track.reverse()
        return Back_Track
    else:
        print("__________________NO Solution Found_________________")

##############################################################################


def BFS_DFS(OR):
    Explored = []
    Frontier = []
    Frontier.append(Start)
    Frontier.append(Start)

    while len(Frontier) > 0:
        N = Frontier.pop(OR)
        if N not in Explored:
            print("Exploring ", N, " Now...")

            if N == End:
                Explored.append(N)
                return Explored

            Frontier.extend(G1.getFrontier(N))
            print("   Frontier: ", Frontier)

            Explored.append(N)
            print("  Explored: ", Explored)
    return Explored


##############################################################################
graph = [(1, 3), (1, 2), (2, 4), (3, 4), (3, 5), (4, 7), (5, 6), (4, 7), (5, 6),
(5, 8), (6, 9), (7, 10), (8, 6), (9, 12), (10, 6), (10, 11), (12, 13)]


##############################################################################
G1 = Graphe()

for i in graph:
    G1.addEdge(i[0], i[1])
print(G1.Graphe)

##############################################################################

Start = int(input("Start From: "))
End = int(input("End in: "))
Methode = int(input("choose a method: \n1- BFS \n2- DFS\n--> "))

if Methode == 1:
    Exp = BFS_DFS(0)
if Methode == 2:
    Exp = BFS_DFS(-1)

print(Path(Exp))

###############################################################################
G2 = {
    1: [(3, 9), (2, 7), (6, 14)],
    2: [(3, 10), (4, 15)],
    3: [(4, 11), (6, 2)],
    4: [(5, 6)],
    6: [(5, 9)],
}
Path = []
Frontier = []
Start = 1
End = 5


def A():
    for x in G2[Start]:
        Frontier.append(x)
    print(Frontier)

    while len(Frontier) > 0:
        N = Frontier[0]
        for y in Frontier:
            if y[1] < N[1]:
                N = y
            if y[0] == End:
                print("___Found Solution___")
                return None
        print(N)
        Path.append(N)
        Frontier.remove(N)

        for x in G2[N[0]]:
            Edit = list(x)
            Edit[1] = Edit[1] + N[1]
            x = tuple(Edit)
            for a in Frontier:
                if x[0] == a[0]:
                    if x[1]<a[1]:
                        Frontier.append(x)
                        Frontier.remove(a)
            if x not in Frontier:
                Frontier.append(x)
        print(Frontier)


A()
print()

