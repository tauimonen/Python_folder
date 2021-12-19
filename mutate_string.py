"""
mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string, .
The next line contains an integer , the index location and a string ,
separated by a space.
"""

from pip._vendor.distlib.compat import raw_input


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)


if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)