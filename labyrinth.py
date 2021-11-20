from collections import deque


def find_path(graph, start, goal):
    queue = deque([("", start)])
    visited = set()

    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"


def count(r):
    y = len(r)
    x = len(r[0])

    A, B = find_start_and_goal_coordinates(r)
    find_path(r, A, B)


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