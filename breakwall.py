from heapq import heappush, heappop


def count(r):
    n = len(r)
    m = len(r[0])
    for y in range(n):
        if "A" in r[y]:
            start = (y, r[y].index("A"))
            # print("start: ", start)
    heap = []
    dist = {}
    dist[start] = 0
    heappush(heap, (0, start))
    while len(heap) > 0:
        pos = heappop(heap)[1]
        # print("pos: ", pos)
        if r[pos[0]][pos[1]] == "B":
            return dist[pos]
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            what = r[new_pos[0]][new_pos[1]]
            if what == "#":
                continue
            new_dist = dist[pos]
            if what == "*":
                new_dist += 1
            if new_pos not in dist:
                dist[new_pos] = new_dist
                heappush(heap, (new_dist, new_pos))
        return len(heap)


if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2