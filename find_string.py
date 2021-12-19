from pip._vendor.distlib.compat import raw_input


def count_substring(string, sub_string):
    """
    Counts how many overlapping substrings is in a string and
    returns the count.
    :param string: String
    :param sub_string: String
    :return: Int
    """
    count = 0
    for i in range(len(string)):
        if (string[i:i + len(sub_string)] == sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print(count)