from pip._vendor.distlib.compat import raw_input

import textwrap

def wrap(string, max_width):
    row = ""
    for i in range(0, len(string), max_width):
        row += string[i:i+max_width] + "\n"
    return row


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print(result)