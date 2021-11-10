"""
Hackerrank challenge.

The first input line contains n. The second line contains an array
of integers each separated by a space.

Printing the runner-up score.
"""

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    setti = set()
    new = []
    for value in arr:
        setti.add(value)
    for val in setti:
        new.append(val)
    new.sort()
    print(new[-2])