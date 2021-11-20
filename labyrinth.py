from collections import deque


def find_path(graph, start):
    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    visited = [[False] * len(graph) for _ in range(len(graph[0]))]
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while len(queue) > 0:
        pos = queue.pop()
        visited[pos[0]][pos[1]] = True
        if graph[pos[0]][pos[1]] == "B":
            return pos[2]
        for move in moves:
            x = pos[0] + move[0]
            y = pos[1] + move[1]
            if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) - 2:
                continue
            if visited[x][y] or graph[x][y] == "#":
                continue
            queue.appendleft((x, y, pos[2] + 1))


def count(r):
    A, B = find_start_and_goal_coordinates(r)
    find_path(r, A)


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