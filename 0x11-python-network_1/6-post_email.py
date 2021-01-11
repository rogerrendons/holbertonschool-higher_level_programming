#!/usr/bin/python3
""" Python Script Send POST Request """

if __name__ == "__main__":
    import sys
    import request

    Mail1 = sys.argv[1]
    Mail2 = {"email": argv[2]}
    Result = request.post(Mail1, Mail2)
    print(Result)
