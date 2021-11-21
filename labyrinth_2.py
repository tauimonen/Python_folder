from collections import deque


def find_path(graph, start, goal):
    queue = deque()
    queue.append(start)
    visited = [[False] * len(graph) for _ in range(len(graph[0]))]
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    distance = [[float('inf')] * len(graph[0]) for _ in range(len(graph))]
    distance[start[1]][start[0]] = 0
    while len(queue) > 0:
        pos = queue.pop()
        visited[pos[0]][pos[1]] = True
        if graph[pos[0]][pos[1]] == "B":
            return pos[2]
        for move in moves:
            if visited[move[1]][move[0]] or graph[move[1]][move[0]] == "#":
                continue
            visited[move[1]][move[0]] = True
            queue.appendleft(move)
            distance[move[1]][move[0]] = distance[move[1]][move[0]] + 1
        path_length = distance[goal[1]][goal[0]]
        return path_length


def count(r):
    A, B = find_start_and_goal_coordinates(r)
    return find_path(r, A, B)


def find_start_and_goal_coordinates(g):
    n = len(g)
    for i in range(n):
        for j in range(0, len(g[0])):
            if g[i][j] == "A":
                start_coordinates = (i, j)
            elif g[i][j] == "B":
                goal_coordinates = (i, j)

    return start_coordinates, goal_coordinates


if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7