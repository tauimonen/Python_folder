

def depth_increase(file="measures.txt"):
    """
    Count and print the number of times a depth measurement increases
    from the previous measurement. (There is no measurement before the
    first measurement.)
    """
    with open(file) as f:
        values = f.readlines()
    count = 0
    last_value = 0
    for value in values:
        v = int(value.strip())
        if v > last_value:
            count += 1
        last_value = v

    print(count - 1)


if __name__ == "__main__":
    depth_increase()
