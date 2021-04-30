
class Python():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1,self.V):
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])

    def minKey(self, key, mstSet):
        min = 1000000
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [1000000] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        self.printMST(parent)
g  = Python(7)
g.graph =  [[0, 15, 8, 0, 14, 0, 0],
            [15, 0, 0, 9, 2, 0, 5],
            [8, 0, 0, 0, 0, 0, 12],
            [0, 9, 0, 0, 0, 11, 13],
            [14, 2, 0, 0, 0, 7, 0],
            [0, 0, 0, 11, 7, 0, 4],
            [0, 5, 12, 13, 0, 4, 0],
           ]
g.primMST();