#!/usr/bin/python3
""" Python Script Send POST Request """

if __name__ == "__main__":
    import sys
    import requests

    Mail1 = sys.argv[1]
    Mail2 = {"email": sys.argv[2]}
    Result = requests.post(Mail1, Mail2)
    print(Result.text)
