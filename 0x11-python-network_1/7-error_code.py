#!/usr/bin/python3
""" Python Script Send POST Request """
import sys
import requests

if __name__ == "__main__":

    Var = requests.get(argv[1])
    if Var.status_code >= 400:
        print("Error code: {}".format(Var.status_code))
    else:
        print(Var.text)
