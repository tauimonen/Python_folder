from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    s = raw_input()

    flag = False
    for c in s:
        if c.isalnum():
            print(True)
            flag = True
            break
    if not flag:
        print(False)

    flag = False
    for c in s:
        if c.isalpha():
            print(True)
            flag = True
            break
    if not flag:
        print(False)

    flag = False
    for c in s:
        if c.isdigit():
            print(True)
            flag = True
            break
    if not flag:
        print(False)

    flag = False
    for c in s:
        if c.islower():
            print(True)
            flag = True
            break
    if not flag:
        print(False)

    flag = False
    for c in s:
        if c.isupper():
            print(True)
            flag = True
            break
    if not flag:
        print(False)




