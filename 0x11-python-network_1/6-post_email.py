#!/usr/bin/python3
""" Python Script Send POST Request """

if __name__ == "__main__":
    import sys
    import requests

    print((requests.post(sys.argv[1], {"email": sys.argv[2]})).text)
