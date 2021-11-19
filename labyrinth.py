def count(r):
    grid_height = len(r)
    grid_width = len(r[0])

def find_start_and_goal_coordinates(g):
    n = len(g)
    start_coordinates = []
    goal_coordinates = []
    for i in range(n):
        for j in range(0, len(g[0])):
            if g[i][j] == "A":
                start_coordinates.append(1)
            elif g[i][j] == "B":
                goal_coordinates .append(0)

    return start_coordinates, goal_coordinates


if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7