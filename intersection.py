from pip._vendor.distlib.compat import raw_input


if __name__ == '__main__':
    set_a = set()
    set_b = set()
    v1 = raw_input()
    s1 = raw_input()
    x = s1.split(" ")
    for v in x:
        set_a.add(v)

    v2 = raw_input()
    s2 = raw_input()
    y = s2.split(" ")
    for v in y:
        set_b.add(v)

    intersection = set_a.intersection(set_b)
    c = len(intersection)
    print(c)

