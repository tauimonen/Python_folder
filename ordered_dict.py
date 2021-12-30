from pip._vendor.distlib.compat import raw_input


if __name__ == '__main__':
    d = {}
    n = int(raw_input())
    for i in range(n):
        s = raw_input()
        spl = s.split()
        if len(spl) == 3:
            key = spl[0] + " " + spl[1]
            val = int(spl[2])
        else:
            key = spl[0]
            val = int(spl[1])

        if key not in d:
            d[key] = val
        else:
            d[key] += val

    for key, value in d.items():
        print(key, value)