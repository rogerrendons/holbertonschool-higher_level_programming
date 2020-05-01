#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    CountArg = len(argv) - 1
    if CountArg == 0:
        print(CountArg, "arguments.")
    else:
        if CountArg == 1:
            print(CountArg, "argument:")
        else:
            print(CountArg, "arguments:")
        for CArg in range(CountArg):
            print("{}:".format(CArg + 1), argv[CArg + 1])
