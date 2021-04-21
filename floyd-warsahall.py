# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        print_solution(distance)
        print("================")


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 5, 1, INF],
         [INF, 0, INF, 3],
         [INF, 2, 0, INF],
         [INF, INF, 4, 0]]
s = [[INF, 2, 5, INF], [2, INF, 1, INF], [5, 1, INF, INF], [INF, INF, INF, INF]]
floyd_warshall(G)