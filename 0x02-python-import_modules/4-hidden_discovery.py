#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    F = dir(hidden_4)

    for cont in F:
        if cont[0] != "_":
            print("{}".format(cont))
