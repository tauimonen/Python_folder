

def depth_increase(file="measures.txt"):
    """
    Count and print the number of times a depth measurement increases
    from the previous measurement. (There is no measurement before the
    first measurement.)
    """
    with open(file) as f:
        values = f.readlines()
    count = 0
    biggest_value = 0
    for value in values:
        v = int(value.strip())
        if v > biggest_value:
            count += 1
            biggest_value = v
            print(v, biggest_value)

    print(count)


if __name__ == "__main__":
    depth_increase()
