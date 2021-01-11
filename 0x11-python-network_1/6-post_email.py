#!/usr/bin/python3
""" Python Script Send POST Request """
import sys
import requests

if __name__ == "__main__":

    print((requests.post(sys.argv[1], {"email": sys.argv[2]})).text)
