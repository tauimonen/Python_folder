#!/usr/bin/env python3
import re


def integers_in_brackets(s):
    found = re.findall(r'\[[ ]*[+-]?[0-9]+[ ]*\]', s)
    l = []
    for x in found:
        l.append(re.search(r'[-]?\d+', x).group(0))
    l = [int(y) for y in l]
    return l


def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))
    print(integers_in_brackets("afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"))
    # # [47, 12]

if __name__ == "__main__":
    main()