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
    #Building a Map for the Graph 
    G = Graphe()
    for i in graph:
        G.addEdge(i[0], i[1])

    if (End in E):
        print("__________________We Found Solution_________________")

        Map = Graphe()
        for i in E:
            for j in G.Graphe[i]:
                Map.addEdge(j, i)
        #Backtracking from the solution to the beginning
        Back_Track = []
        Back_Track.append(End)
        C = Back_Track[-1]
        while C != Start:
            print(C)
            F = list(Map.getFrontier(C))
            Back_Track.append(F[0])
            C = Back_Track[-1]
        Back_Track.reverse()
        return Back_Track
    else:
        #if we don't have the end in the explored points meaning the there is no path to that point
        print("__________________NO Solution Found_________________")

##############################################################################


def BFS_DFS(OR):
    #Creating Dictionary using list of tuples for BFS/DFS
    for i in graph:
        G1.addEdge(i[0], i[1])
    print(G1.Graphe)

    Explored = []
    Frontier = []

    #Adding the Start to the frontier 2 times so we can delete it directly when we explore it
    #without leaving the list empty
    
    Frontier.append(Start)
    Frontier.append(Start)

    while len(Frontier) > 0:
        #using OR to indicate from where we pop the element 
        # 0 from the start for BFS and -1 from the End for DFS
        N = Frontier.pop(OR)
        if N not in Explored:
            print("Exploring ", N, " Now...")
            #checking if we have a solution
            if N == End:
                Explored.append(N)
                return Explored

            Frontier.extend(G1.getFrontier(N))
            print("   Frontier: ", Frontier)

            Explored.append(N)
            print("  Explored: ", Explored)
    #If there's no solution  
    return Explored
##############################################################################


def A():
    #Creating Dictionary using list of tuples for A*
    for i in graph:
        G1.addEdge(i[0], (i[1], abs(i[1]-i[0])))

    Path = []
    Frontier = []

    #Adding the First Frontiers from the Start
    Frontier.extend(G1.getFrontier(Start))

    while len(Frontier) > 0:
        N = Frontier[0]
        #finding the minimum heuristic in the frontier list
        for y in Frontier:
            if y[1] < N[1]:
                N = y
            #While checking in the same time if it's the ending position
            if y[0] == End:
                Path.append(y)
                Path = list(list(zip(*Path))[0])
                return Path

        print(N)
        Path.append(N)
        Frontier.remove(N)
    #if this path have frontiers whit checking if we have a better path for that point
        if N[0] in G1.Graphe:
            for x in G1.Graphe[N[0]]:
                Edit = list(x)
                Edit[1] = Edit[1] + N[1]
                x = tuple(Edit)
                for a in Frontier:
                    if x[0] == a[0]:
                        if x[1] < a[1]:
                            Frontier.append(x)
                            Frontier.remove(a)
                if x not in Frontier:
                    Frontier.append(x)
            print(Frontier)
    #If there's no solution        
    Path = list(list(zip(*Path))[0])
    return Path


###################### Add The Graph Here ###################################

graph = [(1, 3), (1, 2), (2, 4), (3, 4), (3, 5), (4, 7), (5, 6), (4, 7), (5, 6),
(5, 8), (6, 9), (7, 10), (8, 6), (9, 12), (10, 6), (10, 11), (12, 13)]


############################  Main  #########################################

G1 = Graphe()

Start = int(input("Start From: "))
End = int(input("End in: "))
Methode = int(input("choose a method: \n1- BFS \n2- DFS\n3- A*\n--> "))

if Methode == 1:
    Exp = BFS_DFS(0)
if Methode == 2:
    Exp = BFS_DFS(-1)
if Methode == 3:
    Exp = A()

print(Path(Exp))
