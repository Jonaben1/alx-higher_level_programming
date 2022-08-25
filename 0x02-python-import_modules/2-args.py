#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    print("{:d} {:s}{:s}".format(x - 1, "argument" if x <= 2 else "arguments",
                                 "." if x == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
