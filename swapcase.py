from pip._vendor.distlib.compat import raw_input


def swap_case(s):
    res = ""
    for c in s:
        if c.islower():
            res += c.upper()
        elif c.isupper():
            res += c.lower()
        else:
            res += c
    return res


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print(result)