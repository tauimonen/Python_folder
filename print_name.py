f"""
print_full_name has the following parameters:

string first: the first name
string last: the last name

Prints "Hello {first name} {last name}! You just delved into python." 

Input: The first line contains the first name, and the second line contains
the last name.
"""
#
from pip._vendor.distlib.compat import raw_input


def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)