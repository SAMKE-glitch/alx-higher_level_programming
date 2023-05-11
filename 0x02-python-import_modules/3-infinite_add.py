#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = int(len(sys.argv) - 1)
    if count == 0:
        print(0)
    else:
    total = 0
    for arg in sys.argv[1:]:
        total += count
        print(total)

