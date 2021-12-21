from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    res = []

    for k in range(0, x+1):
        for j in range(0, y+1):
            for i in range(0, z+1):
                if sum([k, j, i]) != n:
                    if k <= j and j <= i:
                        res.append([k, j, i])

    print(res)
