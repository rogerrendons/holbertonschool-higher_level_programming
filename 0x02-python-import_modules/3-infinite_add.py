#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    tam = len(sys.argv)
    if (tam > 1):
        for Iter in range(1, tam):
            res = res + int(sys.argv[Iter])
print("{:d}".format(res))
