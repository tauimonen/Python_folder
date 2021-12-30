from __future__ import division

from pip._vendor.distlib.compat import raw_input


def average(array):
    """
    Counts average of distinct values in array
    :param: int array
    :return: float
    """
    dist_values = set()
    for val in array:
        dist_values.add(val)
    return sum(dist_values) / len(dist_values)


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print(result)